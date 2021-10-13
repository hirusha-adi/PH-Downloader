import os
import platform
from phlib import PornHub



def clear_screen():
    if platform.system().lower().startswith('win'):
        os.system("cls")
    else:
        os.system("clear")


def show_logo(clrs: bool = True):
    if clrs:
        clear_screen()
    print("""
 _            _   
| |_ ___  ___| |_ 
| __/ _ \/ __| __|
| ||  __/\__ \ |_ 
 \__\___||___/\__|
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



if __name__ == "__main__":
    ENTIRE_PROGRAM()
