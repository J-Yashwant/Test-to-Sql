from database import get_collection
from models import MCPModel

def insert_mcp(data):
    collection = get_collection("mcp_records")
    mcp_instance = MCPModel(**data)
    result = collection.insert_one(mcp_instance.to_dict())
    return {"message": "Inserted successfully", "id": str(result.inserted_id)}

def fetch_mcp(record_id):
    collection = get_collection("mcp_records")
    data = collection.find_one({"_id": record_id})
    return data if data else {"error": "Record not found"}