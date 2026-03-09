import boto3
import json

def extract_steps(transcript):

    prompt = f"""
    Convert the following tutorial transcript into clear numbered learning steps.

    Transcript:
    {transcript}

    Format:
    Step 1:
    Step 2:
    Step 3:
    """

    client = boto3.client("bedrock-runtime")

    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 400,
            "temperature": 0.2
        }
    })

    response = client.invoke_model(
        body=body,
        modelId="amazon.nova-2-lite",
        accept="application/json",
        contentType="application/json"
    )

    result = json.loads(response["body"].read())

    return result["results"][0]["outputText"]