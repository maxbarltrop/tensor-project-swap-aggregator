from constants import SOL, USDC, USDT, JUP, ETH, ORANGE, RED, GREEN, ONE_OPTIMAL_SKIP, ZEROES, FOUR_SKIPS_A, FOUR_SKIPS_B, FOUR_SKIPS_C, FOUR_SKIPS_D
from classes import Node, Pair
import heapq


# return the best rates we can find for swapping token to all other tokens accross all exchanges
def getBestSwaps(token, exchanges):
    res = {}
    for exchange in exchanges:
        for swappable in exchange.market[token]:
            if (swappable not in res):
                res[swappable] = Pair(
                    exchange.market[token][swappable], exchange.name)
            elif (exchange.market[token][swappable] > res[swappable].rate):
                res[swappable] = Pair(
                    exchange.market[token][swappable], exchange.name)
    return res


# returns the best rate we can find for swapping token for targetToken
def getBestSwap(token, targetToken, exchanges):
    res = None
    for exchange in exchanges:
        if (res == None or exchange.market[token][targetToken] > res.rate):
            res = Pair(exchange.market[token][targetToken], exchange.name)
    return res


def printResult(paths, tokenA, tokenB):
    final = paths[tokenB]
    amount = final.amount
    output = []
    output.append([final.exchangeName, tokenB])
    token = final.previous
    while (token != tokenA):
        final = paths[final.previous]
        output.append([final.exchangeName, token])
        token = final.previous
    output.reverse()
    print(tokenA, end="")
    for stop in output:
        print(" --(" + stop[0] + ")-> " + stop[1], end="")
    print(", Total=" + str(round(amount, 2)))


# Finds an efficient route between tokenA and tokenB across the provided exchanges
# Returns the maximum quantity of tokenB that can be returned along this route
# Prints the route to stdouts
# With t Tokens across e Exchanges, the runtime becomes bound by O(t^2 * e)
def swapRoute(tokenA, tokenB, amount, exchanges):
    if (amount <= 0):
        return 0
    paths = {}

    depth_one_tokens = []
    depth_two_tokens = set()
    bestSwaps = getBestSwaps(token=tokenA, exchanges=exchanges)
    # first, let's initialize the maximum quantity of any token we can swap for tokenA
    for neighbourToken in bestSwaps:
        if (bestSwaps[neighbourToken].rate == 0):
            continue
        paths[neighbourToken] = Node(
            amount=amount *
            bestSwaps[neighbourToken].rate, previous=tokenA, exchangeName=bestSwaps[neighbourToken].exchangeName
        )
        heapq.heappush(depth_one_tokens,
                       (bestSwaps[neighbourToken].rate, neighbourToken))

    # Then let's extend the path length to 2, and update if we can find a higher quantity
    while (len(depth_one_tokens) > 0):
        token = heapq.heappop(depth_one_tokens)[1]
        if (token == tokenB or token in depth_two_tokens):
            continue
        curNode = paths[token]
        bestSwaps = getBestSwaps(token=token, exchanges=exchanges)
        for neighbourToken in bestSwaps:
            if (neighbourToken in depth_two_tokens):
                continue
            rate = bestSwaps[neighbourToken].rate
            if (neighbourToken == tokenA or rate == 0):
                continue
            tempMaximumQuantity = curNode.amount * rate
            if (neighbourToken not in paths):
                paths[neighbourToken] = Node(
                    amount=tempMaximumQuantity, previous=token, exchangeName=bestSwaps[neighbourToken].exchangeName)
                depth_two_tokens.add(neighbourToken)
            elif (tempMaximumQuantity > paths[neighbourToken].amount):
                paths[neighbourToken].update(
                    amount=tempMaximumQuantity, previous=token, exchangeName=bestSwaps[neighbourToken].exchangeName)
                depth_two_tokens.add(neighbourToken)

  # look at all of our length 2 paths, and see if we can swap that token for tokenB
    while (len(depth_two_tokens) > 0):
        token = depth_two_tokens.pop()
        if (token == tokenB):
            continue
        bestSwap = getBestSwap(
            token=token, targetToken=tokenB, exchanges=exchanges)
        if (bestSwap == None):
            continue
        tempMaximumQuantity = paths[token].amount * bestSwap.rate
        if tempMaximumQuantity == 0:
            continue
        if (tokenB not in paths):
            paths[tokenB] = Node(
                amount=tempMaximumQuantity, previous=token, exchangeName=bestSwap.exchangeName)
        elif (tempMaximumQuantity > paths[tokenB].amount):
            paths[tokenB].update(amount=tempMaximumQuantity,
                                 previous=token, exchangeName=bestSwap.exchangeName)
    if (tokenB not in paths):
        print("Not possible.")
        return 0
    printResult(paths, tokenA, tokenB)
    return paths[tokenB].amount


def test(tokenA, tokenB, amount, exchanges, expectedTotal):
    actual = swapRoute(tokenA, tokenB, amount, exchanges)
    if (round(actual, 0) == round(expectedTotal, 0)):
        print("Pass")
    else:
        print("Fail")


test(SOL, USDC, 100, [ORANGE, RED, GREEN], 495)
test(SOL, ETH, 100, [ORANGE, RED], 330)
test(JUP, USDC, 100, [RED], 562)
test(SOL, JUP, 100, [ONE_OPTIMAL_SKIP, RED, GREEN], 10000)
test(SOL, ETH, 100, [ZEROES], 0)
test(SOL, ETH, 100, [ONE_OPTIMAL_SKIP, GREEN], 20750)  # !!
test(SOL, ETH, -1, [RED], 0)
test(SOL, ETH, 0, [GREEN], 0)
test(SOL, USDT, 100, [FOUR_SKIPS_A, FOUR_SKIPS_B,
     FOUR_SKIPS_C, FOUR_SKIPS_D], 0)
