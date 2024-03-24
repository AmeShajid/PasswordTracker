#This is basically a password Manager where you can store all your passwords onto a text file, but the difference is ours will store our passwords then
# it will encrypt them into something else, then you need a big password to see all your passwords



from cryptography.fernet import Fernet #this is a module and this lets us encrypt text
# you have to pip install this btw
#this takes a string and makes it into random text and to make it normal you have to use your very own key
#key + password + text to encrypt = random text
#random text + key + password = text to encrypt
#this is an explanation of what is happening / will happen


def write_key():# this function is for creating a key 
    key = Fernet.generate_key()#this will generate a random key using the fernet module
    with open("key.key", "wb") as key_file:#this will open a key.key file in wb which is writing in byes as a new file named key_file
        key_file.write(key)#in our keyfile file it will write our key and put it inside that file
write_key()


def load_key():#this is how we get out key
    file = open("key.key", "rb")# we are opening this in read bytes mode then we will 
    key = file.read()# we will read the entire file
    file.close()# we will close the file cause always close it 
    return key# then we will finally get our key back


# right here now we have our very own special key which we need 
key = load_key()#this is under becasue it has to be under the funciton so it works
#we have encode because this is a diff way to store information and our key is in bytes so our master password has to be in bytes too and then they will both be our actual key
fer = Fernet(key)#this is for initilazing this encryption module


def view():# we will use a function because it makes things alot easier and we can call the fucntion into our if else block 
    with open("password.txt", "r") as f:#so if we want to view our passwords we will open our textfile and then our mode is read so we will read instead of append and obvy open the file instead of named password txt its just f
        for line in f.readlines():#then for all the lines in our txt file we will read the lines 
            data = line.rstrip()#gets rid of all the extra spaces after the password
            # we made it data because we want to split the data now 
            user, passw = data.split("|")#what this part does is everytime it sees this | it will take each string between the | and make it into a list and you have to access with index
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())# this is the format now
            # what print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode()) is first it takes the string in then it coverts into bytes then it will decode that byte string


def add(): # we will use a function because it makes things alot easier and we can call the function into our if else block
    #after we press add we will need the account name they want it in and that includes password too
    name = input("Account Name: ")
    pwd = input("Password: ")
    # after we have our account and password then we will go into our textfile that stores everything 
    with open("password.txt", "a") as f:#we will open our passwords txt and append to it so after pressing add we will add to our text file
        #we are opening it as f so passwords txt becomes named f 
        f.write(name + "| " + fer.encrypt(pwd.encode()).decode() + "\n") #what this part does is it will now write into our new text file and have it in that format it will have name then seperated then password and then a new line
        # we have fer.encrypt(password.encode().decode()) because it takes a bytes of string then decode it into a regular string


while True:#we have a while loop so they can continously do this until they decide to quit out or stop
    mode = input("Would you like to add a new password or view existing ones, press q to quit(view, add, q): ").lower()#add the .lower here so its easy to keep track of inputs
    #if else statements for the 2 possible inputs 
    if mode == "q":# check for this part case
        break#break because if they want to quit it it stops the program
    #we can start another if else block cause the first one breaks elif we can do but do if else cause why not
    if mode == "view": #call fucntion view
        view()
    elif mode == "add":  #call function add
        add()
    else: # if they type in anything else besides q view and add then it will be invallid
        print("Invalid mode.")
        continue#we have this so in case they have an invalid input it doesn't stop and goes back to the top





#your password txt file will create itself and your account with crypted password will be on it, in the terminal your actual password and account will show