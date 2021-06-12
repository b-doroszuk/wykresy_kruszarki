import matplotlib.pyplot as plt



fig = plt.figure(figsize=(7, 6))
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

plt.plot([1,1], [2, 2], [3,3], [4,4], [5,5], [6,6], [7,7], color='green', marker='o')

#plt.show()


a  =[1,2,3,4,5]
print(len(a))
print(a[len(a)-1])