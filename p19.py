#dictionaries 

#string

studentid={
    #"key":"value",

    "101":"mahim",
    "102":"masud",
    "103":"tayeb",
    "104":"tamim",
}

print(studentid["101"])
print(studentid.get("103","invalid key"))
print(studentid.get("106","invalid key"))


#integer

studentid={
    #"key":"value",

    101:"mahim",
    102:"masud",
    103:"tayeb",
    104:"tamim",
}

print(studentid[101])
print(studentid.get(103,"invalid key"))
print(studentid.get(106,"invalid key"))
