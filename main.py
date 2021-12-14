print("\u001b[37m=============================================================================")
print()
print("\u001b[35m ##     ## ##     ## ##       ##    ## ##     ## ##     ## ##    ## ########")
print(" ##     ## ##     ## ##       ###   ## ##     ## ##     ## ###   ##    ##")
print(" ##     ## ##     ## ##       ####  ## ##     ## ##     ## ####  ##    ##")
print(" ##     ## ##     ## ##       ## ## ## ######### ##     ## ## ## ##    ##")
print("  ##   ##  ##     ## ##       ##  #### ##     ## ##     ## ##  ####    ##")
print("   ## ##   ##     ## ##       ##   ### ##     ## ##     ## ##   ###    ##")
print("    ###     #######  ######## ##    ## ##     ##  #######  ##    ##    ## ")
print()
print("\u001b[37m=============================================================================")
carryOn = 'y'
while carryOn.lower() == 'y':
    print("\u001b[245mchoose the vulnerability : ", "\n\u001b[34m1.Broken Access", "\n2.SSRF", "\n3.Insecure Design",
          "\n4.Security Misconfiguration", "\n5.OS command injection", "\n6.Vulnerable and Outdated Components")
    s = input("\n\u001b[0mselect number of vulnerability from menu: ")
    print("\u001b[245mchoose the examination method :", "\n\u001b[34m1.Describe", "\n2.Manually", "\n3.Exit")
    m = input("\u001b[0mSelect the number of the method : ")
    if s == '1':
        if m == '1':
            infile = open("BrokenAccess.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        elif m == '2':
            infile = open("BrokenCode.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        else:
            break

    elif s == '2':
        if m == '1':
            infile = open("SSRF.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        elif m == '2':
            infile = open("SSRFcode.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        else:
            break

    elif s == '3':
        if m == '1':
            infile = open("ID.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        elif m == '2':
            infile = open("IDcode.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        else:
            break

    elif s == '4':
        if m == '1':
            infile = open("Security.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        elif m == '2':
            infile = open("SecurityCode.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        else:
            break

    elif s == '5':
        if m == '1':
            infile = open("OS.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        elif m == '2':
            infile = open("OScode.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        else:
            break

    elif s == '6':
        if m == '1':
            infile = open("CF.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        elif m == '2':
            infile = open("CFcode.txt", 'r')
            for dat in infile:
                print(dat, end="")
            infile.close()
        else:
            break
    carryOn = input("\n\n\u001b[33mDo you want try again (y/n)? ")
