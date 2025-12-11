# File Extensions: Implement a program that prompts the user for the name of a
#                  file and then outputs that file's media type if the file
#                  name ends, case-insensitively, in any of the suffixes:
#                  [.gif, .jpg, .jpeg, .png, .pdf, .txt, .zip]
#                  Otherwise, output `application/octet-stream`


def main():
    print(media_type(input("File name: ").strip().lower()))

def media_type(file):
    match file.split('.')[1]:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"

    return "application/octet-stream"


main()
