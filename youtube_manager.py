def list_all_videos(videos):
    pass

def add_video(video):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = []
    while True:
        print("\n Youtube Manager | choose your choice ")
        print("1. List all favourite videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video Details ")
        print("4. Delete a youtube video ")
        print("5. Exit Application ")

        choice = input("Enter your choice: ")

        match(choice):
            case "1":
                print("\n List of all favourite videos ")
                list_all_videos(videos)

            case "2":
                print("\n youtube video has been added sucessfully. ")
                add_video(video)

            case "3":
                print("\n Updated youtube video Details ")
                update_video(videos)
            case "4":
                print("\n Updated youtube video Details ")
                delete_video(videos)
            case "5":
                print("\n Application Exit ")
                break
            case _:
                print("\nInvalid choice ")
                break

if __name__ == "__main__":
    main()