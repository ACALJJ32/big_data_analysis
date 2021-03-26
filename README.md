## 作业1 : ./ft1
#### 参考作业链接，重新做了旅行者困境问题
#### 函数的定义和之前一样不变，只重新约定了参数，并写了plot函数
#### 定义博弈矩阵
```
td = (np.array([
                [2,4,4],
                [0,3,5],
                [0,1,4]]),
        np.array([
                [2,0,0],
                [4,3,1],
                [4,5,4]])
        )
```
#### 定义随机人数，以及他们会随机选择的策略
```
def get_population(number_of_strategies,size=50):
    population = np.random.randint(0, number_of_strategies, size)
    return population
```
#### 定义得分函数
```
def get_scores(population, opponents, game):
    return [(game[0][i,j], game[1][i,j]) for i,j in zip(population, opponents)]
```
#### 定义mutate函数，将博弈过程中的最优策略记录下来
```
def mutate(socres, population, opponents):
    mutated_population = []
    for score, strategy_pair in zip(socres, zip(population, opponents)):
        if score[1] >= score[0]:
            mutated_population.append(strategy_pair[1])
        else:
            mutated_population.append(strategy_pair[0])
    return np.array(mutated_population)
```
#### 演化过程也参考原文不做改变，定义绘图函数
```
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
    plt.grid('on')
    plt.show()
```
#### 当然，如果想要生成多种随机种子的情况，可以在plot_line的基础上改写。得到的实验结果如下：
![Alt text](https://img-blog.csdnimg.cn/20210325165536821.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzMDMwMA==,size_16,color_FFFFFF,t_70#pic_center)
![Alt text](https://img-blog.csdnimg.cn/20210325165725305.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzMDMwMA==,size_16,color_FFFFFF,t_70#pic_center)
#### 可以看到初始化不同的种子，图像会有一些变化，但是随着迭代次数的增加，不论是哪一种初始化的随机过程，都会达到相同的稳定过程。
#### 参考链接：https://cloud.tencent.com/developer/article/1182756?from=information.detail.%E5%8D%9A%E5%BC%88%E8%AE%BA%20python
## 作业2 : ./ft1
#### 用shap解释机器学习模型xgboost
#### 首先安装shap和xgboost
```
import xgboost
import shap
```
#### 使用的数据集是波士顿房价数据
#### 绘制图像，下图展示的是各种特征对最终的输出值贡献的大小
![Alt text](https://img-blog.csdnimg.cn/20210326130727193.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzMDMwMA==,size_16,color_FFFFFF,t_70#pic_center)
#### 下图是针对单个数据的解释说明，比如RM(一栋房子中的平均房间数)这一指标，将其与RAD(告诉公路可达性指标)进行交互，红色的代表sharp贡献值很高。
![Alt text](https://img-blog.csdnimg.cn/20210326135238529.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzMDMwMA==,size_16,color_FFFFFF,t_70#pic_center)
#### 
![Alt text](https://img-blog.csdnimg.cn/20210326135429807.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzMDMwMA==,size_16,color_FFFFFF,t_70#pic_center)
#### 我们也可以取每个特征的SHAP值的绝对值的平均值来得到一个标准的条形图(为多类输出产生堆叠的条形图)。
![Alt text](https://img-blog.csdnimg.cn/20210326135552891.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjEzMDMwMA==,size_16,color_FFFFFF,t_70#pic_center)

#### 参考链接：https://github.com/slundberg/shap

