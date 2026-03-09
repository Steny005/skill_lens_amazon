import json
def save_steps(steps, frames):

    data = []

    for i in range(len(steps)):
        data.append({
            "step": i + 1,
            "instruction": steps[i],
            "frame": frames[i]
        })

    with open("tutorial_steps.json", "w") as f:
        json.dump(data, f, indent=4)