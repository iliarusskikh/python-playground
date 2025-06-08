import requests

def get_posts():
    """Retrieve a list of posts using a GET request."""
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        print(f"\nGET Request to {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers['content-type']}")
        if response.status_code == 200:
            posts = response.json()
            print(f"First Post: {posts[0]}")
            print(f"Total Posts: {len(posts)}")
        else:
            print(f"Error: {response.text}")
    except requests.RequestException as e:
        print(f"GET Request failed: {e}")

def create_post():
    """Create a new post using a POST request."""
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "My New Post",
        "body": "This is the content of my new post.",
        "userId": 1
    }
    try:
        response = requests.post(url, json=payload)
        print(f"\nPOST Request to {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers['content-type']}")
        if response.status_code == 201:
            post = response.json()
            print(f"Created Post: {post}")
        else:
            print(f"Error: {response.text}")
    except requests.RequestException as e:
        print(f"POST Request failed: {e}")

def update_post(post_id):
    """Update an existing post using a PUT request."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    payload = {
        "id": post_id,
        "title": "Updated Post Title",
        "body": "This is the updated content.",
        "userId": 1
    }
    try:
        response = requests.put(url, json=payload)
        print(f"\nPUT Request to {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers['content-type']}")
        if response.status_code == 200:
            post = response.json()
            print(f"Updated Post: {post}")
        else:
            print(f"Error: {response.text}")
    except requests.RequestException as e:
        print(f"PUT Request failed: {e}")

def delete_post(post_id):
    """Delete a post using a DELETE request."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.delete(url)
        print(f"\nDELETE Request to {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers['content-type']}")
        if response.status_code == 200:
            print("Post deleted successfully (no content returned).")
        else:
            print(f"Error: {response.text}")
    except requests.RequestException as e:
        print(f"DELETE Request failed: {e}")

def main():
    """Run all example requests."""
    print("=== Requests Library Practice Script ===")
    get_posts()
    create_post()
    update_post(1)
    delete_post(1)

if __name__ == "__main__":
    main()
