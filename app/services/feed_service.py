from app.models.user import User
from app.models.post import Post
from beanie.operators import In

from app.schemas.feed import (
    FeedPostResponse,
    FeedResponse
)

async def get_feed_service(
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
    next_cursor = None

    if posts:
        last_post = posts[-1]
        next_cursor= str(last_post.id)

    return FeedResponse(
        posts=feed_posts,
        next_cursor=next_cursor
    )