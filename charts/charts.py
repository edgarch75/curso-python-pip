import matplotlib.pyplot as plt
def generate_pie():
    labels = ['A','B','C']
    values = [150,35,60]
    fig , ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie.png')
    plt.close()