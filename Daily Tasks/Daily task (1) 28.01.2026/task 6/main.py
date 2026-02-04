from simple_cache import SimpleCache

cache = SimpleCache()

cache.set("token", "123456", ttl=60)
cache.set("user", "Mancho")

print(cache.get("token"))
print(cache.get("user"))