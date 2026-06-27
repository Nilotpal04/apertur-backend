from app.models.user import User
from app.models.post import Post
from beanie.operators import In
from app.models.like import Like
from app.schemas.feed import (
    FeedPostResponse,
    FeedResponse
)

async def get_feed_service(
    current_user: User | None = None,
    cursor: str | None = None,
    limit: int = 20
):
    posts = await Post.find().sort(-Post.id).limit(limit).to_list()
    
    author_ids = set()
    author_ids = {post.author_id for post in posts}
    users = await User.find(In(User.id, list(author_ids))).to_list()
    users_map = {str(user.id): user for user in users}
    
    feed_posts: list[FeedPostResponse] = []
    for post in posts:
        author = users_map.get(post.author_id)
        
        if author:
            feed_post = FeedPostResponse(
                id= str(post.id),
                username= author.username,
                avatar_url= author.avatar_url,
                content= post.content,
                image_url= post.image_url
            )
            feed_posts.append(feed_post)
    post_ids = {str(post.id) for post in posts}
    likes = await Like.find(In(Like.post_id, list(post_ids))).to_list()
    likes_count_map: dict[str, int] = {}
    
    liked_posts = set()

    if current_user:
        liked_posts = {
            like.post_id
            for like in likes
            if like.user_id == str(current_user.id)
        }
    for like in likes:
        likes_count_map[like.post_id] = (
            likes_count_map.get(like.post_id, 0) + 1
        )
    next_cursor = None

    if posts:
        last_post = posts[-1]
        next_cursor= str(last_post.id)

    return FeedResponse(
        posts=feed_posts,
        next_cursor=next_cursor,
        likes_count=likes_count_map.get(str(post.id), 0),
        liked_by_user=(
            str(post.id) in liked_posts
            if current_user
            else None
        )
    )