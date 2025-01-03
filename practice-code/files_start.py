def main():
    # 
    
    myfile = open("textfile.txt", "r")
    
    for i in range(10):
        myfile.write("This is some text\n")
        
    myfile.close()