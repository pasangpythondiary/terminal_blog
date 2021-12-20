# import pymongo
#
# uri="mongodb://127.0.0.1:27017"
# client=pymongo.MongoClient(uri)
# database=client['terminal_blog']
# collection=database['students']
#
# students=collection.find({})
# print(students)


from database import Database
from models.post import Post

Database.initialize()

from models.post import Post
post= Post(blog_id="123", title="another great post", content="this is good title", author="pasang")
post.save_to_mongo()


