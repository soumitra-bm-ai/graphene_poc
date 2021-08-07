from ariadne import ObjectType, QueryType
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import FederatedObjectType, make_federated_schema

type_defs = """
  type Query {
    topProducts(first: Int = 5): [Product]
  }
  type Product @key(fields: "upc") {
    upc: String!
    name: String
    price: Int
    weight: Int
  }
"""

query = QueryType()
products = FederatedObjectType("Product")


@query.field("topProducts")
def resolve_top_products(*_, first):
    return products[:first]


@products.reference_resolver
def resolve_product_reference(_, _info, representation):
    return get_product_by_upc(representation["upc"])


schema = make_federated_schema(type_defs, [query, products])
