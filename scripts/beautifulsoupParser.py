import pandas as pd
from bs4 import BeautifulSoup

html = '''<!DOCTYPE html><html><body><h4>The five main constituents of an actively perceiving agent are defined</h4><head><style> table, th, td {border: 1px solid black;}</style></head><body><table xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" frame="hsides" rules="groups"><thead><tr><th align="left">Active perception</th><th align="left">Definition</th></tr></thead><tbody><tr><td align="left">Why</td><td align="left">The current state of the agent determines what its next actions might be based on the expectations that its state generates. These are termed Expectation-Action tuples. This would rely on any form of inductive inference (inductive generalization, Bayesian inference, analogical reasoning, prediction, etc.) because inductive reasoning takes specific information (premises) and makes a broader generalization (conclusion) that is considered probable. The only way to know is to test the conclusion. A fixed, pre-specified, control loop is not within this definition</td></tr><tr><td align="left">What</td><td align="left">Each expectation applies to a specific subset of the world that can be sensed (visual field, tactile field, etc.) and any subsequent action would be executed within that field. We may call this Scene Selection</td></tr><tr><td align="left">How</td><td align="left">A variety of actions must precede the execution of a sensing or perceiving action. The agent must be placed appropriately within the sensory field (Mechanical Alignment). The sensing geometry must be set to enable the best sensing action for the agent’s expectations (Sensor Alignment, including components internal to a sensor such as focus, light levels, etc.). Finally, the agent’s perception mechanism must be adapted to be most receptive for interpretation of sensing results, both specific to current agent expectations as well as more general world knowledge (Priming)</td></tr><tr><td align="left">When</td><td align="left">An agent expectation requires Temporal Selection, that is, each expectation has a temporal component that prescribes when is it valid and with what duration</td></tr><tr><td align="left">Where</td><td align="left">The sensory elements of each expectation can only be sensed from a particular viewpoint and its determination is modality specific. For example, how an agent determines a viewpoint for a visual scene differs from how it does so for a tactile surface. The specifics of the sensor and the geometry of its interaction with its domain combine to accomplish this. This will be termed the Viewpoint Selection process</td></tr></tbody></table></body></html>
'''

def get_tags(input_file):
    '''Function to retrieve all unique html tags from a lxml document'''
    all_tags= []
    with open(input_file, 'r') as file:
        for line in file:
            soup = BeautifulSoup(line, 'lxml')  # Parse the HTML as a string
            tags = [tag.name for tag in soup.find_all()]
            all_tags += tags

    unique_tags = list(set(all_tags))
    print(unique_tags)
    print(len(unique_tags))

get_tags("../data/textfiles/text.txt")
