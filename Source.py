
from xata.client import XataClient

xata = XataClient(api_key="xau_zlmLvwInrSgCgQNwpgEQHiCmLLHBm6JH0", branch_name="master")

# Define table schemas
user_table_schema = {
    "name": "User",
    "columns": [
        {"name": "id", "type": "int", "primary_key": True},
        {"name": "username", "type": "string", "unique": True, "nullable": False},
        {"name": "email", "type": "string", "unique": True, "nullable": False},
        {"name": "password", "type": "string", "nullable": False},
        {"name": "profile_picture", "type": "string", "length": 255},
        {"name": "bio", "type": "text"},
        {"name": "private_status", "type": "bool", "default": False},
        {"name": "verified_status", "type": "bool", "default": False}
    ]
}

user_records = [
    {"id": 1, "username": "user1", "email": "user1@example.com", "password": "password1"},
    {"id": 2, "username": "user2", "email": "user2@example.com", "password": "password2"}
]

def insert_user_record(user_data):
    resp = xata.records().insert("User", user_data)
    assert resp.is_success()
    print("Record Id: %s" % resp["id"])

post_table_schema = {
    "name": "Post",
    "columns": [
        {"name": "id", "type": "int", "primary_key": True},
        {"name": "user_id", "type": "int", "foreign_key": "User.id", "nullable": False},
        {"name": "post_type", "type": "string", "length": 10, "nullable": False},
        {"name": "content", "type": "text", "nullable": False},
        {"name": "timestamp", "type": "datetime", "default": "CURRENT_TIMESTAMP"},
        {"name": "location", "type": "string", "length": 50, "nullable": True}
    ]
}

follower_table_schema = {
    "name": "Follower",
    "columns": [
        {"name": "id", "type": "int", "primary_key": True},
        {"name": "follower_id", "type": "int", "foreign_key": "User.id", "nullable": False},
        {"name": "following_id", "type": "int", "foreign_key": "User.id", "nullable": False},
        {"name": "timestamp", "type": "datetime", "default": "CURRENT_TIMESTAMP"}
    ]
}

hashtag_table_schema = {
    "name": "Hashtag",
    "columns": [
        {"name": "id", "type": "int", "primary_key": True},
        {"name": "name", "type": "string", "unique": True, "nullable": False}
    ]
}

like_table_schema = {
    "name": "Like",
    "columns": [
        {"name": "id", "type": "int", "primary_key": True},
        {"name": "user_id", "type": "int", "foreign_key": "User.id", "nullable": False},
        {"name": "post_id", "type": "int", "foreign_key": "Post.id", "nullable": False},
        {"name": "timestamp", "type": "datetime", "default": "CURRENT_TIMESTAMP"}
    ]
}

comment_table_schema = {
    "name": "Comment",
    "columns": [
        {"name": "id", "type": "int", "primary_key": True},
        {"name": "user_id", "type": "int", "foreign_key": "User.id", "nullable": False},
        {"name": "post_id", "type": "int", "foreign_key": "Post.id", "nullable": False},
        {"name": "content", "type": "text", "nullable": False},
        {"name": "timestamp", "type": "datetime", "default": "CURRENT_TIMESTAMP"}
    ]
}

post_hashtag_association_table_schema = {
    "name": "PostHashtag",
    "columns": [
        {"name": "post_id", "type": "int", "foreign_key": "Post.id", "nullable": False},
        {"name": "hashtag_id", "type": "int", "foreign_key": "Hashtag.id", "nullable": False}
    ]
}

notification_table_schema = {
    "name": "Notification",
    "columns": [
        {"name": "id", "type": "int", "primary_key": True},
        {"name": "user_id", "type": "int", "foreign_key": "User.id"}
    ]
}

assert xata.table().create("User").is_success()

# Set the schema for the "User" table
resp = xata.table().set_schema("User", user_table_schema["columns"])  # Pass only the "columns" part of the schema

# Check if the operation was successful
if resp.is_success():
    print("Schema set successfully for table 'User'.")
else:
    print("Failed to set schema. Error:", resp)

'''# Create the "User" table
assert xata.table().create("User").is_success()

# Set the schema for the "User" table
resp = xata.table().set_schema("User", user_table_schema)

# Check if the operation was successful
if resp.is_success():
    print("Schema set successfully for table 'User'.")
else:
    print("Failed to set schema. Error:", resp)'''

'''# Create the "User" table
assert xata.table().create(user_table_schema["name"]).is_success()

# Set the schema for the "User" table
resp = xata.table().set_schema(user_table_schema["name"], user_table_schema)

# Check if the operation was successful
if resp.is_success():
    print("Schema set successfully for table 'User'.")
else:
    print("Failed to set schema. Error:", resp)'''