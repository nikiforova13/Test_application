import pytest
import requests  # type: ignore

test_url = "http://127.0.0.1:8000"


@pytest.mark.parametrize("uri", ["docs", "/"])
def test_available_urls(uri):
    response = requests.get(f"{test_url}/{uri}")
    assert response.status_code == 200


query1 = """prefix owl: <http://www.w3.org/2002/07/owl#>
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?individual_iri ?individual_label WHERE {
            ?individual_iri a owl:NamedIndividual;
            }"""
query2 = "SELECT ?subject ?predicate ?object WHERE {?subject ?predicate ?object}"
query3 = "SELECT ?subject ?predicate ?object WHERE {?subject ?predicate ?object}"


@pytest.mark.parametrize(
    "query", [query1, query2, query3], ids=["query1", "query2", "query3"]
)
def test_get_data_from_db(query):
    response = requests.post(f"{test_url}/blazegraph/fetch", json={"query": query})
    assert len(response.json()) != 0
    assert response.status_code == 200


@pytest.mark.parametrize(
    "query, status_code",
    ([{}, 404], ['{"query": "ddd"}"', 500]),
    ids=["query_with_null", "incorrect_value"],
)
def test_get_data_from_db_with_invalid_query(query, status_code):
    response = requests.post(f"{test_url}/blazegraph/fetch", json=query)
    assert len(response.json()) != 0
    assert response.status_code == status_code
