from app.models.like import Like
from app.models.post import Post
from app.models.user import User


from app.schemas.like import LikeResponse
from app.exceptions.post_exceptions import (
    PostNotFoundException
)

from app.services.notification import create_notification_service
from app.enums.notification_type import NotificationType

async def like_post_service(
    post_id: str,
    current_user: User
):
    post = await Post.get(post_id)
    if not post:
        raise PostNotFoundException()
    
    condition1 = Like.post_id == post_id
    condition2 = Like.user_id == str(current_user.id)
    
    liked = await Like.find_one(condition1, condition2)
    
    if not liked:
        like = Like(
            user_id= str(current_user.id),
            post_id= post_id,
        )
        await like.insert()
        await create_notification_service(
            recipient_id=str(post.author_id),
            actor_id=str(current_user.id),
            notification_type=NotificationType.LIKE,
            post_id=post_id
        )   
    likes_count = await Like.find(Like.post_id == post_id).count()
    return LikeResponse(
        liked=True,
        likes_count= likes_count
    )
    
async def unlike_post_service(
    post_id: str,
    current_user: User
):
    post = await Post.get(post_id)
    if not post:
        raise PostNotFoundException()
    
    condition1 = Like.post_id == post_id
    condition2 = Like.user_id == str(current_user.id)
    
    liked = await Like.find_one(condition1, condition2)
    
    if liked:
        await liked.delete()
    
    likes_count = await Like.find(Like.post_id == post_id).count()
    return LikeResponse(
        liked= False,
        likes_count=likes_count
    )
    