class Comment:
    def __init__(self, name: str, text: str, numbers: int = 0) -> None:
        self.username = name
        self.content = text
        self.likes = numbers


comment = Comment("user1", "I like this book", 20)
print(comment.username)
print(comment.content)
print(comment.likes)
