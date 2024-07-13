#!/usr/bin/env python
# coding: utf-8

# In[83]:


import mysql.connector ##################################################
mydb = mysql.connector.connect(
    host = "sql8.freemysqlhosting.net" ,
    user = "sql8612734",
    password = "5SNNKsbblH",
    database = "sql8612734"

)


import tkinter
from tkinter import *
from tkinter.ttk import *


#function to create a new window for regestering a new user --> 1
def openNewWindow1():
   ############################################
    def printValue():
        username = username_Entry.get()
        email = email_Entry.get()
        age = gender_Entry.get()
        gender = gender_Entry.get()
        birthday = birthday_Entry.get()
        
        import mysql.connector
        mycursor = mydb.cursor()


        sql = """
        INSERT INTO APP_user 
        VALUES (%s,%s,%s,%s,%s)
        """

        val = (username, email, age, gender,birthday)
        mycursor.execute(sql,val)

        mydb.commit()
       
    ############################################
    newWindow1 = Toplevel()
 
    newWindow1.title("Register a user")
 
    newWindow1.geometry("500x300")
 
    # A Label widget to show in toplevel
    Label(newWindow1, text ="Enter your Information", font = ('Times New Roman',17,'bold') ).pack()
    
    #taking info from user
    Label(newWindow1, text ="Username:").pack()
    username_Entry= Entry(newWindow1, width= 40)
    username_Entry.focus_set()
    username_Entry.pack()
    
    Label(newWindow1, text ="Email:").pack()
    email_Entry= Entry(newWindow1, width= 40)
    email_Entry.focus_set()
    email_Entry.pack()
    
    Label(newWindow1, text ="Age:").pack()
    age_Entry= Entry(newWindow1, width= 40)
    age_Entry.focus_set()
    age_Entry.pack()
    
    Label(newWindow1, text ="Gender (M:Male / F:Female) :").pack()
    gender_Entry= Entry(newWindow1, width= 40)
    gender_Entry.focus_set()
    gender_Entry.pack()
    
    Label(newWindow1, text ="Birthday (YYYY-MM-DD) :").pack()
    birthday_Entry= Entry(newWindow1, width= 40)
    birthday_Entry.focus_set()
    birthday_Entry.pack()
    
    SubmitButton1 = Button(newWindow1, text = 'Submit', width = 50, command=printValue).pack()

