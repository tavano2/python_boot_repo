facebook_posts = eval(input())

total_likes = 0
try:
    for post in facebook_posts:
        total_likes = total_likes + post['Likes']
except KeyError:
    total_likes += 0
finally:
    print(total_likes)
