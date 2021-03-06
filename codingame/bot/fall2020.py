"""
https://www.codingame.com/multiplayer/bot-programming/fall-challenge-2020
"""
import sys

# how many turns we will spend on learning spells
LEARN_TURNS = 7


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# Depth-first search algorithm


def dfs(graph, move):
    for node in graph:
        if not node["discovered"]:
            explore(node, move)
    pass


def explore(node, move):
    if len(node["links"]) != 0:
        node["discovered"] = True
        for link in node["links"]:
            explore(link, move)
    elif not node["discovered"]:
        node["discovered"] = True
        move.append(node)
    pass


def init_node(node):
    node["best"] = 0
    node["discovered"] = False
    node["links"] = []
    if "repeatable" not in node:
        node["repeatable"] = 0
    return node


def node_sum(node):
    return node["d0"] + node["d1"] + node["d2"] + node["d3"]

# create graph


def graph(orders, inventory, spells):
    need = set()

    for order in orders:
        for key in ["d0", "d1", "d2", "d3"]:
            if inventory[key] + order[key] < 0:
                need.add(key)

        if len(need) > 0:
            key = need.pop()
            for i in spells:
                if i[key] > 0 and not order["discovered"]:
                    order["links"].append(i)
                    i["discovered"] = True
            if len(order["links"]) != 0:
                graph(order["links"], inventory, spells)

    for i in spells:
        i["discovered"] = False
    for i in orders:
        i["discovered"] = False
    pass


def learn_first_spell(spells):
    print("LEARN %s" % spells[0]["id"])


def make_step(turn):
    orders = []
    spells = []
    spell_book = []
    best_move = []

    action_count = int(input())
    for i in range(action_count):
        action_id, action_type, delta_0, delta_1, delta_2, delta_3, price, tome_index, tax_count, castable, repeatable = input().split()
        action_id = int(action_id)
        delta_0 = int(delta_0)
        delta_1 = int(delta_1)
        delta_2 = int(delta_2)
        delta_3 = int(delta_3)
        price = int(price)
        tome_index = int(tome_index)
        tax_count = int(tax_count)
        castable = int(castable)
        repeatable = int(repeatable)

        if action_type == "BREW":
            node = init_node({
                "d0": delta_0,
                "d1": delta_1,
                "d2": delta_2,
                "d3": delta_3,
                "id": action_id,
                "price": price,
            })
            orders.append(node)

        if action_type == "CAST":
            node = init_node({
                "d0": delta_0,
                "d1": delta_1,
                "d2": delta_2,
                "d3": delta_3,
                "id": action_id,
                "castable": castable,
                "repeatable": repeatable,
            })
            spells.append(node)

        if action_type == "LEARN":
            node = init_node({
                "d0": delta_0,
                "d1": delta_1,
                "d2": delta_2,
                "d3": delta_3,
                "id": action_id,
                "castable": castable,
                "repeatable": repeatable,
                "taxcount": tax_count,
                "taxindex": tome_index,
            })
            spell_book.append(node)
    pass
    inv = list(map(int, input().split()))
    inv = init_node({
        "d0": inv[0],
        "d1": inv[1],
        "d2": inv[2],
        "d3": inv[3],
        "score": inv[4],
    })
    # not used right now
    opp_inv = map(int, input().split())

    # cast first spell on first move to have more d0
    # if turn == 1:
    #     for spl in spells:
    #         if spl["d0"] == 2 and spl["d1"] == 0 and spl["d2"] == 0 and spl["d3"] == 0:
    #             print(f'CAST {spl["id"]}')
    #             return

    # brew if we can
    for od in orders:
        if inv["d0"] + od["d0"] >= 0 and inv["d1"] + od["d1"] >= 0 and inv["d2"] + od["d2"] >= 0 and inv["d3"] + od["d3"] >= 0:
            print(f'BREW {od["id"]}')
            return

    # try to learn spell without consumable inv first
    for als in spell_book:
        if als["d0"] >= 0 and als["d1"] >= 0 and als["d2"] >= 0 and als["d3"] >= 0 and als["taxindex"] <= inv["d0"]:
            print(f'LEARN {als["id"]}')
            return

    # learn spells at the early stage of the game
    if turn <= LEARN_TURNS:
        learn_first_spell(spell_book)
        return

    # for ao in orders:
    graph(orders, inv, spells)
    dfs(orders, best_move)

    # default action if we don't have best move
    if len(best_move) == 0:
        learn_first_spell(spell_book)
        return

    for bm in best_move:
        if bm["d0"] + inv["d0"] < 0 or bm["d1"] + inv["d1"] < 0 or bm["d2"] + inv["d2"] < 0 or \
                bm["d3"] + inv["d3"] < 0 or node_sum(bm) + node_sum(inv) > 10:
            bm["best"] -= 999

        if bm["castable"] == 1:
            bm["best"] += 5
        if bm["d0"] >= 0:
            bm["best"] += 1
        if bm["d1"] >= 0:
            bm["best"] += 2
        if bm["d2"] >= 0:
            bm["best"] += 3
        if bm["d3"] >= 0:
            bm["best"] += 4
    best_move.sort(key=lambda x: x["best"])

    if best_move[-1]["castable"] == 0:
        print('REST')
        return

    # log("Best move: %s" % best_move[-1])
    k = 1
    if best_move[-1]["repeatable"] == 1:
        k = 0
        while node_sum(best_move[-1]) + node_sum(inv) <= 10 and \
                best_move[-1]["d0"] + inv["d0"] >= 0 and \
                best_move[-1]["d1"] + inv["d1"] >= 0 and \
                best_move[-1]["d2"] + inv["d2"] >= 0 and \
                best_move[-1]["d3"] + inv["d3"] >= 0:
            # log(f"Inv {k}: {inv}")
            inv["d0"] += best_move[-1]["d0"]
            inv["d1"] += best_move[-1]["d1"]
            inv["d2"] += best_move[-1]["d2"]
            inv["d3"] += best_move[-1]["d3"]
            k += 1
    # log(f"Inv {k}: {inv}")
    if k > 1:
        log(f"Repeated {k}")
    print(f'CAST {best_move[-1]["id"]} {k}')
    return


def main():
    turn = 0

    while True:
        turn += 1
        make_step(turn)


if __name__ == "__main__":
    main()
