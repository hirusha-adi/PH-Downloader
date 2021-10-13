import os
import platform
from PHbackend import PornHub
try:
    import youtube_dl
except:
    if platform.system().lower().startswith('win'):
        os.system("pip install youtube-dl")
    else:
        os.system("pip3 install youtube-dl")


def clear_screen():
    if platform.system().lower().startswith('win'):
        os.system("cls")
    else:
        os.system("clear")


def show_logo(clrs: bool = True):
    if clrs:
        clear_screen()
    print("""
     ____  _   _     _ _ 
    |  _ \| | | | __| | |
    | |_) | |_| |/ _` | |
    |  __/|  _  | (_| | |
    |_|   |_| |_|\__,_|_|

  PORN HUB DOWNLOADER v0.1
    """)


def ENTIRE_PROGRAM():
    # Creating the object
    print("+ Creating object")
    ph = PornHub()
    print("+ Completed!")

    clear_screen()

    # Home screen
    show_logo()
    print("""
    [1] List categories 
    [2] Search by word

    [3] Mass Download
    [4] Search and Download

    [5] Mass Download (720p)
    [6] Search and Download (720p)

    [7] Mass Download (480p)
    [8] Search and Download (480p)

    [9] Mass Download (360p)
    [10] Search and Download (360p)
    """)

    main_menu_opt = input("? Select an option: ")

    # List Categories
    if main_menu_opt == "1":
        for i in ph.categories:
            print(i.title)
    
    # Search videos by word
    if main_menu_opt == "2":
        search_for = input("? What to search: ")
        search_amout = int(input("? How many: "))
        ph_results = ph.search(search_for, max=search_amout)
        for ph_result in ph_results:
            print("")
            print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
            print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
            for category in ph_result.meta['category_names']:
                print(category, end=", ")
            print("")

    # Mass Downloader
    if main_menu_opt == "3":
        search_for = input("? What to search: ")
        search_amout = int(input("? How many: "))
        ph_results = ph.search(search_for, max=search_amout)
        for ph_result in ph_results:
            print("")
            print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
            print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
            for category in ph_result.meta['category_names']:
                print(category, end=", ")
            print("")
            print("! Downloading video...")
            ph_result.download()
            print("+ Download complete!")
    
    # Search and Download
    if main_menu_opt == "4":
        search_for = input("? What to search: ")
        ph_results = ph.search(search_for, max=1)
        for ph_result in ph_results:
            print("")
            print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
            print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
            for category in ph_result.meta['category_names']:
                print(category, end=", ")
            print("")
            print("! Downloading video...")
            ph_result.download()
            print("+ Download complete!")

    # Mass Downloader (720p)
    if main_menu_opt == "5":
        search_for = input("? What to search: ")
        search_amout = int(input("? How many: "))
        ph_results = ph.search(search_for, max=search_amout)
        for ph_result in ph_results:
            print("")
            print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
            print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
            for category in ph_result.meta['category_names']:
                print(category, end=", ")
            print("")
            print("! Downloading video...")
            ph_result.download_720p()
            print("+ Download complete!")

    # Search and Download (720p)
    if main_menu_opt == "6":
        search_for = input("? What to search: ")
        ph_results = ph.search(search_for, max=1)
        for ph_result in ph_results:
            print("")
            print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
            print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
            for category in ph_result.meta['category_names']:
                print(category, end=", ")
            print("")
            print("! Downloading video...")
            ph_result.download_720p()
            print("+ Download complete!")
    
    # Mass Downloader (480p)
    if main_menu_opt == "7":
        search_for = input("? What to search: ")
        search_amout = int(input("? How many: "))
        ph_results = ph.search(search_for, max=search_amout)
        for ph_result in ph_results:
            print("")
            print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
            print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
            for category in ph_result.meta['category_names']:
                print(category, end=", ")
            print("")
            print("! Downloading video...")
            ph_result.download_480p()
            print("+ Download complete!")

    # Search and Download (480p)
    if main_menu_opt == "8":
        search_for = input("? What to search: ")
        ph_results = ph.search(search_for, max=1)
        for ph_result in ph_results:
            print("")
            print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
            print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
            for category in ph_result.meta['category_names']:
                print(category, end=", ")
            print("")
            print("! Downloading video...")
            ph_result.download_480p()
            print("+ Download complete!")
    
    # Mass Downloader (360p)
    if main_menu_opt == "9":
        search_for = input("? What to search: ")
        search_amout = int(input("? How many: "))
        ph_results = ph.search(search_for, max=search_amout)
        for ph_result in ph_results:
            print("")
            print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
            print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
            for category in ph_result.meta['category_names']:
                print(category, end=", ")
            print("")
            print("! Downloading video...")
            ph_result.download_360p()
            print("+ Download complete!")

    # Search and Download (360p)
    if main_menu_opt == "10":
        search_for = input("? What to search: ")
        ph_results = ph.search(search_for, max=1)
        for ph_result in ph_results:
            print("")
            print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
            print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
            for category in ph_result.meta['category_names']:
                print(category, end=", ")
            print("")
            print("! Downloading video...")
            ph_result.download_360p()
            print("+ Download complete!")






if __name__ == "__main__":
    try:
        ENTIRE_PROGRAM()
    except Exception as e:
        print("Error", e)
    finally:
        print("HAVE A NICE DAY!")
