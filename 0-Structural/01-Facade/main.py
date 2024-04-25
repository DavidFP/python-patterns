from carFacade import CarFacade

if __name__=="__main__":
    car_facade = CarFacade()
    print("Actions: \n 1-Start \n 2-Stop \n 0-Exit")
    action = -1
    while action!="0":
        action = input("Input action \t")
        if action ==1 or action=="1":
            car_facade.start_car()
        if action==2  or action =="2":
            car_facade.stop_car()