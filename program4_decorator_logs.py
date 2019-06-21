import functools
import logging
import requests

class ApiHelper:
 def decorator_arguments(page_nr):
    def my_decorator(f):
        @functools.wraps(f)
        def function_that_runs_f(*args, **kwargs):
            print ("inside decorators")
            logging.info(page_nr,'Page Number has passed  as Arguments')
            if(page_nr <1):
                logging.warning("Invalid Page no")
            else:
                f(*args, **kwargs)
                print("After Decorators")
        return function_that_runs_f
    return my_decorator

 @decorator_arguments(1)
 def star_wars_characters(self,page_nr):
        # Start with an empty list
            total_chr = []
            final_result = []

# Grab the search results
            response = requests.get("https://swapi.co/api/people/")
            data = response.json()

# Store the first page of results
            total_chr = total_chr + data['results']
            a=1
# While data['next'] isn't empty, let's download the next page, too
            while data['next'] is not None:
                  if(page_nr==1): 
                      break
                  elif(a==page_nr):
                     total_chr = []
                     print("page found")
    # Store the current page of results
                     total_chr =data['results']
                     break
                  else:
                     a=a+1
                     response = requests.get(data['next'])
                     data = response.json()
                     total_chr =data['results']
                     
            if(a!=page_nr):
                print ("No Result found for selected page no ",page_nr)
                #logging.warning('No Result found for selected page no ',page_nr)
            else:
                print("Page have", len(total_chr), "total starwars characters")
                logging.info("Page " ,page_nr, " have", len(total_chr), "total starwars characters")
                for person in total_chr:
                    final_result.append([person['name'],person['height'],person['gender']])
            print (final_result)
            
tmp=ApiHelper()
tmp.star_wars_characters(1)