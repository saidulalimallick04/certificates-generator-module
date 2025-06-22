from utils.certificates_generator import generate_certificate as gc
def main():
    print("Hello from certificates-generator-module!")
    # title = input("Enter Title of Certificate: ")
    title = "The Shadow Monark"

    # organization = input("Organization Name: ")
    organization = "The Apex Devs"

    # username = input("Enter Name: ")
    username = "Saidul Ali Mallick"

    # role = input("Enter Role of Labled Person: ")
    role = "The Head of Apex Devs"

    # head_name = input("Name of the Labeled Person: ")
    head_name = "Supriya Khanra"
    
    gc(title,organization,username,role,head_name)

if __name__ == "__main__":
    main()
