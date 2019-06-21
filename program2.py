import requests

class ApiHelper:
    def append_to_file(self,filepath):

# Start with an empty list
        total_chr = []
        final_result = []

# Grab the search results
        response = requests.get("https://swapi.co/api/people/")
        data = response.json()

# Store the first page of results
        total_chr = total_chr + data['results']
 
# While data['next'] isn't empty, let's download the next page, too
        while data['next'] is not None:
                response = requests.get(data['next'])
                data = response.json()
                total_chr =total_chr+data['results']
    
        if(len(total_chr)==0):
            print ("No Result found for selected page no ")
        else:
            print("Page have", len(total_chr), "total characters")
            for person in total_chr:
                f= open(filepath,"a+")
                final_result=[person['name'],person['height'],person['gender']]
                with open(filepath, "+a") as output:
                    l1= ", ".join( repr(e) for e in final_result )
                    print (l1)
                    output.write(l1.replace("'","")+'\n')
                    f.close()

        

tmp=ApiHelper()
tmp.append_to_file("program2result.txt")