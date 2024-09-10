from enum import Enum
from classes import Exchange

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}


SOL = "SOL"
USDC = "USDC"
JUP = "JUP"
ETH = "ETH"
USDT = "USDT"


ORANGE = Exchange("ORANGE", {
    SOL: {USDC: 1.7, JUP: 1.1, ETH: 1, USDT: 1},
    USDC: {SOL: 0.4, JUP: 1, ETH: 1, USDT: 1},
    JUP: {USDC: 1.1, SOL: 1, ETH: 1, USDT: 1.1},
    ETH: {USDC: 1, JUP: 1, SOL: 1, USDT: 1},
    USDT: {USDC: 1, JUP: 0.9, ETH: 1, SOL: 1}
})

RED = Exchange("RED", {
    SOL: {USDC: 1.8, JUP: 0.4, ETH: 1.5, USDT: 1.2},
    USDC: {SOL: 0.56, JUP: 0.22, ETH: 0.67, USDT: 0.83},
    JUP: {USDC: 2.5, SOL: 2.5, ETH: 3.0, USDT: 2.0},
    ETH: {USDC: 1.5, JUP: 0.33, SOL: 0.67, USDT: 1.0},
    USDT: {USDC: 1.2, JUP: 0.5, ETH: 1.0, SOL: 0.83}
})

GREEN = Exchange("GREEN", {
    SOL: {USDC: 1.5, JUP: 0.6, ETH: 1.2, USDT: 1.0},
    USDC: {SOL: 0.67, JUP: 0.4, ETH: 0.83, USDT: 0.67},
    JUP: {USDC: 2.5, SOL: 1.67, ETH: 2.0, USDT: 1.67},
    ETH: {USDC: 1.2, JUP: 0.5, SOL: 0.83, USDT: 1.0},
    USDT: {USDC: 1.0, JUP: 0.6, ETH: 1.0, SOL: 1.2}
})

ONE_OPTIMAL_SKIP = Exchange("ONE_OPTIMAL_SKIP", {
    SOL: {USDC: 100, JUP: 100, ETH: 100, USDT: 100},
    USDC: {SOL: 0, JUP: 0, ETH: 0, USDT: 0},
    JUP: {USDC: 0, SOL: 0, ETH: 0, USDT: 0},
    ETH: {USDC: 0, JUP: 0, SOL: 0, USDT: 0},
    USDT: {USDC: 0, JUP: 0, ETH: 0, SOL: 0}
})


ZEROES = Exchange("ZEROES", {
    SOL: {USDC: 0, JUP: 0, ETH: 0, USDT: 0},
    USDC: {SOL: 0, JUP: 0, ETH: 0, USDT: 0},
    JUP: {USDC: 0, SOL: 0, ETH: 0, USDT: 0},
    ETH: {USDC: 0, JUP: 0, SOL: 0, USDT: 0},
    USDT: {USDC: 0, JUP: 0, ETH: 0, SOL: 0}
})

FOUR_SKIPS_A = Exchange("ZEROES", {
    SOL: {USDC: 1, JUP: 0, ETH: 0, USDT: 0},
    USDC: {SOL: 0, JUP: 0, ETH: 0, USDT: 0},
    JUP: {USDC: 0, SOL: 0, ETH: 0, USDT: 0},
    ETH: {USDC: 0, JUP: 0, SOL: 0, USDT: 0},
    USDT: {USDC: 0, JUP: 0, ETH: 0, SOL: 0}
})

FOUR_SKIPS_B = Exchange("ZEROES", {
    SOL: {USDC: 1, JUP: 0, ETH: 0, USDT: 0},
    USDC: {SOL: 0, JUP: 1, ETH: 0, USDT: 0},
    JUP: {USDC: 0, SOL: 0, ETH: 0, USDT: 0},
    ETH: {USDC: 0, JUP: 0, SOL: 0, USDT: 0},
    USDT: {USDC: 0, JUP: 0, ETH: 0, SOL: 0}
})

FOUR_SKIPS_C = Exchange("ZEROES", {
    SOL: {USDC: 1, JUP: 0, ETH: 0, USDT: 0},
    USDC: {SOL: 0, JUP: 0, ETH: 0, USDT: 0},
    JUP: {USDC: 0, SOL: 0, ETH: 1, USDT: 0},
    ETH: {USDC: 0, JUP: 0, SOL: 0, USDT: 0},
    USDT: {USDC: 0, JUP: 0, ETH: 0, SOL: 0}
})

FOUR_SKIPS_D = Exchange("ZEROES", {
    SOL: {USDC: 1, JUP: 0, ETH: 0, USDT: 0},
    USDC: {SOL: 0, JUP: 0, ETH: 0, USDT: 0},
    JUP: {USDC: 0, SOL: 0, ETH: 0, USDT: 0},
    ETH: {USDC: 0, JUP: 0, SOL: 0, USDT: 1},
    USDT: {USDC: 0, JUP: 0, ETH: 0, SOL: 0}
})
