# Import your API file (socialapi.py)
import socialapi

# This is an endless loop. It will only end if you use the `break` keyword
while True:
    # Prompt the user with options
    print("\nWhat would you like to do? Type a number and press Enter.")
    print("\t1) Get all posts")
    print("\t2) Get one post")
    print("\t3) Save a post")
    print("\t4) Delete a post")
    print("\t5) Quit the program")
    
    # Get input from the user
    response = input()
    
    # Check to make sure the input is valid
    if response != "1" and response != "2" and response != "3" and response != "4" and response != "5":
        print("That is an invalid response. Please try again.\n")
        continue
        
    # Perform an action based on the user's input
    response = int(response)
    if response == 1:
        posts = socialapi.get_all_posts()
        for name, content in posts.items():
            print("Name:", name, "\nContent:", content)
        continue
    elif response == 2:
        name = input("\nEnter the name of the post you are looking for: ")
        post = socialapi.get_one_post(name)
        if post == False:
            print("That post couldn't be found!")
        else:
            print("Name:", post[0], "\nContent:", post[1])
        continue
    elif response == 3:
        name = input("\nEnter the name you want to give your post: ")
        content = input("Enter the content you want your post to contain: ") 
        socialapi.save_post(name, content)
        print("Saved!")
        continue
    elif response == 4:
        name = input("\nEnter the name of the post you want to delete: ")
        success = socialapi.delete_post(name)
        if success == False:
            print("That post couldn't be found!")
        else:
            print("Deleted!")
        continue
    else:
        print("Goodbye!\n")
        break # End the loop
        
    
