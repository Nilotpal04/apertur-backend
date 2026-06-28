from app.models.frame import Frame
from app.models.post import Post
from app.models.user import User
from app.models.like import Like

from beanie.operators import In

from app.schemas.frame import (
    FrameResponse
)
from app.schemas.feed import FeedPostResponse

from app.exceptions.post_exceptions import PostNotFoundException
from app.exceptions.user_exception import UserNotFoundException

async def frame_post_service(
    post_id: str,
    current_user: User
):
    post = await Post.get(post_id)
    if not post:
        raise PostNotFoundException()
    
    framed = await Frame.find_one(
        Frame.post_id == post_id,
        Frame.user_id == str(current_user.id)
    )
    
    if not framed:
        frame = Frame(
            user_id= str(current_user.id),
            post_id= post_id
        )
        
        await frame.insert()
        
    frames_count = await Frame.find(Frame.post_id == post_id).count()
    return FrameResponse(
        framed=True,
        frames_count=frames_count
    )

async def unframe_post_service(
    post_id: str,
    current_user: User
):
    post = await Post.get(post_id)
    if not post:
        raise PostNotFoundException()
    
    framed = await Frame.find_one(
        Frame.post_id == post_id,
        Frame.user_id == str(current_user.id)
    )
    
    if framed:
        await framed.delete()
    
    frames_count = await Frame.find(Frame.post_id == post_id).count()
    return FrameResponse(
        framed=False,
        frames_count=frames_count
    )

async def get_user_frames_service(
    username: str
):
    user = await User.find_one(User.username == username)

    if not user:
        raise UserNotFoundException()

    frames = await Frame.find(Frame.user_id == str(user.id)).to_list()
    if not frames:
        return []

    post_ids = {frame.post_id for frame in frames}
    posts = await Post.find(In(Post.id, list(post_ids))).to_list()
    author_ids = {post.author_id for post in posts}
    users = await User.find(In(User.id, list(author_ids))).to_list()

    users_map = {
        str(user.id): user
        for user in users
    }

    likes = await Like.find(In(Like.post_id, list(post_ids))).to_list()
    likes_count_map = {}

    for like in likes:
        likes_count_map[like.post_id] = (
            likes_count_map.get(like.post_id, 0) + 1
        )
        
    all_frames = await Frame.find(In(Frame.post_id, list(post_ids))).to_list()
    frames_count_map = {}

    for frame in all_frames:
        frames_count_map[frame.post_id] = (
            frames_count_map.get(frame.post_id, 0) + 1
        )

    feed_posts: list[FeedPostResponse] = []

    for post in posts:
        author = users_map.get(str(post.author_id))

        if not author:
            continue

        feed_posts.append(
            FeedPostResponse(
                id=str(post.id),
                username=author.username,
                avatar_url=author.avatar_url,
                content=post.content,
                image_url=post.image_url,
                likes_count=likes_count_map.get(str(post.id), 0),
                frames_count=frames_count_map.get(str(post.id), 0),
            )
        )

    return feed_posts
    