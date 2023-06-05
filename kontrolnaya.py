import datetime


class Post:
    def __init__(self, author, text,):
        self.author = author
        self.text = text
        self.likes = 0
        self.comments = []
        self.timestamp = datetime.now()
        self.curse = 0

    def add_like(self):
        self.likes += 1
    def get_like(self):
        return self.likes
    def set_comments(self,comment):
        self.comments.append(comment)
    def get_comments(self):
        return self.comments

kaplan = Post("Kaplan", "I'm going by Kaplan Mobile")
kaplan.set_likes(112.432)
print(kaplan.get_like())
kaplan.set_comments("YEY")

comments = kaplan.get_comments()
for i in range(len(kaplan.get_comments())):
    print("Комментарий №", i, comments[i])
