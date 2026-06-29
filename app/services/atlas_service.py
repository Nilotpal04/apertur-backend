from datetime import datetime, timedelta, timezone
from app.models.post import Post
from app.models.user import User
from bson import ObjectId

from app.schemas.atlas import AtlasPostResponse
ATLAS_VISIBLE_HOURS = 24
async def get_atlas_post_service():
    
    cutoff = datetime.now(timezone.utc) - timedelta(hours=ATLAS_VISIBLE_HOURS)
    
    posts = await Post.find(
        Post.created_at >= cutoff,
        Post.latitude != None,
        Post.longitude != None,
    ).sort(-Post.created_at).to_list()
    if not posts:
        return []
    
    author_ids = {post.author_id for post in posts}
    users = await User.find(
        {
            "_id": {
                "$in": [ObjectId(id) for id in author_ids]
            }
        }
    ).to_list()
    users_map = {str(user.id): user for user in users}
    
    atlas_posts = []
    
    for post in posts:
        author = users_map.get(post.author_id)
        
        if not author:
            continue
        
        atlas_posts.append(
            AtlasPostResponse(
                post_id=str(post.id),
                username=author.username,
                avatar_url=author.avatar_url,
                image_url=post.image_url,
                latitude=post.latitude,
                longitude=post.longitude,
                location_name=post.location_name,
                created_at=post.created_at,
            )
        )
    
    return atlas_posts