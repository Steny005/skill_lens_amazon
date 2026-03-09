import boto3

def generate_steps_from_frames(frame_list):

    client = boto3.client("bedrock-runtime")

    steps = []

    for frame in frame_list:

        prompt = f"""
        Look at this tutorial frame and describe the action
        as a clear instruction step along with the correct directions like left to right etc.
        """

        response = client.invoke_model(
            modelId="amazon.nova-2-lite",
            body=prompt
        )

        steps.append(response)

    return steps