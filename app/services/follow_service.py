from app.models.follow import Follow
from app.models.user import User

from app.schemas.follow import FollowResponse

from app.exceptions.user_exception import (
    UserNotFoundException
)
from app.exceptions.follow_exceptions import (
    SelfFollowException
)
async def follow_user_service(
    username: str,
    current_user: User
):
    target_user = await User.find_one(User.username == username)
    if not target_user:
        raise UserNotFoundException()
    
    if str(current_user.id) == str(target_user.id):
        raise SelfFollowException()
    
    follow = await Follow.find_one(
        Follow.follower_id == str(current_user.id),
        Follow.following_id == str(target_user.id)
    )
    
    if not follow:
        follow = Follow(
            follower_id= str(current_user.id),
            following_id= str(target_user.id)
        )
        
        await follow.insert()
    
    followers_count = await Follow.find(Follow.following_id == str(target_user.id)).count()
    
    return FollowResponse(
        following= True,
        followers_count=followers_count
    )
    
async def unfollow_user_service(
    username: str,
    current_user: User
):
    target_user = await User.find_one(User.username == username)
    if not target_user:
        raise UserNotFoundException()
    
    follow = await Follow.find_one(
        Follow.follower_id == str(current_user.id),
        Follow.following_id == str(target_user.id)
    )
    
    if follow:
        await follow.delete()
    
    followers_count = await Follow.find(Follow.following_id == str(target_user.id)).count()
    
    return FollowResponse(
        following= False,
        followers_count=followers_count
    )