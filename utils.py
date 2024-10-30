import numpy as np
import os
import glob
import torch

def array_into_text(arr_old):
    text = ""
    if(arr_old.shape[0] == 3):
        arr = np.transpose(arr_old, (1, 2, 0))
    else:
        arr = arr_old
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if (arr[j][i][0] == 2 and arr[j][i][1] == 5 and arr[j][i][2] == 0):
                text+="#"
            elif (arr[j][i][0] == 10 and arr[j][i][1] == 0):
                text+="@"
            elif (arr[j][i][0] == 10 and arr[j][i][1] == 0 and arr[j][i][2] == 0):
                text+="\u2192"
            elif (arr[j][i][0] == 10 and arr[j][i][1] == 0 and arr[j][i][2] == 1):
                text+="\u2193"
            elif (arr[j][i][0] == 10 and arr[j][i][1] == 0 and arr[j][i][2] == 2):
                text+="\u2190"
            elif (arr[j][i][0] == 10 and arr[j][i][1] == 0 and arr[j][i][2] == 3):
                text+="\u2191"
            elif (arr[j][i][0] == 1 and arr[j][i][1] == 0 and arr[j][i][2] == 0):
                text+=" "
            elif (arr[j][i][0] == 4 and arr[j][i][1] == 4 and arr[j][i][2] == 2):
                text+="R"
            elif (arr[j][i][0] == 6 and arr[j][i][1] == 4 and arr[j][i][2] == 0):
                text+="R"
            elif (arr[j][i][0] == 8 and arr[j][i][1] == 1 and arr[j][i][2] == 0):
                text+="A"
            else:
                text+= " "
        text+="\n"

    return(text)

def text_to_array(text):
    arr = np.zeros((8,8,3))
    j = 0
    k = 0
    for i, element in enumerate(text):
        if(element == '\n'):
            k+=1
            j = -1
        elif(element == '#'):
            arr[j][k][0] = 2
            arr[j][k][1] = 5
            arr[j][k][2] = 0
        elif(element == '@'):
            arr[j][k][0] = 10
            arr[j][k][1] = 0
        elif(element == 'A'):
            arr[j][k][0] = 8
            arr[j][k][1] = 1
            arr[j][k][2] = 0
        j+=1
    return arr

def similarity(state, final_state):
    print(final_state, state, "miaos")
    if(np.array_equal(final_state, state)):
        return 1
    return 0

def text_similarity(state, final_state):
    if not isinstance(state, str):
        state = array_into_text(state)
    if not isinstance(final_state, str):
        final_state = array_into_text(final_state)
    if(state == final_state):
        return 2
    return 0

def load_final_states(folder):
    states = []
    tensor_states = []
    for file_path in glob.glob(os.path.join(folder, "*.txt")):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            states.append(text_to_array(content))
            tensor_states.append(torch.tensor(np.transpose(text_to_array(content))).float())
            
    return states, tensor_states