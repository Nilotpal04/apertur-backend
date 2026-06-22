from app.models.post import Post
from app.models.user import User

from app.schemas.post import (
    PostCreate,
    PostResponse,
    PostUpdate
)
from app.exceptions.post_exceptions import (
    PostNotFoundException,
    PostOwnershipException
)

from app.exceptions.user_exception import UserNotFoundException
from datetime import datetime

async def create_post_service(post_data: PostCreate, current_user: User):
    post = Post(
        author_id=str(current_user.id),
        content=post_data.content,
        image_url=post_data.image_url
    )
    
    await post.insert()
    
    return PostResponse(
        id=str(post.id),
        content=post.content,
        image_url=post.image_url,
        created_at=post.created_at
    )

async def get_post_service(post_id: str):
    post = await Post.get(post_id)
    if not post:
        raise PostNotFoundException()
    return PostResponse(
        id=str(post.id),
        content=post.content,
        image_url=post.image_url,
        created_at=post.created_at
    )

async def get_user_posts_service(username: str):
    user = await User.find_one(
        User.username == username
    )
    
    if not user:
        raise UserNotFoundException()
    
    posts = await Post.find(
        Post.author_id == str(user.id)
    ).sort( -Post.created_at).to_list()
    
    return [
        PostResponse(
            id=str(post.id),
            content=post.content,
            image_url=post.image_url,
            created_at=post.created_at
        ) for post in posts
    ]
    
async def update_post_service(
    post_id: str,
    post_data: PostUpdate,
    current_user: User
):
    post = await Post.get(post_id)
    if not post:
        raise PostNotFoundException()
    if post.author_id != str(current_user.id):
        raise PostOwnershipException()
    update_data = post_data.model_dump(
        exclude_unset=True
    )
    for field, value in update_data.items():
        setattr(post, field, value)
        
    post.updated_at = datetime.utcnow()
    
    await post.save()
    
    return PostResponse(
        id=str(post.id),
        content=post.content,
        image_url=post.image_url,
        created_at=post.created_at
    )
    
async def delete_post_service(
    post_id: str,
    current_user: User
):
    post = await Post.get(post_id)
    if not post:
        raise PostNotFoundException()
    if post.author_id != str(current_user.id):
        raise PostOwnershipException()
    await post.delete()
    
    return {
        "message": "Post deleted successfully"
    }