import csv

# Global lists to store user and post data
users = []
posts = []

# Function to load user information from file
def load_user_data(file_path):
    # Open the CSV file containing user data
    with open(file_path, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file, delimiter=';')
       
        for line in reader:
            
            username, display_name, state, friends_str = line
           
            friends = friends_str.strip('[]').split(', ')
            # Add user data to the global users list
            users.append({'username': username, 'display_name': display_name, 'state': state, 'friends': friends})

# Function to load post information from file
def load_post_data(file_path):
   
    with open(file_path, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file, delimiter=';')
       
        for line in reader:
            # Extract post information from the line
            post_id, user_id, visibility = line
            # Add post data to the global posts list
            posts.append({'post_id': post_id, 'user_id': user_id, 'visibility': visibility})

# Function to check visibility of a post
def check_visibility(post_id, username):
    # Find the post with the given post_id
    post = next((p for p in posts if p['post_id'] == post_id), None)
    # If post not found, print an error message
    if post is None:
        print('Post not found.')
        return
    # If the post is public, access is permitted
    if post['visibility'] == 'public':
        print('Access Permitted')
    else:
        # Find the user with the given username
        user = next((u for u in users if u['username'] == username), None)
        # If user not found, print an error message
        if user is None:
            print('User not found.')
            return
        # If the user is friends with the post owner, access is permitted
        if post['user_id'] in user['friends']:
            print('Access Permitted')
        else:
            # Otherwise, access is denied
            print('Access Denied')

# Function to retrieve posts accessible to a user
def retrieve_posts(username):
    # Find the user with the given username
    user = next((u for u in users if u['username'] == username), None)
    # If user not found, print an error message
    if user is None:
        print('User not found.')
        return
    # Filter posts based on visibility and friendship, and print accessible posts
    accessible_posts = [post['post_id'] for post in posts if post['user_id'] != username and (post['visibility'] == 'public' or post['user_id'] in user['friends'])]
    print('Accessible posts:')
    print('\n'.join(accessible_posts))

# Function to search users by location
def search_users_by_location(state):
    # Find users in the given state and print their display names
    matching_users = [user['display_name'] for user in users if user['state'] == state]
    if matching_users:
        print('Users in {}:'.format(state))
        print('\n'.join(matching_users))
    else:
        print('No users found in {}.'.format(state))

# Main menu function to interact with the user
def menu():
    print('1. Load input data')
    print('2. Check visibility')
    print('3. Retrieve posts')
    print('4. Search users by location')
    print('5. Exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        # Prompt user for file paths and load data
        user_data_file = input('Enter path to user data file: ')
        post_data_file = input('Enter path to post data file: ')
        load_user_data(user_data_file)
        load_post_data(post_data_file)
        print('Data loaded successfully.')
    elif choice == '2':
        # Prompt user for post ID and username, then check visibility
        post_id = input('Enter post ID: ')
        username = input('Enter username: ')
        check_visibility(post_id, username)
    elif choice == '3':
        # Prompt user for username and retrieve accessible posts
        username = input('Enter username: ')
        retrieve_posts(username)
    elif choice == '4':
        # Prompt user for state and search users by location
        state = input('Enter state: ')
        search_users_by_location(state)
    elif choice == '5':
        # Exit the program
        exit(0)
    else:
        # Invalid choice, prompt user to enter a valid option
        print('Invalid choice. Please enter a valid option.')


while True:
    menu()
