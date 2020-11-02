
class Cinema():
    
    @property
    def chairs_num(self):
        return self.__chairs_num
    
    @chairs_num.setter
    def chairs_num(self,num):
        self.__chairs_num=num if(num>0) else 0 

    @property
    def open_hour(self):
        return self.__open_hour
    
    @open_hour.setter
    def open_hour(self,hour):
        self.__open_hour=hour if(hour>=6 and hour<=12) else 6

    @property
    def close_hour(self):
        return self.__close_hour
    
    @close_hour.setter
    def close_hour(self,hour):
        self.__close_hour=hour if(hour>=18 and hour<=23) else 18

c1=Cinema

    

