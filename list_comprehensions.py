def run():
    my_list = [0,1,2,3,4,5,6,7,8,9]
    my_list1 = [i for i in my_list if i%2 == 0]
    print(my_list1)
    

if __name__=='__main__':
    run()