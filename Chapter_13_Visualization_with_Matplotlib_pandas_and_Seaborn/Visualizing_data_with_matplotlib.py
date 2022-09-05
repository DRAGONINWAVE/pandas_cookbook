import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

alta = pd.read_csv(r'D:\python3.10\Pandas-Cookbook-master\data\alta-noaa-1980-2019.csv')
print(alta)

data = (alta
        .assign(DATE=pd.to_datetime(alta.DATE))
        .set_index('DATE')
        .loc['2018-09':'2019-08']
        .SNWD)
print(data)

blue = '#99ddee'
white = '#ffffff'
fig,ax= plt.subplots(figsize=(12,4),
                     linewidth=5,facecolor=blue)
ax.set_facecolor(blue)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='x',colors=white)
ax.tick_params(axis='y',colors=white)
ax.set_ylabel('Snow Depth (in)',color=white)
ax.set_title('2009-2010',color=white,fontweight='bold')
ax.fill_between(data.index,data,color=white)
fig.savefig('c13-alta1.png',dpi=300,facecolor=blue)

import matplotlib.dates as mdt

def plot_year(ax,data,years):
    ax.set_facecolor(blue)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='x',colors=white)
    ax.tick_params(axis='y',colors=white)
    ax.set_ylabel('Snow Depth (in)',color=white)
    ax.set_title(years,color=white,fontweight='bold')
    ax.fill_between(data.index,data,color=white)

years = range(2009,2019)
fig,axs = plt.subplots(ncols=2,nrows=int(len(years)/2),
                       figsize=(16,10),linewidth=5,facecolor=blue)

axs = axs.flatten()
max_val = None
max_data = None
max_ax = None
for i,y in enumerate(years):
    ax = axs[i]
    data = (alta
            .assign(DATE=pd.to_datetime(alta.DATE))
            .set_index('DATE')
            .loc[f'{y}-09':f'{y+1}-08']
            .SNWD
            )

    if max_val is None or max_val < data.max():
        max_val = data.max()
        max_data = data
        max_ax = ax
    ax.set_ylim(0,180)
    years = f'{y} - {y+1}'
    plot_year(ax,data,years)

max_ax.annotate(f'Max Snow {max_val}',
                xy=(mdt.date2num(max_data.idxmax()),max_val),
                color = white)

fig.suptitle('Alta Snowfall',color=white,fontweight='bold')
fig.tight_layout(rect=[0,0.03,1,0.95])
fig.savefig('c13-alta.png',dpi=300,facecolor=blue)

print(alta
      .assign(DATE=pd.to_datetime(alta.DATE))
      .set_index('DATE')
      .SNWD
      .to_frame()
      .assign(next=lambda df_:df_.SNWD.shift(-1),
              snwd_diff = lambda df_:df_.next-df_.SNWD)
      .pipe(lambda df_:df_[df_.snwd_diff.abs() > 50])
      )

def fix_gaps(ser,threshold=50):
    #'Replace values where the shift is > threshold with nan'
    mask = (ser
            .to_frame()
            .assign(next=lambda df_:df_.SNWD.shift(-1),
                    snwd_diff=lambda df_:df_.next-df_.SNWD)
            .pipe(lambda df_:df_.snwd_diff.abs() > threshold)
    )

    return ser.where(~mask,np.nan)

years = range(2009,2019)
for i,y in enumerate(years):
    ax = axs[i]
    data = (alta
            .assign(DATE=pd.to_datetime(alta.DATE))
            .set_index('DATE')
            .loc[f'{y}-09':f'{y+1}-08']
            .SNWD
            .pipe(fix_gaps)
            .interpolate()
            )

    if max_val is None or max_val < data.max():
        max_val = data.max()
        max_data = data
        max_ax = ax
    ax.set_ylim(0,180)
    years = f'{y}-{y+1}'
    plot_year(ax,data,years)

max_ax.annotate(f'Max Snow {max_val}',
                xy=(mdt.date2num(max_data.idxmax()),max_val),
                color = white)

fig.suptitle('Alta Snowfall',color=white,fontweight='bold')
fig.tight_layout(rect=[0,0.03,1,0.95])
fig.savefig('c13-alta4.png',dpi=300,facecolor=blue)