import requests

class ApiHelper:
    def star_wars_characters(self, page_nr): 

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
            print ("No Result found for selected page no ")
        else:
            print("Page have", len(total_chr), "total characters")
            for person in total_chr:
                final_result.append([person['name'],person['height'],person['gender']])
                #final_result.append('\n')

        return final_result
    
tmp=ApiHelper()
final_result=tmp.star_wars_characters(9)
print (final_result)