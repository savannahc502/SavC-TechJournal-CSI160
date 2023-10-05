# Some tips about Lab 5

url = "https://www.champlain.edu/courses"


def domain_name_extractor(url):
    protocol = url[0:7]
    if(protocol == "https:/"):
        domain = url[8:]
        pos = domain.index("/")
        print (domain[0:pos])
    elif(protocol == "http://"):
        domain = url[7:]
        pos = domain.index("/")
        print(domain[0:pos])

    # print(domain)

    """Given a url, return the domain name

    You will need to utilize the .find method to complete this https://docs.python.org/3/library/stdtypes.html#str.find

    Hint: Find the starting point of the domain name, then find the end point.
    params:
    url (string) the url to search. Example: https://docs.python.org/3/library

    return (string) The domain name or IP address. Example: docs.python.org
    """
    pass

# domain_name_extractor(url)

y = url.find('w')
domain = url[y:]  # www.champlain.edu/course
z = domain.find('/')  # Find the '/'
                        # Finds the '/' and pass it the the variable 'z'
print(domain[0:z])  # Remember, the 'domain' variable holds: www.champlain.edu/course
                    # Start the slice at zero. The end of the slice is up to BUT DO NOT INCLUDE
                    # the "/" and it sindex position is held in the variable 'z'
