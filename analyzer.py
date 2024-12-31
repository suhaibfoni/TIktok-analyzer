def analyze_fake_likes(comments_data):
    fake_likes = []
    real_likes = []

    for comment in comments_data:
        username, comment_text, likes = comment
        if likes > 500 and username != "@suhaib_.5":  # Example threshold
            fake_likes.append((username, comment_text, likes))
        else:
            real_likes.append((username, comment_text, likes))
    
    return real_likes, fake_likes
