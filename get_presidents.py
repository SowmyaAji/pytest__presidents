import requests


class QueryPresidents():
    
    _presidents_list = [ "Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Van Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Truman", "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"]
    
    def __init__(self, url:str, query:str) -> None:
        self.url = url
        self.query = query
        
    def get_response(self):
        resp = requests.get(f"{self.url}/?q={self.query}&format=json")
        return resp.json()

    def get_results(self) -> list:
        response = self.get_response()
        print("Heading: ", response["Heading"])
        all_res = response["RelatedTopics"]
        results = [res["Text"][:25].upper() for res in all_res]
        return results
    
    def match_results(self) -> list:
        results = self.get_results()
        # get just the first bit to reduce the amount of string to be checked; upper case it to standardize the case for checking
        matched_presidents = set([prez for prez in self._presidents_list if any(prez.upper() in result for result in results)])# gets each string in the texts field that includes a Prez's name and the set makes sure a Prez's name doesn't come twice if it is repeated in the two texts
        return list(matched_presidents)


query = "presidents+of+the+United+States"
url = "https://api.duckduckgo.com"
query_presidents = QueryPresidents(url, query)

if __name__=="__main__":
    result = query_presidents.match_results()
    print("Result: ", result)