# import graphene
# # from graphql_auth.schema import UserQuery, MeQuery
#
# from sub_service_schema.accounts_schema import Aggregator, AggQuery
# from sub_service_schema.food_schema import Food, FoodQuery
#
#
# class Query(FoodQuery,AggQuery):
#     Aggregator = graphene.Field(Aggregator)
#     Food = graphene.Field(Food)
#
#     # def get_dict_from_info(self,data):
#     #     if isinstance(data,list):
#     #         ans={}
#     #         for i in data:
#     #             ans[]
#     # def resolve_Aggregator(root,info):
#     #     #print(info.field_asts[0].selection_set.selections,"*"*40)
#     #     #print(parent)
#     #     return "1"
#     # def resolve_Food(parent,info):
#     #     return "1"
#
#
# schema = graphene.Schema(query=Query)
# #print(schema.__dict__)
###############################################################

# schema.py
from ariadne import QueryType, make_executable_schema
type_defs = """

    type Token{
        name: String
        count: Int
    }
    type Query {
        hello: String!
        tokens: [Token!]!
    }

"""

query = QueryType()


@query.field("tokens")
def resolve_tokens(*kwargs):
    return [
        {
            "name":"sam",
            "count":1,
        }
    ]
@query.field("hello")
def resolve_hello(*_):
    return "Hello world!"

schema = make_executable_schema(type_defs, query)