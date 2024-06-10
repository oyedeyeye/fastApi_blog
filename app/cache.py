from cachetools import TTLCache

# Define a cache for posts with a TTL of 5 minutes
posts_cache = TTLCache(maxsize=100, ttl=300)

def get_posts_cache(user_id: int):
    """
    Retrieve cached posts for a user.
    """
    return posts_cache.get(user_id)

def set_posts_cache(user_id: int, posts):
    """
    Cache the posts for a user.
    """
    posts_cache[user_id] = posts
