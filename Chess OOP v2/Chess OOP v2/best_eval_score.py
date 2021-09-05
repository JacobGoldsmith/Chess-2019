def best_eval_score(histogram, color):
        highest = -1004
        highest_index = None
        lowest = 1004
        lowest_index = None
        if color == 'white':
            for i in range(len(histogram)):
                if isinstance(histogram[i], str):
                    continue
                elif isinstance(histogram[i], list):
                    for j in range(len(histogram[i])):
                        if isinstance(histogram[i][j], str):
                            continue
                        elif histogram[i][j] > highest:
                            highest = histogram[i][j]
                            highest_index = [i, j]
                elif isinstance(histogram[i], int):
                    if histogram[i]>=highest:
                        highest = histogram[i]
            return [highest, highest_index]
        if color == 'black':
            for i in range(len(histogram)):
                if isinstance(histogram[i], str):
                    continue
                elif isinstance(histogram[i], list):
                    for j in range(len(histogram[i])):
                        if isinstance(histogram[i][j], str):
                            continue
                        elif histogram[i][j] < lowest:
                            lowest = histogram[i][j]
                            lowest_index = [i, j]
                elif isinstance(histogram[i], int):
                    if histogram[i]<=lowest:
                        lowest = histogram[i]
            return [lowest, lowest_index]
