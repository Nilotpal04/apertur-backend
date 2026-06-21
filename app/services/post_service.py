from app.models.post import Post
from app.models.user import User

from app.schemas.post import (
    PostCreate,
    PostResponse
)

async def create_post_service(post_data: PostCreate, current_user: User):
    post = Post(
        author_id=str(current_user.id),
        content=post_data.content,
        image_url=post_data.image_url
    )
    
    await post.insert
    
    return PostResponse(
        id=str(post.id),
        content=post.content,
        image_url=post.image_url,
        created_at=post.created_at
    )

async def get_post_service(post_id: str):
    post = await Post.get(post_id)
    if not Post:
        raise PostNotFoundException()
    return PostResponse(
        id=str(post.id),
        content=post.content,
        image_url=post.image_url,
        created_at=post.created_at
    )