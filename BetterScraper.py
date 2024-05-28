import praw
# from text_gen import gpt_summarize

# Initialize the Reddit instance
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT'
)

def scrapeRedditPostByURL(url):
    # Step 1: Extract the submission ID from the URL
    submission_id = url.split('/')[-3]

    # Step 2: Fetch the submission using praw
    submission = reddit.submission(id=submission_id)

    # Step 3: Extract specific data
    title = submission.title
    post_paragraphs = []

    # If the submission has selftext (text content), add it to the post_paragraphs
    if submission.selftext:
        post_paragraphs.append(submission.selftext)

    # Return the data as a dictionary
    return {
        'title': title,
        'post_paragraphs': post_paragraphs,
    }

def polish(data):
    print(data)

# Example usage
url = 'https://www.reddit.com/r/subreddit/comments/post_id/post_title/'
data = scrapeRedditPostByURL(url)
polish(data)
