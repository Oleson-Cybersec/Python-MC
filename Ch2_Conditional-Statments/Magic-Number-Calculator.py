# Magic Number calculator. Multiples month and day. If it equals the year, then it's a magic number!

print("\nPick a date, and I'll let you know if it's a magic number!")
print("This requires the MM / DD / YY format\n")


# Month input + Logic Check
MM = int(input("Enter the month [MM]: "))
if MM in range(1, 13):
    pass
else:
    print()
    print ((str(MM).zfill(2)), "is an invalid month identifier... try again")
    quit()


# Day input + Logic Check
DD = int(input("Enter the day of the month [DD]: "))
# Day Logic Check
if DD in range(1, 32):
    pass
else:
    print()
    print ((str(DD).zfill(2)), "is not a real day of the month... try again.")
    quit()


# Year input + Logic Check
YY = int(input("Enter the year [YY]: "))
if YY in range(0, 100):
    pass
else:
    print()
    print ((str(YY).zfill(2)), "is not a valid year format... try again.")
    quit()


print() # Extra space after inputs
DateFormat = (str(MM).zfill(2)) + "/" + (str(DD).zfill(2)) + "/" + (str(YY).zfill(2)) # zfill will make value at least 2 characters ( i.e. 2 -> 02 )



# Month + Day Logic
#############################################################################
if MM == 1 and 0 > DD > 32:    # Jan Proper Dates (1-31)
    print(DD, "is not a real day in the month of January...")
    quit()
else:
    pass
#############################################################################
if MM == 2 and DD == 29:    # Accounting for leap year every 4 years (Feb 29th)
    print ("Wow! You were born on a leap year?! HOW COOL IS THAT!\n")
    pass
else:
    pass
#############################################################################
if MM == 2 and 1 < DD > 29:  # Feb Proper Dates (1-28;29)
    print(DD, "is not a real day in the month of February...")
    quit()
else:
    pass
#############################################################################
if MM == 3 and 1 < DD > 31:  # Mar Proper Dates (1-31)
    print(DD, "is not a real day in the month of March...")
    quit()
else:
    pass
#############################################################################
if MM == 4 and 1 < DD > 30:  # Apr Proper Dates (1-30)
    print(DD, "is not a real day in the month of April...")
    quit()
else:
    pass
#############################################################################
if MM == 5 and 1 < DD > 31:  # May Proper Dates (1-31)
    print(DD, "is not a real day in the month of May...")
    quit()
else:
    pass
#############################################################################
if MM == 6 and 1 < DD > 30:  # June Proper Dates (1-30)
    print(DD, "is not a real day in the month of June...")
    quit()
else:
    pass
#############################################################################
if MM == 7 and 1 < DD > 31:  # July Proper Dates (1-31)
    print(DD, "is not a real day in the month of July...")
    quit()
else:
    pass
#############################################################################
if MM == 8 and 1 < DD > 31:  # Aug Proper Dates (1-31)
    print(DD, "is not a real day in the month of August...")
    quit()
else:
    pass
#############################################################################
if MM == 9 and 1 < DD > 30:  # Sep Proper Dates (1-30)
    print(DD, "is not a real day in the month of September...")
    quit()
else:
    pass
#############################################################################
if MM == 10 and 1 < DD > 31:   # Oct Proper Dates (1-31)
    print(DD, "is not a real day in the month of October...")
    quit()
else:
    pass
#############################################################################
if MM == 11 and 1 < DD > 30:   # Nov Proper Dates (1-30)
    print(DD, "is not a real day in the month of November...")
    quit()
else:
    pass
#############################################################################
if MM == 12 and 1 < DD > 31:   # Dec Proper Dates (1-31)
    print(DD, "is not a real day in the month of December...")
    quit()
else:
    pass
#############################################################################


# Magic Number Calculation:
Mathmatics = (MM * DD == YY)


if Mathmatics == True:
    print ("The date", DateFormat, "is indeed a magic number :~)")
else:
    print("                     vvv\nThe date", DateFormat, "is NOT a magic number. What a shame :/\n                     ^^^")
