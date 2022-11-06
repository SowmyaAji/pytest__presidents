import pytest
from get_presidents import QueryPresidents

class TestQueryPresidents():
    
    def test_wrong_query(self):
        url = "https://api.duckduckgo.com"
        query  = "List+Of+Presidents+of+United+States+of+America"
        test_query = QueryPresidents(url, query)
        res = test_query.get_response()
        assert res["RelatedTopics"] == []
    
    @pytest.fixture(scope="class")
    def test_query_results(self):
        """Fixture that is built just once for the class

        Returns:
            the matched results, api response and the list of presidents to check against as a tuple
        """
        url = "https://api.duckduckgo.com"
        query = "presidents+of+the+United+States"
        test_query_object = QueryPresidents(url, query)
        return test_query_object.match_results() # (matched_results, api response, presidents_list)
    
    def test_get_presidents(self, test_query_results):
        assert "Presidents of the United States" in test_query_results[1]["Heading"]
        
    def test_related_topics(self, test_query_results):
        all_res =  test_query_results[1]["RelatedTopics"]
        assert len(all_res)
    
    def test_match_results_length(self, test_query_results):
        assert len(test_query_results[0]) == len(test_query_results[2]) # confirm that all the presidents in the presidents_list are in the response
    
    def test_does_not_match_results(self, test_query_results):
        assert test_query_results[0] != test_query_results[2] # the results of don't match because neither list is in sorted order
    
    def test_match_results(self, test_query_results):
        assert sorted(test_query_results[0]) == sorted(test_query_results[2])
    
    def test_name_not_repeated(self, test_query_results):
        matched = test_query_results[0]
        for match in matched:
            assert matched.count(match) == 1 # this will always work because set() has been called on matched results in the code and there is no chance of a bug like a name getting repeated, even if it is repeated in the results list
        