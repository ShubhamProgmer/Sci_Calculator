# Calculator - optimised and scientific one!

import math
import time
print("-----------------------------")
print("\tCALCULATOR")
print("-----------------------------")
print()
print("Welcome to our calculator!\nWhat do you want to do?\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square root\n6. Trigonometry")
while 1:
	print()
	while 1:
		try:
			a = int(input("Please enter the accordingly serial number: "))
			break
		except Exception as e:
			print("Please enter a valid input!")
			continue
		
	if a == 1:
		while 1:
			try:
				b = float(input("1st number to add: "))
				c = float(input("2nd number to add: "))
				break
			except Exception as e:
				print("You are requested to provide NUMBERS!")
				continue
			
		print(f"Your sum is: {c+b}")
		
	elif a == 2:
		while 1:
			try:
				b = float(input("1st number to subtract: "))
				c = float(input("2nd number to subtract: "))
				break
			except Exception as e:
				print("You are requested to provide NUMBERS!")
				continue
			
		print(f"Your subtraction is: {b-c}")	
	
	elif a == 3:
		while 1:
			try:
				b = float(input("1st number to multiply: "))
				c = float(input("2nd number to multiply: "))
				break
			except Exception as e:
				print("You are requested to provide NUMBERS!")
				continue
			
		print(f"Your multiplication is: {b*c}")
		
	elif a == 4:
		while 1:
			try:
				b = float(input("1st number to divide: "))
				c = float(input("2nd number to divide: "))
				break
			except Exception as e:
				print("You are requested to provide VALID NUMBERS!")
				continue
			
		print(f"Your division is: {b/c} (remainder = {b%c} and quotient = {b//c})")
		
	elif a == 5:
		while 1:
			try:
				b = float(input("Enter number of which you want square root: "))
				break
			except Exception as e:
				print("You are requested to provide NUMBERS!")
				continue
			
		print(f"Your square root is: {math.sqrt(b)}")
		
	elif a == 6:
		 print("Please choose the Trigonometric ratio:\n1. cos\n2. sine\n3. tan\n4. cosec\n5. sec\n6. cot")
		 print()
		 while True:
			 while True:
		 		try:
		 			b = int(input("Please enter the accordingly serial number for trigo ratio: "))
		 			break
		 		except Exception as e:
		 			print("You are requested to provide VALID NUMBERS!")
		 		continue
		 
		 	
			 if b == 1:
			 		while 1:
			 			try:
			 				c = float(input("Please enter angle (in degrees) "))
		 					break
			 			except Exception as error:
			 				print("You must consider again that you are providing us ANGLE IN DEGREES")
			 				continue
		 				
		 			d = math.cos(math.radians(c))
		 			e = round(d, 3)
		 			print(f"cos({c}) degrees = {e}")
		 			break
			 elif b == 2:
		 			while 1:
		 				try:
		 					c = float(input("Please enter angle (in degrees) "))
		 					break
		 				except Exception as error:
		 					print("You must consider again that you are providing us ANGLE IN DEGREES")
		 					continue
		 				
		 			d = math.sin(math.radians(c))
		 			e = round(d, 3)
		 			print(f"sin({c}) degrees = {e}")
		 			break
			 elif b == 3:
		 			while 1:
		 				try:
		 					c = float(input("Please enter angle (in degrees) "))
		 					break
		 				except Exception as error:
		 					print("You must consider again that you are providing us ANGLE IN DEGREES")
		 					continue
		 			d = math.tan(math.radians(c))
		 			e = round(d, 3)
		 			if d > 1000:
		 				print(f"tan({c}) degrees = infinity or not defined")
		 			else:
		 				print(f"tan({c}) degrees = {e}")
		 			break
			 elif b == 4:
		 			while 1:
		 				try:
		 					c = float(input("Please enter angle (in degrees) "))
		 					break
		 				except Exception as error:
		 					print("You must consider again that you are providing us ANGLE IN DEGREES")
		 					continue
		 			try:
		 				d = (math.sin(math.radians(c)))**-1
		 			except Exception as e:
		 				print(f"cosec({c}) degrees = infinity or not defined")
		 			
		 			else:
		 				e = round(d, 3)
		 				print(f"cosec({c}) degrees = {e}")
		 			break
			 elif b == 5:
		 			while 1:
		 				try:
		 					c = float(input("Please enter angle (in degrees) "))
		 					break
		 				except Exception as error:
		 					print("You must consider again that you are providing us ANGLE IN DEGREES")
		 					continue
		 			try:
		 				d = (math.cos(math.radians(c)))**-1
		 				if d > 1000:
		 					print(f"sec({c}) degrees = infinity or not defined")
		 				else:
		 					e = round(d, 3)
		 					print(f"sec({c}) degrees = {e}")
		 			except Exception as e:
		 				print(f"sec({c}) degrees = infinity or not defined")
		 			break
			 elif b == 6:
		 			while 1:
		 				try:
		 					c = float(input("Please enter angle (in degrees) "))
		 					break
		 				except Exception as error:
		 					print("You must consider again that you are providing us ANGLE IN DEGREES")
		 					continue
		 			try:
		 				d = (math.tan(math.radians(c)))**-1
		 				if d > 1000:
		 					print(f"cot({c}) degrees = infinity or not defined")
		 				else:
		 					e = round(d, 3)
		 					print(f"cot({c}) degrees = {e}")
		 			except Exception as e:
		 				print(f"cot({c}) degrees = infinity or not defined")
		 			break
			 else:
			 		print("Please enter a VALID OPTION")
			 		continue

	while True:
		 		print()
		 		z = input("Do you want to use this calculator again? (y/n) ")
		 		if z != "y" and z != "n":
		 			print("Please enter a valid option!")
		 			continue
		 		elif z == "y":
		 			break
		 			
		 		else:
		 			print()
		 			print()
		 			print("Thank you for using this calculator!\nExiting......")
		 			time.sleep(5)
		 			exit()
		 			
	continue
		 					 		
		 		
		 			

		 					 