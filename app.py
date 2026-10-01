import json

def handler(event=None, context=None):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "service": "p-api",
            "status": "healthy",
            "version": "1.0.0"
        })
    }

if __name__ == "__main__":
    print(handler()["body"])
