import nashpy as nash
import numpy as np
import matplotlib.pyplot as plt

def get_population(number_of_strategies,size=50):
    population = np.random.randint(0, number_of_strategies, size)
    return population

def get_scores(population, opponents, game):
    return [(game[0][i,j], game[1][i,j]) for i,j in zip(population, opponents)]

def mutate(socres, population, opponents):
    mutated_population = []
    for score, strategy_pair in zip(socres, zip(population, opponents)):
        if score[1] >= score[0]:
            mutated_population.append(strategy_pair[1])
        else:
            mutated_population.append(strategy_pair[0])
    
    return np.array(mutated_population)

def evolve(game, size, generations):
    population = get_population(len(game[0]), size)
    opponents = get_population(len(game[0]), size)

    history = [population]

    for _ in range(generations):
        scores = get_scores(population, opponents, game)
        population = mutate(scores, population, opponents)
        opponents = get_population(len(game[0]), size)
        history.append(population)
    
    return history

def plot_line(history):
    list1, list2, list3 = [], [], []
    for data in history:
        _list = data.tolist()
        list1.append(_list.count(0))
        list2.append(_list.count(1))
        list3.append(_list.count(2))

    plt.plot(list1, label="0",color="blue")
    plt.plot(list2, label="1",color="orange")
    plt.plot(list3, label="2",color="green")
    plt.title("Random seed: 0")
    plt.legend()
    plt.show()

def start_test(seeds = 10):
    iterations = 15
    size = 5
    # 定义博弈矩阵
    td = (np.array([
                [2,4,4],
                [0,3,5],
                [0,1,4]]),
        np.array([
                [2,0,0],
                [4,3,1],
                [4,5,4]])
        )
    # print(list(game.support_enumeration()))  # 用support_enumeration计算纳什均衡点
    if seeds == 0:
        np.random.seed(seeds)
        population = get_population(3, 10)
        opponents = get_population(3, 10)
        scores = get_scores(population, opponents, td)
        history = evolve(td, size, iterations)
        plot_line(history)
    else:
        row = int(np.sqrt(seeds))
        col = int(seeds/row) + 1
        # fig, axs = plt.subplots(row, col, figsize=(15,9))
        for seed in range(seeds):
            np.random.seed(seed)
            population = get_population(3, 10)
            opponents = get_population(3, 10)
            scores = get_scores(population, opponents, td)
            history = evolve(td, size, iterations)
            list1, list2, list3 = [], [], []
            for data in history:
                _list = data.tolist()
                list1.append(_list.count(0))
                list2.append(_list.count(1))
                list3.append(_list.count(2))

            plt.subplot(row, col, seed + 1)  # 绘制多张图像
            plt.plot(list1, label="0",color="blue")
            plt.plot(list2, label="1",color="orange")
            plt.plot(list3, label="2",color="green")
            plt.title("Seeds:{}".format(seed + 1))
            plt.legend()
            plt.axis('off')

        plt.show()
            

    

if __name__ == "__main__":
    start_test()