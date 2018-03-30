import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

# 特征工程构造特征方法：将数字1,2,3 ... 等构造特征（重要影响因素，对预测number, "fizz", "buzz", "fizzbuzz"有帮助的因素），构造为三个维度。
# 将每个输入的数，表示为一个特征数组（向量），这个特征数组有三个维度。
def feature_engineer(i):
#    return np.array([i % 3, i % 5, i % 15])
    return np.array([i % 3])


# 将需要预测的指标转换为数字方法：将数据的真实值（预测结果）number, "fizz", "buzz", "fizzbuzz"
# 分别对应转换为数字 3, 2, 1, 0，这样后续能被计算机处理
def construct_sample_label(i):
    # if   i % 15 == 0: return np.array([3])
    # elif i % 5  == 0: return np.array([2])
    # elif i % 3  == 0: return np.array([1])
    # else:             return np.array([0])
    # if   i % 15 == 0: return np.array([3])
    # elif i % 5  == 0: return np.array([2])
    if i % 3  == 0: return np.array([1])
    else:             return np.array([0])

#[1, 1] [2, 2] [3, fizz]
# 生成训练集和测试集数据：我们的面试题目标是预测 1 到 100的fizz buzz情况. 所以为了
# 更加公平的预测，不让分类预测器较早的知道要预测的数据的情况，
# 我们选取101到200这个范围的数作为我们的训练集和测试集。 
# Note: 语法说明。 for i in range(101, 200)代表Python中从for循环中遍历取值为i，并
# 赋值将i值输入到feature_engineer函数

#[x1, x2, x3, x4 ... x100]
#[y1, y2, y3, y4 ... y100]

训练集真题
x_train = np.array([feature_engineer(i) for i in range(101, 200)])
y_train = np.array([construct_sample_label(i) for i in range(101, 200)])

测试集期末考试试卷
x_test = np.array([feature_engineer(i) for i in range(1, 100)])
y_test = np.array([construct_sample_label(i) for i in range(1, 100)])

A =100 
y = 100 x
# 构造线性回归模型 Y = AX。这里的X是代表含有三个维度的数组[x1,x2,x3]，
regr = linear_model.LinearRegression()

# 使用训练集训练模型，训练的过程，就是搜索最优A的值的过程。最优咱们通过
# 均方差 = 根号下 (累加所有样本（真实值 - 预测值）^2) 来评价模型中A值选取的优劣
regr.fit(x_train, y_train)

# 使用测试集进行预测
y_pred = regr.predict(x_test)

# 使用均方差（mean squared error）评价模型，均方差越小，
# 代表模型越精准
print("Mean squared error (均方差-误差): %.2f"
      % mean_squared_error(y_test, y_pred))
