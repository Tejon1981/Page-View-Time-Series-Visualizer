import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"]=pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Clean data
_2_5_percentil = df["value"].quantile(0.025)
_97_5_percentil = df["value"].quantile(0.975)
df = df[(df["value"] >= _2_5_percentil) & (df["value"] <= _97_5_percentil)]
# print("Test:",int(df.count(numeric_only=True)))

####################################################################################

def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(figsize=(12,6))
    plt.plot(df.index, df["value"])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

####################################################################################

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    # Extraer el año y el mes del índice de fecha
    df['Year'] = df.index.year
    df['Month'] = df.index.month

    # Calcular el promedio de 'value' por año y por mes
    df_bar = df.pivot_table(values='value', index='Year', columns='Month', aggfunc='mean')
    month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    # month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_bar = df_bar.rename(columns=month_names)

    # Draw bar plot
    fig,ax = plt.subplots(figsize=(16, 8))
    df_bar.plot(kind='bar', ax=plt.gca())
    plt.title('Average Page Views by Month (Grouped by Year)', fontsize=16)
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Average Page Views', fontsize=14)
    plt.xticks(rotation=90)
    plt.legend(title='Months')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

####################################################################################

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,(ax1, ax2)= plt.subplots(1, 2, figsize=(17, 8))
    view_ticks=[n for n in range(0,210000,20000)]
    
    # Left plot
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df_box['year'], y="value", data=df_box)
    plt.title('Year-wise Box Plot (Trend)', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Page Views', fontsize=14)
    plt.ylim(0, 200000)
    plt.yticks(view_ticks)
    
    # Right plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df_box['month'], y='value', data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.title('Month-wise Box Plot (Seasonality)', fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Page Views', fontsize=14)
    plt.ylim(0, 200000)
    plt.tight_layout()
    plt.yticks(view_ticks)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

# Rapid check
# draw_line_plot()
# draw_bar_plot()
# draw_box_plot()

print("\"int(time_series_visualizer.df.count(numeric_only=True))\" is not a valid code line in test_module.py")