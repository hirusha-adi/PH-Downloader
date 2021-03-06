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


def DOWNLOAD_PH_VID(dlqualty: str = None, mass: bool = False):
    ph = PornHub()
    search_for = input("? What to search: ")

    if mass:
        search_amout = int(input("? How many: "))
        ph_results = ph.search(search_for, max=search_amout)
    else:
        ph_results = ph.search(search_for, max=1)

    for ph_result in ph_results:
        print("")
        print(f"---------------\n{ph_result.title}\n+ URL: {ph_result.url}\n+ Category: {ph_result.category}")
        print(f"+ View Count: {ph_result.meta['count']}\n+ Like Percentage: {ph_result.meta['percent']}%\n+ Categories:")
        
        for category in ph_result.meta['category_names']:
            print(category, end=", ")
        
        print("")
        print("! Downloading video...")

        if dlqualty == "max":
            ph_result.download()
        elif dlqualty == "720p":
            ph_result.download_720p()
        elif dlqualty == "480p":
            ph_result.download_480p()
        elif dlqualty == "360p":
            ph_result.download_360p()
        else:
            print("- Invalid quality selected!")
            qerror = True

        if not qerror:
            print("+ Download complete!")


def OTHER_2(action: str = None):
    ph = PornHub()
    if action == "list":
        for i in ph.categories:
                print(i.title)
    
    elif action == "search_by_name":
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


def ENTIRE_PROGRAM():
    clear_screen()
    show_logo()
    print("""
    [1] List categories 
    [2] Search by word
    [3] Download
    """)

    main_menu_opt = input("? Select an option: ")

    if main_menu_opt == "1":
        show_logo()
        OTHER_2("list")
        
    
    if main_menu_opt == "2":
        show_logo()
        OTHER_2("search_by_name")
        
    
    if main_menu_opt == "3":
        show_logo()
        print("""
    [1] Highest QUality
    [2] 720p
    [3] 480p
    [4] 360p
        """)

        quality_menu = input("? Select a quality: ")
        if quality_menu == "1":
            show_logo()
            print("""
+ Selected Quality: Highest Available
    [1] Mass Download
    [2] Search and Download
            """)
            highest_qm = input("? Select an option: ")
            
            # Mass Downloader
            if highest_qm == "1":
                show_logo()
                DOWNLOAD_PH_VID(dlqualty="max", mass=True)
    
            # Search and Download
            if highest_qm == "2":
                show_logo()
                DOWNLOAD_PH_VID(dlqualty="max")


        if quality_menu == "2":
            show_logo()
            print("""
+ Selected Quality: 720p
    [1] Mass Download
    [2] Search and Download
            """)
            p720_qm = input("? Select an option: ")
            
            # Mass Downloader (720p)
            if p720_qm == "1":
                show_logo()
                DOWNLOAD_PH_VID(dlqualty="720p", mass=True)

            # Search and Download (720p)
            if p720_qm == "2":
                show_logo()
                DOWNLOAD_PH_VID(dlqualty="720p")


        if quality_menu == "3":
            print("""
+ Selected Quality: 480p
    [1] Mass Download
    [2] Search and Download
            """)
            p480p_qm = input("? Select an option: ")
            
            # Mass Downloader (480p)
            if p480p_qm == "1":
                show_logo()
                DOWNLOAD_PH_VID(dlqualty="480p", mass=True)

            # Search and Download (480p)
            if p480p_qm == "2":
                show_logo()
                DOWNLOAD_PH_VID(dlqualty="480p")


        if quality_menu == "4":
            print("""
+ Selected Quality: 360p
    [1] Mass Download
    [2] Search and Download
            """)
            p480p_qm = input("? Select an option: ")

            # Mass Downloader (360p)
            if main_menu_opt == "1":
                show_logo()
                DOWNLOAD_PH_VID(dlqualty="360p", mass=True)

            # Search and Download (360p)
            if main_menu_opt == "2":
                show_logo()
                DOWNLOAD_PH_VID(dlqualty="360p")



if __name__ == "__main__":
    
    try:
        ENTIRE_PROGRAM()
    except Exception as e:
        print("Error", e)
    finally:
        print("HAVE A NICE DAY!")
