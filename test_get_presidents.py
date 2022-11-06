# Write a PyTest module that queries the DuckDuckGo api for “presidents of the united states,” and tests that each president is listed in the response.  (If you need a list or our presidents, see Presidents (opens in new window))
# The presidents should be listed in the RelatedTopics returned field.  RelatedTopics is a list, and you should check the Text entries of RelatedTopics to search for presidents.  We’ll only look for the last name of a president.  That means that we won’t distinguish between John Adams and his son, John Quincy Adams, or George Bush the senior and ‘W.’
# Place your test code in a GitHub repository.  

import pytest
from get_presidents import QueryPresidents

class TestQueryPresidents():
    url = "https://api.duckduckgo.com"
    @pytest.fixture(scope="function")
    def test_query_object(self):
        """Fixture that is rebuilt after each function.

        Returns:
            a test query object
        """
        query = "presidents+of+the+United+States"
        return QueryPresidents(self.url, query)
    
    
    def test_ddg0(self):
        query = "DuckDuckGo"
        test_query = QueryPresidents(self.url, query)
        res = test_query.get_response()
        assert "DuckDuckGo" in res["Heading"]
    
    def test_wrong_query(self):
        query  = "List+Of+Presidents+of+United+States+of+America"
        test_query = QueryPresidents(self.url, query)
        res = test_query.get_response()
        assert res["RelatedTopics"] == []
    
    def test_get_presidents(self, test_query_object):
        res = test_query_object.get_response()
        assert "Presidents of the United States" in res["Heading"]
        
    def test_related_topics(self, test_query_object):
        res = test_query_object.get_response()
        all_res =  res["RelatedTopics"]
        assert len(all_res)
    
    def test_get_results(self, test_query_object):
        results = test_query_object.get_results()
        assert len(results) != len(test_query_object._presidents_list) # the results list is greater because the Text field has additional entries like speeches and books as well
    
    def test_does_not_match_results_length(self, test_query_object):
        matched = test_query_object.match_results()
        assert len(matched) == len(test_query_object._presidents_list) # confirm that all the presidents in the presidents_list are in the response
    
    def test_does_not_match_results(self, test_query_object):
        matched = test_query_object.match_results()
        assert matched != test_query_object._presidents_list # because neither of them are in sorted order
    
    def test_match_results(self, test_query_object):
        matched = test_query_object.match_results()
        assert sorted(matched) == sorted(test_query_object._presidents_list)
    
    def test_name_not_repeated(self, test_query_object):
        matched = test_query_object.match_results()
        for match in matched:
            assert matched.count(match) == 1 # this will always work because set() has been called on matched results in the code and there is no chance of a bug like a name getting repeated, even if it is repeated in the results list
        