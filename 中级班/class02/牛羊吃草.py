# 牛牛和羊羊都很喜欢青草。今天他们决定玩青草游戏。
# 最初有一个装有n份青草的箱子,牛牛和羊羊依次进行,牛牛先开始。在每个回合中,每个
# 玩家必须吃一些箱子中的青草,所吃的青草份数必须是4的x次幂,比如1,4,16,64等等。
# 不能在箱子中吃到有效份数青草的玩家落败。假定牛牛和羊羊都是按照最佳方法进行游
# 戏,请输出胜利者的名字。

def Winner1(N):
    if N < 5:
        return "后手" if N == 0 or N == 2 else "先手"
    base = 1
    while base <= N:
        if Winner1(N - base) == "后手":
            return "先手"
        if base > N / 4:
            break
        base *= 4
    return "后手"


def Winner2(N):
    if N % 5 == 0 or N % 5 == 2:
        return "后手"
    else:
        return "先手"


if __name__ == "__main__":
    N = 66
    print(Winner1(N))
    print(Winner2(N))
    # print("-----------找规律---------")
    # for i in range(50):
    #     print(Winner1(i))
    # print("-------------------------")
