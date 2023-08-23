from president import President

p = President(40)
print(p.first_name, p.last_name)

field_name = "birth_place"

print(f"getattr(p, field_name): {getattr(p, field_name)}\n")

print(f"hasattr(p, 'assassinated'): {hasattr(p, 'assassinated')}")

print(f"getattr(p, 'wombat', 'whoops'): {getattr(p, 'wombat', 'whoops')}")

def full_name(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, "full_name", full_name)

print(f"p.full_name(): {p.full_name()}")



