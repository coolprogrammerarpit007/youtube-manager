import json
import sys


# method to display all videos

def display_favourite_videos(videos):
    print("********************************")
    print("Displaying all the your favourite videos.")
    list_all_videos(videos)
    print("**********************************")
    print()
    print()

def save_video_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)  # write the data into file

def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)  # will automatically fetches data from from file and converts into json

    except FileNotFoundError:
        return []
    except FileExistsError:
        print("No Data in File: ")
        return []
    except Exception:
        print("Exception captured!")
        return []
    
def list_all_videos(videos):
    if not videos:
        print("No Videos Found!")
        return
    for index,video in enumerate(videos,start=1):
        print(f"Video Number {index} : Video Name: {video["name"]} : Video Time: {video["time"]}")

def add_video(videos):
    video_name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({
        "name":video_name,
        "time":time
    })
    save_video_helper(videos)

def update_video(videos):
    display_favourite_videos(videos)
    video_number = int(input("Enter Video Number which you want to update: "))
    video_number = video_number - 1
    if 0 <= video_number < len(videos):
        video_name = input("Enter New Video Name: ")
        time = input("Enter New Video Time: ")
        videos[video_number] = {
            "name":video_name,
            "time":time
        }
        save_video_helper(videos)
    else:
        print("Video Not Found!")

def delete_video(videos):
    display_favourite_videos(videos)
    ans = input("Are you sure you want to delete a video. (y/n) ").lower()
    if ans == "y":
        video_number = int(input("Enter video number you wanted to deleted: "))
        video_number = video_number - 1
        if 0 <= video_number < len(videos):
            videos.pop(video_number)
            print("Your video has been deleted sucessfully! ")
        else:
            print("Video does not exist! ")
    else:
        return 

def main():
    # Load data from file
    videos = load_data()
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
                add_video(videos)

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


    # enumerate helps in addng indexes to the Itterables.