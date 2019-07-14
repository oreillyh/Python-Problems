def main():
	#While True:
		display_menu()
		choice = input("Choice:")
		if (choice == "1"):
			view_15()
		elif(choice == "2"):
			view_by_pop()
		elif(choice == "3"):
			add_new_city()
		elif (choice == "4"):
			find_new_car()
		elif (choice == "5"):
			add_new_car()
		elif (choice == "6"):
			view_con_by_name()
		elif (choice == "7"):
			view_con_by_pop()
		elif (choice == "8"):
			exit_app()
	
def display_menu():
	print("World DB")
	print("--------")
	print("")
	print("MENU")
	print("====")
	print("1 - View 15 Cities")
	print("2 - View Cities by Population")
	print("3 - Add New City")
	print("4 - Find New Car by Engine Size")
	print("5 - Add New Car")
	print("6 - View Countries by Name")
	print("7 - View Countries by Population")
	print("8 - Exit Application")
	
def view_15():
	#select * from city where id<16;

if __name__== "__main__":
	main()