#function to create a new ad --> 2
def openNewWindow2():
    ############################################
    def printValue2():
        
        AD_ID= ID_Entry.get() ; price= price_Entry.get() ; brand= brand_Entry.get() ; model= model_Entry.get() ; 
        fuel_type= fuel_type_Entry.get() ; payment_Options= payment_Entry.get() ;transmission_type= transmission_Entry.get() ;
        color= color_Entry.get() ; body_type= body_type_Entry.get() ; upper_engine_capacity= upper_engine_Entry.get() ; 
        lower_engine_capacity= lower_engine_Entry.get() ; lower_KM= lower_KM_Entry.get() ; upper_KM= upper_KM_Entry.get() ;
        AD_Year= year_Entry.get(); location= location_Entry.get(); description = description_Entry.get();
        seller_account_link= seller_account_link_Entry.get() ;
        
        
        import mysql.connector
        mycursor = mydb.cursor()

        sql = """
        INSERT INTO Car (AD_ID, price, brand, model, fuel_type, payment_Options, transmission_type, color, body_type, 
        upper_engine_capacity, lower_engine_capacity, lower_KM, upper_KM, AD_Year, location, car_Description, seller_account_link)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
       
        
        
        val = (AD_ID, price, brand, model, fuel_type, payment_Options, transmission_type, color, body_type, 
        upper_engine_capacity, lower_engine_capacity, lower_KM, upper_KM, AD_Year, location,description, seller_account_link)
        mycursor.execute(sql,val)

        mydb.commit()
    ############################################
       
    newWindow2 = Toplevel(master)
 
    newWindow2.title("Create a new car ad")
 
    newWindow2.geometry("700x800")
 
    # A Label widget to show in toplevel
    Label(newWindow2, text ="Enter car Information", font = ('Times New Roman',17,'bold') ).pack()
    
    #taking info from user
    Label(newWindow2, text ="AD ID:").pack()
    ID_Entry= Entry(newWindow2, width= 40)
    ID_Entry.focus_set()
    ID_Entry.pack()
    
    Label(newWindow2, text ="Price:").pack()
    price_Entry= Entry(newWindow2, width= 40)
    price_Entry.focus_set()
    price_Entry.pack()
    
    Label(newWindow2, text ="Brand:").pack()
    brand_Entry= Entry(newWindow2, width= 40)
    brand_Entry.focus_set()
    brand_Entry.pack()
    
    Label(newWindow2, text ="Model:").pack()
    model_Entry= Entry(newWindow2, width= 40)
    model_Entry.focus_set()
    model_Entry.pack()
    
    Label(newWindow2, text ="Fuel Type:").pack()
    fuel_type_Entry= Entry(newWindow2, width= 40)
    fuel_type_Entry.focus_set()
    fuel_type_Entry.pack()
    
    Label(newWindow2, text ="Payment Options:").pack()
    payment_Entry= Entry(newWindow2, width= 40)
    payment_Entry.focus_set()
    payment_Entry.pack()
    
    Label(newWindow2, text ="Transmission Type:").pack()
    transmission_Entry= Entry(newWindow2, width= 40)
    transmission_Entry.focus_set()
    transmission_Entry.pack()
    
    Label(newWindow2, text ="Color:").pack()
    color_Entry= Entry(newWindow2, width= 40)
    color_Entry.focus_set()
    color_Entry.pack()
    
    Label(newWindow2, text ="Body Type:").pack()
    body_type_Entry= Entry(newWindow2, width= 40)
    body_type_Entry.focus_set()
    body_type_Entry.pack()
    
    Label(newWindow2, text ="Upper Engine Capacity:").pack()
    upper_engine_Entry= Entry(newWindow2, width= 40)
    upper_engine_Entry.focus_set()
    upper_engine_Entry.pack()
    
    Label(newWindow2, text ="Lower Engine Capacity:").pack()
    lower_engine_Entry= Entry(newWindow2, width= 40)
    lower_engine_Entry.focus_set()
    lower_engine_Entry.pack()
    
    Label(newWindow2, text ="Lower KM:").pack()
    lower_KM_Entry= Entry(newWindow2, width= 40)
    lower_KM_Entry.focus_set()
    lower_KM_Entry.pack()
    
    Label(newWindow2, text ="Upper KM:").pack()
    upper_KM_Entry= Entry(newWindow2, width= 40)
    upper_KM_Entry.focus_set()
    upper_KM_Entry.pack()
    
    Label(newWindow2, text ="Year:").pack()
    year_Entry= Entry(newWindow2, width= 40)
    year_Entry.focus_set()
    year_Entry.pack()
    
    Label(newWindow2, text ="Location:").pack()
    location_Entry= Entry(newWindow2, width= 40)
    location_Entry.focus_set()
    location_Entry.pack()
    
    Label(newWindow2, text ="Car Description:").pack()
    description_Entry= Entry(newWindow2, width= 40)
    description_Entry.focus_set()
    description_Entry.pack()
    
    Label(newWindow2, text ="Seller Account Link:").pack()
    seller_account_link_Entry= Entry(newWindow2, width= 40)
    seller_account_link_Entry.focus_set()
    seller_account_link_Entry.pack()
    

    
    SubmitButton2 = Button(newWindow2, text = 'Submit', width = 50, command=printValue2).pack()
   
    
#function to View existing reviews of a given ad --> 3
def openNewWindow3():
    ############################################
    def printValue3():
        wanted_id = reviewEntry.get()
        import mysql.connector
        mycursor = mydb.cursor()
        
      
        sql = """
        SELECT review FROM Car WHERE AD_ID = %s 
        """ 
        mycursor.execute(sql, (wanted_id,))
        
        results = mycursor.fetchone()
        if results[0] != None:
            Label(newWindow3, text = 'Review: ').pack()
            Label(newWindow3, text = results[0]).pack()
        else:
            Label(newWindow3, text = 'No reviews available').pack()

        
    ############################################
       
    newWindow3 = Toplevel(master)
 
    newWindow3.title("View existing reviews of a given ad")
 
    newWindow3.geometry("500x300")
 
    # A Label widget to show in toplevel
    Label(newWindow3, text ="Enter car ID to view reviews", font = ('Times New Roman',17,'bold') ).pack()
    
    #taking info from user
    reviewEntry= Entry(newWindow3, width= 40)
    reviewEntry.focus_set()
    reviewEntry.pack()
    
    SubmitButton3 = Button(newWindow3, text = 'Submit', width = 50, command=printValue3).pack()

#function to View AVG rating of a given seller --> 4
def openNewWindow4():
    ############################################
    def printValue4():
        wanted_seller = wanted_seller_entry.get()
        import mysql.connector
        mycursor = mydb.cursor()
        
      
        sql = """
        select avg(rating) from Car where seller_account_link = %s AND rating is not null 
        """ 
        mycursor.execute(sql, (wanted_seller,))
        
        results = mycursor.fetchone()
        if results[0] != None:
            Label(newWindow4, text = 'Rating: ').pack()
            Label(newWindow4, text = results[0]).pack()
        else:
            Label(newWindow4, text = 'No ratings available').pack()

        
    ############################################
       
    newWindow4 = Toplevel(master)
 
    newWindow4.title("View AVG rating of a given seller")
 
    newWindow4.geometry("500x300")
 
    # A Label widget to show in toplevel
    Label(newWindow4, text ="Enter seller account link", font = ('Times New Roman',17,'bold') ).pack()
    
    #taking info from user
    wanted_seller_entry= Entry(newWindow4, width= 40)
    wanted_seller_entry.focus_set()
    wanted_seller_entry.pack()
    
    SubmitButton4 = Button(newWindow4, text = 'Submit', width = 50, command=printValue4).pack()
    

#function to Show all the ads for a given car make --> 5
def openNewWindow5():
    ############################################
    def printValue5():
    
        brand = brand_Entry.get() ; body_type = body_type_Entry.get() ; AD_Year = year_Entry.get() ; location = location_Entry.get();
        
        import mysql.connector
        mycursor = mydb.cursor()

        sql = """
        select *, AVG(price), COUNT(price) from Car where brand = %s 
        AND body_type = %s AND AD_Year = %s AND location = %s group by model
        """ 
        mycursor.execute(sql, (brand,body_type,AD_Year,location))

        
        results = mycursor.fetchall()
        Label(newWindow5, text = "Ads:",font = ('Times New Roman',13,'bold')).pack()
        for r in results:
            Label(newWindow5, text = "AD ID: ").pack(side=LEFT)
            Label(newWindow5, text = r[0]).pack(side=LEFT)
            Label(newWindow5, text = "  Brand: ").pack(side=LEFT)
            Label(newWindow5, text = r[2]).pack(side=LEFT)
            Label(newWindow5, text = "  Model: ").pack(side=LEFT)
            Label(newWindow5, text = r[3]).pack(side=LEFT)
            Label(newWindow5, text = "  Average price: ").pack(side=LEFT)
            Label(newWindow5, text = r[21]).pack(side=LEFT)
            Label(newWindow5, text = "  Count: ").pack(side=LEFT)
            Label(newWindow5, text = r[22]).pack(side=LEFT)

        
    ############################################
       
    newWindow5 = Toplevel(master)
 
    newWindow5.title("show ads for a givin brand")
 
    newWindow5.geometry("500x300")
 
    # A Label widget to show in toplevel
    Label(newWindow5, text ="Enter Car data", font = ('Times New Roman',17,'bold') ).pack()
    
    #taking info from user
    Label(newWindow5, text ="Brand:").pack()
    brand_Entry= Entry(newWindow5, width= 40)
    brand_Entry.focus_set()
    brand_Entry.pack()
    
    Label(newWindow5, text ="Body Type:").pack()
    body_type_Entry= Entry(newWindow5, width= 40)
    body_type_Entry.focus_set()
    body_type_Entry.pack()
    
    Label(newWindow5, text ="Year:").pack()
    year_Entry= Entry(newWindow5, width= 40)
    year_Entry.focus_set()
    year_Entry.pack()
    
    Label(newWindow5, text ="Location:").pack()
    location_Entry= Entry(newWindow5, width= 40)
    location_Entry.focus_set()
    location_Entry.pack()
    
    SubmitButton5 = Button(newWindow5, text = 'Submit', width = 50, command=printValue5).pack()
 
    
#function to Show all the used cars in a certain location --> 6
def openNewWindow6():
    ############################################
    def printValue6():
        
        location = location_Entry.get(); low_price = low_price_Entry.get(); high_price = up_price_Entry.get(); 
        feat = feat_Entry.get()
        
        if feat == '#':
            import mysql.connector
            mycursor = mydb.cursor()

            sql = """
            Select C.AD_ID, C.brand, C.model from Car C inner join CAR_features S ON C.AD_ID = S.AD_ID where location = %s AND (price BETWEEN %s AND %s) AND feat IS NULL
            """ 
            mycursor.execute(sql, (location,low_price,high_price))


            results = mycursor.fetchall()
            Label(newWindow6, text = "Cars:",font = ('Times New Roman',13,'bold')).pack()
            for r in results:
                Label(newWindow6, text = "AD ID: ").pack(side = LEFT)
                Label(newWindow6, text = r[0]).pack(side = LEFT)
                Label(newWindow6, text = "  Brand: ").pack(side=LEFT)
                Label(newWindow6, text = r[1]).pack(side=LEFT)
                Label(newWindow6, text = "  Model: ").pack(side=LEFT)
                Label(newWindow6, text = r[2]).pack(side=LEFT)
                
        else:
            import mysql.connector
            mycursor = mydb.cursor()

            sql = """
            Select C.AD_ID, C.brand, C.model from Car C inner join CAR_features S ON C.AD_ID = S.AD_ID where location = %s AND (price BETWEEN %s AND %s) AND feat = %s
            """ 
            mycursor.execute(sql, (location,low_price,high_price,feat))


            results = mycursor.fetchall()
            Label(newWindow6, text = "Cars:",font = ('Times New Roman',13,'bold')).pack()
            for r in results:
                Label(newWindow6, text = "AD ID: ").pack(side = LEFT)
                Label(newWindow6, text = r[0]).pack(side = LEFT)
                Label(newWindow6, text = "  Brand: ").pack(side=LEFT)
                Label(newWindow6, text = r[1]).pack(side=LEFT)
                Label(newWindow6, text = "  Model: ").pack(side=LEFT)
                Label(newWindow6, text = r[2]).pack(side=LEFT)
        
        
    ############################################
       
    newWindow6 = Toplevel(master)
 
    newWindow6.title("show top 5 areas")
 
    newWindow6.geometry("500x300")
 
    # A Label widget to show in toplevel
    Label(newWindow6, text ="Enter Car Information", font = ('Times New Roman',17,'bold') ).pack()
    
    #taking info from user
    Label(newWindow6, text ="Location:").pack()
    location_Entry= Entry(newWindow6, width= 40)
    location_Entry.focus_set()
    location_Entry.pack()
    
    Label(newWindow6, text ="Lower Price limit:").pack()
    low_price_Entry= Entry(newWindow6, width= 40)
    low_price_Entry.focus_set()
    low_price_Entry.pack()
    
    Label(newWindow6, text ="Upper Price limit:").pack()
    up_price_Entry= Entry(newWindow6, width= 40)
    up_price_Entry.focus_set()
    up_price_Entry.pack()
    
    Label(newWindow6, text ="Features (type # for no features ):").pack()
    feat_Entry= Entry(newWindow6, width= 40)
    feat_Entry.focus_set()
    feat_Entry.pack()
    
    SubmitButton6 = Button(newWindow6, text = 'Submit', width = 50, command=printValue6).pack()
    

#function to View show top 5 areas --> 7
def openNewWindow7():
    ############################################
    def printValue7():
        
        brand = brand_Entry.get() ; model = model_Entry.get() ; 
        import mysql.connector
        mycursor = mydb.cursor()

        sql = """
        select brand, model, location from Car where brand = %s And model = %s group by brand, model, location order by count(AD_ID) DESC, AVG(price) DESC LIMIT 5
        """ 
        mycursor.execute(sql, (brand,model))

        
        results = mycursor.fetchall()
        Label(newWindow7, text = "areas by order",font = ('Times New Roman',13,'bold')).pack()
        for r in results:
            Label(newWindow7, text = r[2]).pack()
        

        
    ############################################
       
    newWindow7 = Toplevel(master)
 
    newWindow7.title("show top 5 areas")
 
    newWindow7.geometry("500x300")
 
    # A Label widget to show in toplevel
    Label(newWindow7, text ="Enter Car data", font = ('Times New Roman',17,'bold') ).pack()
    Label(newWindow7, text ="enter: brand - model" ).pack()
    
    #taking info from user
    Label(newWindow7, text ="Brand:").pack()
    brand_Entry= Entry(newWindow7, width= 40)
    brand_Entry.focus_set()
    brand_Entry.pack()
    
    Label(newWindow7, text ="Model:").pack()
    model_Entry= Entry(newWindow7, width= 40)
    model_Entry.focus_set()
    model_Entry.pack()
    
    SubmitButton7 = Button(newWindow7, text = 'Submit', width = 50, command=printValue7).pack()
    

#function to View show top 5 sellers --> 8
def openNewWindow8():
    ############################################
    def printValue8():
        import mysql.connector
        mycursor = mydb.cursor()
        
        year = year_Entry.get()
        sql = """
        select Fname, Lname, AVG(price) from seller S inner join Car C ON S.account_link = C.seller_account_link  Where AD_Year = %s group by Fname, Lname order by count(AD_ID) DESC Limit 5
        """ 
        mycursor.execute(sql, (year,))

        
        Label(newWindow8, text = "Sellers First name - Last name - Average Price", font = ('Times New Roman',13,'bold')).pack()
        results = mycursor.fetchall()
        Label(newWindow8, text = results[0]).pack()
        Label(newWindow8, text = results[1]).pack()
        Label(newWindow8, text = results[2]).pack()
        Label(newWindow8, text = results[3]).pack()
        Label(newWindow8, text = results[4]).pack()

        
    ############################################
       
    newWindow8 = Toplevel(master)
 
    newWindow8.title("show top 5 sellers")
 
    newWindow8.geometry("500x300")
    
    #taking info from user
    Label(newWindow8, text ="Search Year:").pack()
    year_Entry= Entry(newWindow8, width= 40)
    year_Entry.focus_set()
    year_Entry.pack()
    
    
    SubmitButton8 = Button(newWindow8, text = 'Submit', width = 50, command=printValue8).pack()
    
#function to Show all the properties --> 9
def openNewWindow9():
    ############################################
    def printValue9():
        
        Fname = Fname_entry.get() ; Lname = Lname_entry.get() ; account_link = link_entry.get() ;
        import mysql.connector
        mycursor = mydb.cursor()

        sql = """
        select * from seller S inner join Car C ON S.account_link = C.seller_account_link where (Fname = %s AND Lname = %s) OR (account_link = %s) """ 
        mycursor.execute(sql, (Fname,Lname,account_link))

        
        results = mycursor.fetchall()
        Label(newWindow9, text = "Ads:").pack()
        for r in results:
            Label(newWindow9, text = r).pack()

        
    ############################################
       
    newWindow9 = Toplevel(master)
 
    newWindow9.title("show ads by a seller")
 
    newWindow9.geometry("500x300")
 
    # A Label widget to show in toplevel
    Label(newWindow9, text ="Enter Car data", font = ('Times New Roman',17,'bold') ).pack()
    Label(newWindow9, text ="enter: first name - last name - account link (if one of them is not avaliable write #)" ).pack()
    
    #taking info from user
    Label(newWindow9, text ="First Name (if not avaliable type #)" ).pack()
    Fname_entry= Entry(newWindow9, width= 60)
    Fname_entry.focus_set()
    Fname_entry.pack()
    
    Label(newWindow9, text ="Last Name (if not avaliable type #)" ).pack()
    Lname_entry= Entry(newWindow9, width= 60)
    Lname_entry.focus_set()
    Lname_entry.pack()
    
    Label(newWindow9, text ="Account link (if not avaliable type #)" ).pack()
    link_entry= Entry(newWindow9, width= 60)
    link_entry.focus_set()
    link_entry.pack()
    
    SubmitButton9 = Button(newWindow9, text = 'Submit', width = 50, command=printValue9).pack()
    

    
#function to Show Show the top 5 models --> 10
def openNewWindow10():
    ############################################
    def printValue10():
        
        low_year = lower_year_entry.get() ; high_year = upper_year_entry.get() ;
        import mysql.connector
        mycursor = mydb.cursor()

        sql = """
        select brand, model from Car where (AD_Year BETWEEN %s AND %s) group by brand, model order by count(AD_ID) DESC, AVG(price) DESC limit 5 
        """ 
        mycursor.execute(sql, (low_year,high_year))

        
        results = mycursor.fetchall()
        Label(newWindow10, text = "brand - model:").pack()
        for r in results:
            Label(newWindow10, text = r).pack()

        
    ############################################
       
    newWindow10 = Toplevel(master)
 
    newWindow10.title("Show the top 5 sellers")
 
    newWindow10.geometry("500x300")
 
    # A Label widget to show in toplevel
    Label(newWindow10, text ="Enter year range ", font = ('Times New Roman',17,'bold') ).pack()
    
    
    #taking info from user
    Label(newWindow10, text ="Year lower limit:" ).pack()
    lower_year_entry= Entry(newWindow10, width= 60)
    lower_year_entry.focus_set()
    lower_year_entry.pack()
    
    Label(newWindow10, text ="Year upper limit:" ).pack()
    upper_year_entry= Entry(newWindow10, width= 60)
    upper_year_entry.focus_set()
    upper_year_entry.pack()
    
    SubmitButton10 = Button(newWindow10, text = 'Submit', width = 50, command=printValue10).pack()
    
    
    
# creating main window with a title
master=Tk()
master.title('Main Window')
master.geometry("600x400")
Label(master,text = "What do you want to do?", font = ('Times New Roman',17,'bold')).pack()

b1 = Button(master, text = '1-Register a user', width = 50, command=openNewWindow1).pack()

b2 = Button(master, text = '2-Create a new car AD', width = 50, command=openNewWindow2).pack()

b3 = Button(master, text = '3-View existing reviews of a given ad', width = 50, command=openNewWindow3).pack()

b4 = Button(master, text = '4-View average ratings for a seller', width = 50, command=openNewWindow4).pack()

b5 = Button(master, text = '5-Show ads for a givin brand', width = 50, command=openNewWindow5).pack()

b6 = Button(master, text = '6-Show all the used cars in a certain location', width = 50, command=openNewWindow6).pack()

b7 = Button(master, text = '7-Show the top 5 areas', width = 50, command=openNewWindow7).pack()

b8 = Button(master, text = '8-Show the top 5 sellers', width = 50, command=openNewWindow8).pack()

b9 = Button(master, text = '9-Show all the properties', width = 50, command=openNewWindow9).pack()

b10 = Button(master, text = '10-Show the top 5 cars', width = 50, command=openNewWindow10).pack()
    
master.mainloop()

