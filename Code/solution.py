# Jake Schnyder - Assignment 1

def verify_access(username, password, clearance_level):
    # TODO: Write your logic below and return the matching string
    #If username is not equal to "soc_admin" or password is not equal to "S3cur3_P@ss", return "INTRUSION_DETECTED".  Otherwise (meaning the username and password are correct), check clearance_level:
    if (not(username == "soc_admin" and password == "S3cur3_P@ss")):    
        return ("INTRUSION_DETECTED");

    #If clearance_level is greater than or equal to 5, return "ROOT_ACCESS_GRANTED".
    if(clearance_level >= 5):
        return ("ROOT_ACCESS_GRANTED");
    
    #If clearance_level is 3 or 4, return "ANALYST_ACCESS_GRANTED".
    elif(3 == clearance_level or clearance_level == 4):
        return ("ANALYST_ACCESS_GRANTED");

    #For any lower clearance_level, return "INSUFFICIENT_CLEARANCE".
    else:
        return ("INSUFFICIENT_CLEARANCE");
    
    pass


