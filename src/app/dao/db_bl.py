from app.dao.db_base import DALBase


class BlazegraphDB(DALBase):
    def get_all_classes(self):
        return self.get_query(
            "SELECT ?class WHERE {?class a <http://www.w3.org/2002/07/owl#Class>}"
        )

    def get_all_individual_iri_and_label(self):
        return self.get_query(
            """prefix owl: <http://www.w3.org/2002/07/owl#>
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?individual_iri ?individual_label WHERE {
            ?individual_iri a owl:NamedIndividual;
            }"""
        )

    def get_all_subject_and_predicate_and_object(self):
        return self.get_query(
            "SELECT ?subject ?predicate ?object WHERE {?subject ?predicate ?object}"
        )
