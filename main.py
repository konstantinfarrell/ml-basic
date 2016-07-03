

def linear_classifier(data, weight, bias):
    """
    Takes a list containing data, and a weight and bias, and
    returns a list of scores for the data.
    """
    result = list()
    for pt in data:
        result.append(weight * pt + bias)
    return result

def softmax(scores):
    """
    Takes a list of scores and returns a dictionary of score-probabilities.
    """
    total = sum(scores)
    return dict((score, score/total) for score in scores)

def one_hot_encode(softmax):
    """
    Takes a dictionary of score-probabilities and returns a one-hot encoded
    dictionary of probabilities.
    """
    encoded = dict()
    hot = max(softmax.values())
    for key, value in softmax.items():
        if value == hot:
            encoded[key] = 1
        else:
            encoded[key] = 0
    return encoded

def cross_entropy(softmax, one_hot_encoding):
    """
    Takes the softmax probabilities and one-hot encoding and
    determines the cross-entropy
    """
    total = 0
    for key in softmax:
        total += one_hot_encoding[key] * math.log10(softmax[key])
    return -1 * total


if __name__ == '__main__':
    scores = [1, 1.0, 1.3, 2, 2, 1.75, 1.5]
    softmax = softmax(scores)
    one_hot = one_hot_encode(softmax)
    entropy = cross_entropy(softmax, one_hot)

