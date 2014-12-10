# author : Akshay Vilekar
# Download all the issues of ubuntu magzines automatically

import urllib
import requests


def download(url, name, count):

    # info about file
    print "We are about to download " + "magzine number " + count
    size = requests.head(url).headers.get('content-length', None)
    # size in Megabytes
    size = str(round((int(size) / 1024.0 / 1024.0), 2))
    print " Size of " + count + " issue is " + size + " MB "

    # ask for confirmation
    choice = raw_input("Should I download " + count + " issue\n")
    if choice == "n":
        return "Cannot download " + name

    else:
        # print message
        print "Downloading file " + count
        
        # open file
        file_name = open(name, "wb")

        # download file
        temp_file = urllib.urlopen(url)

        # write content to file
        file_name.write(temp_file.read())

        # close them
        file_name.close()
        temp_file.close()

        # show message to user
        return "Completed Downloading file " + count

# end


def main():
    for i in range(1, 92):
        url = "http://dl.fullcirclemagazine.org/issue" + str(i) + "_en.pdf"
        name = "issue" + str(i) + "en.pdf"
        print download(url, name, str(i))

# end

if __name__ == "__main__":
    main()
