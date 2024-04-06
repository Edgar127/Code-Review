# Code-Review
 Assignment 2 - Code Review
Test Case 1: Load Input Data
Objective: Validate that user and post data are correctly loaded from files.
Input: User selects option 1.
User inputs user-info.txt and post-info.txt filenames when prompted.
Expected Output: The program should confirm "Data loaded successfully."
Test Case 2: Check Visibility (Access Permitted)
Objective: Check if a user can access a friend's post.
Prerequisite: Data must be loaded successfully.
Input: User selects option 2.
User enters post ID: post1112.
User enters username: whiskerwatcher.
Expected Output: "Access Permitted", since whiskerwatcher is a friend of goldenlover1 (the creator of post1112).
Test Case 3: Check Visibility (Access Denied)
Objective: Check if a user cannot access a non-friend's post marked as "friend".
Prerequisite: Data must be loaded successfully.
Input: User selects option 2.
User enters post ID: post2123.
User enters username: petpal4ever.
Expected Output: "Access Denied", since petpal4ever is not a friend of whiskerwatcher (the creator of post2123).
Test Case 4: Retrieve Posts Including User's Own Post
Objective: Retrieve all accessible posts for a user, including their own.
Prerequisite: Data must be loaded successfully.
Input: User selects option 3.
User enters username: whiskerwatcher.
Expected Output: "Accessible posts: post1112, post2123, post3298". This assumes the retrieve_posts method has been adjusted to include the user's own posts as well.
Test Case 5: Search Users by Location
Objective: Find all users in a specified state.
Prerequisite: Data must be loaded successfully.
Input:User selects option 4.
User enters state location: CA.
Expected Output: "Users in CA: Jane Doe", indicating that Jane Doe (goldenlover1) is the user located in California.
