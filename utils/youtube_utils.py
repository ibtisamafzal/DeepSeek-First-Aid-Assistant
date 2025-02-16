import requests
import os

def get_youtube_video(query):
    """Search for a relevant first aid video on YouTube."""
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
    if not YOUTUBE_API_KEY:
        raise ValueError("Please set your YOUTUBE_API_KEY in the .env file.")
    
    try:
        base_url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            'part': 'snippet',
            'q': f"how to treat {query} first aid medical emergency",
            'key': YOUTUBE_API_KEY,
            'maxResults': 1,
            'type': 'video'
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if 'items' in data and len(data['items']) > 0:
            video_id = data['items'][0]['id']['videoId']
            return f"https://www.youtube.com/watch?v={video_id}"
        return None
    except Exception as e:
        raise Exception(f"Error fetching YouTube video: {str(e)}")