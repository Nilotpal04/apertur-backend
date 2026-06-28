from app.models.frame import Frame
from app.models.post import Post
from app.models.user import User

from app.schemas.frame import (
    FrameResponse
)

from app.exceptions.post_exceptions import PostNotFoundException

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