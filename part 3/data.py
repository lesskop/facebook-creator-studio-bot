username = ''
password = ''

link = 'https://business.facebook.com/creatorstudio/home'

num_of_photo = 0
num_of_video = 0

# write path to your content
cats_photo = [rf'\photo ({i}).jpg' for i in range(1, num_of_photo + 1)]
cats_video = [rf'\video ({i}).mp4' for i in range(1, num_of_video + 1)]
cats_content = cats_video + cats_photo

tags_cats = ['cats', 'catsofinstagram', 'cat', 'of', 'catstagram', 'instagram', 'catlovers', 'catlover', 'catlife',
             'instacat', 'meow', 'pets', 'kittens', 'kitten', 'kitty', 'catoftheday', 'love', 'cute', 'pet', 'animals',
             'dogs', 'gatos', 'world', 'gato', 'petsofinstagram', 'adoptdontshop', 'kittensofinstagram', 'cutecats',
             'lovecats', 'bhfyp', 'cutecat', 'catsofig', 'catlove', 'instacats', 'petstagram', 'animal', 'dog',
             'kittycat', 'ilovemycat', 'catslover', 'catsofinsta', 'catloversclub', 'catscatscats', 'instagood', 'day',
             'dogsofinstagram', 'blackcat', 'katze', 'photooftheday', 'ilovecats', 'catsofworld', 'catsoftheworld',
             'catworld', 'katzen', 'caturday', 'chat', 'neko', 'nature', 'gatosdeinstagram', 'photography']

tags_follow = ['follow', 'like', 'love', 'instagood', 'instagram', 'photooftheday', 'followme', 'photography',
               'likeforlikes', 'picoftheday', 'fashion', 'beautiful', 'me', 'instadaily', 'likes', 'smile',
               'followforfollowback', 'instalike', 'myself', 'happy', 'f', 'followback', 'l', 'style', 'art',
               'followers', 'likeforfollow', 'followforfollow', 'bhfyp', 'likeforlike', 'life', 'comment', 'cute',
               'model', 'girl', 'nature', 'beauty', 'selfie', 'likesforlikes', 'fun', 'travel', 'photographer',
               'motivation', 'music', 'makeup', 'memes', 'quotes', 'lifestyle', 'photoshoot', 'portrait', 'igers',
               'following', 'insta', 'friends', 'fitness', 'tiktok', 'food', 'inspiration', 'share']

tags_like = ['likes', 'like', 'follow', 'likeforlikes', 'love', 'instagood', 'instagram', 'followforfollowback',
             'followme', 'photooftheday', 'bhfyp', 'instalike', 'photography', 'l', 'instadaily', 'me', 'picoftheday',
             'beautiful', 'myself', 'likeforfollow', 'fashion', 'smile', 'followers', 'likeforlike', 'followback',
             'f', 'followforfollow', 'comment', 'likesforlikes', 'bhfyp', 'happy', 'style', 'life', 'photo', 'nature',
             'cute', 'insta', 'model', 'music', 'travel', 'likesforlike', 'girl', 'selfie', 'viral', 'loveyourself',
             'following', 'memes', 'beauty', 'liker', 'lfl', 'yourself', 'lifestyle', 'likeback', 'sad', 'thoughts',
             'writer', 'photographer', 'k', 'photoshoot', 'india']

tags = list(set(tags_like + tags_cats + tags_follow))

locations = ['Taganrog Old Cemetery', 'New York', 'Los Angeles, California', 'San Francisco, California',
             'Paris, France', 'Alabama', 'Barcelona, Spain', 'Madrid, Spain', 'Melbourne, Australia',
             'Sydney, Australia', 'Bangkok, Thailand', 'Jakarta, Indonesia', 'Amsterdam, Netherlands',
             'Chicago, Illinois', 'Santiago, Chile', 'San Diego, California', 'Houston, Texas',
             'Mexico City, Mexico']
