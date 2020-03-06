Question 1

import requests
# GET REQUEST
Response = requests.get('https://www.google.com/search?hl=en&sxsrf=ACYBGNRO4N_KLJLcil043Xq9GiO45sHnRA%3A1580354690533&source=hp&ei=gkwyXu-wHsrH5gLDj5aACg&q=tim+berners+lee&oq=tim+berners+lee&gs_l=psy-ab.3..35i39j0i67j0l8.423.6631..6781...3.0..1.658.3413.8j2j1j3j0j2......0....1..gws-wiz.....10..0i131i67j0i131j35i362i39j0i20i263.phK3SJsQLH8&ved=0ahUKEwjv-cj_r6rnAhXKo1kKHcOHBaAQ4dUDCAg&uact=5')

#Status Code
print(Response.status_code)

#Content
print(Response.content)

#Headers
print(Response.headers)



Question 2

#Post
R=requests.post("https://www.google.com",data = {'Email':'sj','Password':'qwerty'})
print(R)

#Status Code
print(R.status_code)

#Content
print(R.content)

#Headers
print(R.headers)



#Question 3

# Request to a non-existing URL
R1=requests.get("https://www.facebook.com/asdascf")

#Status code
print(R1.status_code)

#Headers
print(R1.headers)

#Content
print(R1.content)
