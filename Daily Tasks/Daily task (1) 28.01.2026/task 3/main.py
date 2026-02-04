from memory_storage import MemoryStorage

storage = MemoryStorage()

storage.save("username", "Mancho")
storage.save("age", 17)

print(storage.load("username"))
print(storage.load("age"))