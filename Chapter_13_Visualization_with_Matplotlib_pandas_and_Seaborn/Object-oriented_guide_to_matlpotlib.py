import matplotlib.pyplot as plt
x = [-3,5,7]
y = [10,2,5]
fig = plt.figure(figsize=(15,3))
plt.plot(x,y)
plt.xlim(0,10)
plt.ylim(0,10)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot')
plt.suptitle('Figure Title',size=20,y=1.03)
fig.savefig('c13-fig1.png',dpi=300,bbox_inches='tight')

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from IPython.core.display import display
fig = Figure(figsize=(15,3))
FigureCanvas(fig)
ax = fig.add_subplot(111)
ax.plot(x,y)
ax.set_xlim(0,10)
ax.set_ylim(-3,8)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Line Plot')
fig.suptitle('Figure Title',size=20,y=1.03)
display(fig)
fig.savefig('c13-fig2.png',dpi=300,bbox_inches='tight')

fig,ax = plt.subplots(nrows=1,ncols=1)
fig.savefig('c13-step2.png',dpi=300)
print(type(fig))
print(type(ax))

print(fig.get_size_inches())
print(fig.set_size_inches(14,4))
fig.savefig('c13-step4.png',dpi=300)
print(fig)
print(fig.axes)
print(fig.axes[0] is ax)
fig.set_facecolor('.7')
ax.set_facecolor('.5')
fig.savefig('c13-step7.png',dpi=300,facecolor='.7')
print(fig)
ax_children = ax.get_children()
print(ax_children)
spines = ax.spines
print(spines)

spine_left = spines['left']
spine_left.set_position(('outward',-100))
spine_bottom = spines['bottom']
spine_bottom.set_visible(False)
fig.savefig('c13-step10.png',dpi=300,facecolor='.7')

#ax.xaxis.grid(True,which='major',linewidth=2,
#              color='black',linestyle='--')
#ax.xaxis.set_ticks([.2,.4,.55,.93])
#ax.xaxis.set_label_text('X Axis',family='Verdana',fontsize=15)
#ax.set_ylabel('Y Axis',family='Gotham',fontsize=20)
#ax.set_yticks([.1,.9])
#ax.set_yticklabels(['point 1','point 9'],rotation=45)
#fig.savefig('c13-step11.png',dpi=300,facecolor='.7')

plot_objects = plt.subplots(nrows=1,ncols=1)
print(type(plot_objects))
fig = plot_objects[0]
ax = plot_objects[1]
fig.savefig('c13-1-works1.png',dpi=300)

fig,axs = plt.subplots(2,4)
fig.savefig('c13-1-works.png',dpi=300)