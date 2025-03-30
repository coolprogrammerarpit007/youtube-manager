import sqlite3

from youtube_manager import add_video

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute('''
        SELECT * FROM videos
    ''')
    for row in cursor.fetchall():
        print(row)


def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()



def update_video(id,name,time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(name,time,id))
    conn.commit()



def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit Application")

        choice = input("Enter your choice: ")

        match(choice):
            case "1":
                print("\n These are your favourite videos: ")
                list_videos()
            case "2":
                print("\n Add your favourite video: ")
                video_name = input("Enter the video name: ")
                video_time = input("Enter the video time: ")
                add_video(video_name,video_time)
            case "3":
                print("\n Update your video details:  ")
                video_id = input("Enter video id: ")
                video_name = input("Enter the video name: ")
                video_time = input("Enter the video time: ")
                update_video(video_id,video_name, video_time)
            case "4":
                print("\n Delete your video: ")
                video_id = input("Enter video id: ")
                delete_video(video_id)
            case "5":
                print("Come use again, sometime!!")
                break
            case _:
                print("Invalid User Choice:")

    conn.close()






if __name__ == "__main__":
    main()