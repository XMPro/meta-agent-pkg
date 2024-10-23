# TODO include example of this
from src.packages.logs_to_node_graph.action_agent.source_code.logs_to_neo4j import update_node_graph
import os
import json
from datetime import datetime
from collections import defaultdict
import glob
from neo4j import GraphDatabase

# Global variables
stream_object_id = None
stream_object_title = None
data_stream_id = None
stream_host_id = None
stream_host_collection_id = None
ds_server_url = None
events_processed_count = 0
stream_object_event_count = 0


def on_create(data: dict) -> dict | None:
    return {}


def on_receive(data: dict) -> dict | None:

    result = update_node_graph('/app/logs')
    # print(result)
    return result


def on_destroy() -> dict | None:
    return {}



# def _merge_stream_object_edge(tx):
#     query = """
#         MATCH (so:StreamObject {id: $so_id})
    
#         MERGE (sot:StreamObject {id: $so_target_id})
#         SET sot.last_updated = $last_updated
        
#         WITH so, sot
    
#         MERGE (so)-[r:CONNECTS_TO {
#                 id: $sh_rel_id, 
#                 source_id: $so_id, 
#                 target_id: $so_target_id,
#                 last_updated: $last_updated
#             }]->(sot)
#     """

#     tx.run(query, {
#         "so_id": stream_object_id,
#         "so_target_id": stream_object_target_id,
#         "sh_rel_id": stream_object_id + "_" + stream_object_target_id,
#         "last_updated": datetime.now().isoformat()
#     })




# def _merge_sh_collection_and_sh_edge(tx):
#     query = """
#         MATCH (sh:StreamHost {id: $sh_id})
    
#         MERGE (c:Collection {id: $sh_collection_id})
#         SET c.title = $sh_collection_title,
#             c.last_updated = $last_updated

#         WITH sh, c
        
#         MERGE (c)-[cr:BELONGS_TO { 
#                 id: $sh_collection_rel_id
#             }]->(sh)
#         ON CREATE SET cr.source_id = $sh_collection_id, 
#             cr.target_id = $sh_id,
#             cr.last_updated = $last_updated
#     """

#     tx.run(query, {
#         "sh_id": stream_host_id,
#         "sh_collection_id": stream_host_collection_id,
#         "sh_collection_title": stream_host_collection_title,
#         "sh_collection_rel_id": stream_host_collection_id + "_" + stream_host_id,
#         "last_updated": datetime.now().isoformat()
#     })


# def _merge_ds_and_sh_collection_edge(tx):
#     query = """
#         MATCH (c:Collection {id: $sh_collection_id})
    
#         MERGE (ds:DataStream {id: $ds_id})
#         SET ds.title = $ds_title,
#             ds.last_updated = $last_updated
        
#         WITH c, ds
        
#         MERGE (ds)-[dsr:BELONGS_TO { 
#                 id: $ds_rel_id
#             }]->(c)
#         ON CREATE SET dsr.source_id = $ds_id, 
#             dsr.target_id = $sh_collection_id,
#             dsr.last_updated = $last_updated
#     """

#     tx.run(query, {
#         "sh_collection_id": stream_host_collection_id,
#         "ds_id": data_stream_id,
#         "ds_title": data_stream_title,
#         "ds_rel_id": data_stream_id + "_" + stream_host_collection_id,
#         "last_updated": datetime.now().isoformat()
#     })


# def _merge_node_event_count(tx):
#     query = """
#     MERGE (so:StreamObject {id: $so_id})
#     SET so.event_count = $so_event_count,
#         so.last_updated = $last_updated
#     """

#     tx.run(query, {
#         "so_id": stream_object_id,
#         "so_event_count": stream_object_event_count,
#         "last_updated": datetime.now().isoformat()
#     })