def scope():
    restaurant = {
        "kitchen": {"A1": 1, "A3": 1.5},
        "A1": {"A3": 0.5, "A2": 1.75, "kitchen": 1},
        "A2": {"A1": 1.75, "A4": 0.5},
        "A3": {"kitchen": 1.5, "A1": 0.5, "A4": 1.75, "E3": 2.5, "E4": 2},
        "A4": {"A2": 0.5, "A3": 1.75, "D3": 3.5, "D4": 3, "B3": 2, "B4": 2.5},

        "B1": {"B2": 0.5, "B3": 1.75},
        "B2": {"B1": 0.5, "B4": 1.75},
        "B3": {"B1": 1.75, "B4": 0.5, "A4": 2, "D4": 2.5},
        "B4": {"B3": 0.5, "B2": 1.75, "C4": 1.5, "A4": 2.5},

        "C1": {"C2": 1, "C4": 1.75},
        "C2": {"C1": 1, "C6": 1, "C3": 1},
        "C3": {"C2": 1, "C8": 1.75},
        "C4": {"B4": 1.5, "C7": 0.5, "C1": 1.75},
        "C5": {"C6": 0.5, "C8": 0.5},
        "C6": {"C2": 1, "C5": 0.5, "C7": 0.5},
        "C7": {"C6": 0.5, "C4": 0.5},
        "C8": {"C5": 0.5, "D3": 1.5, "C3": 1.75},

        "D1": {"D2": 0.5, "D3": 1.75},
        "D2": {"D1": 0.5, "D4": 1.75},
        "D3": {"D1": 1.75, "D4": 0.5, "A4": 3.5, "C8": 1.5},
        "D4": {"D3": 0.5, "D2": 1.75, "B3": 2.5, "A4": 3},

        "E1": {"E2": 0.5, "E3": 1.75},
        "E2": {"E1": 0.5, "E4": 1.75},
        "E3": {"E4": 0.5, "E1": 1.75, "A3": 2.5},
        "E4": {"E3": 0.5, "E2": 1.75, "A3": 2},
    }

    all_path = []
    all_cost = 0

    cost = 0
    best_cost = 1000

    path = []
    best_path = []

    origin = "kitchen"
    destiny = ""

    def the_best_route(t_list):
        nonlocal destiny, path, all_path
        all_path.append(origin)
        while len(t_list) > 0:
            all_path += the_closest_table(t_list)
            t_list.remove(origin)
        destiny = "kitchen"
        search(origin)
        all_path += best_path

    def the_closest_table(t_list):
        nonlocal cost, best_cost, best_path, path, destiny, origin, all_cost
        closest_table = []
        closest_table_cost = 1000
        for t in t_list:
            destiny = t
            search(origin)
            if best_cost < closest_table_cost:
                closest_table_cost = best_cost
                closest_table = best_path
            reset()
        origin = closest_table[len(closest_table) - 1]
        all_cost += closest_table_cost
        return closest_table

    def search(table):
        nonlocal cost, best_cost, best_path, path
        if not is_best_route(table):
            t = restaurant.get(table)
            for key in t.keys():
                if key not in path:
                    path.append(key)
                    cost += t.get(key)
                    if cost < best_cost:
                        search(key)
                    path.pop()
                    cost -= t.get(key)

    def is_best_route(table):
        nonlocal cost, best_cost, best_path, path
        if table == destiny and cost < best_cost:
            best_cost = cost
            best_path = path.copy()
            return True
        return False

    def reset():
        nonlocal cost, best_cost, best_path, path
        cost = 0
        best_cost = 1000
        path = []
        best_path = []

    def input_tables():
        size = 0
        try:
            size = int(input("Introduce the number of tables: "))
            if size > 4 or size < 1:
                print("valor a de estar entre 1 i 4")
                input_tables()
        except ValueError:
            print("El valor ha de ser numeric")
            input_tables()

        return input_t(size)

    def input_t(size):
        tables = []
        table = ""
        for i in range(size):
            table = input("Introduce table" + str(i + 1) + ": ").capitalize()
            while table not in restaurant.keys():
                print("el valor no existeix")
                table = input("Introduce table" + str(i + 1) + ": ").capitalize()
            tables.append(table)
        return tables

    the_best_route(input_tables())
    print(all_path)
    print(all_cost + best_cost)


scope()