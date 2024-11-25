import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as anm

def setup_plot_styles(ax):
    # Customize axis styles
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='y', which='both', left=False)
    ax.set_title('Top 15 Countries with Highest Population', fontsize=16, pad=20)  # Add padding to title
    ax.set_xlabel('Population (in millions)', fontsize=14, labelpad=10)  # Add padding to x-label
    ax.set_ylabel('Country', fontsize=14, labelpad=10)  # Add padding to y-label
    ax.tick_params(axis='x', which='both', bottom=False)

def add_month_year_text(ax, year, month):
    # Add year and month dynamically
    month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month - 1]
    ax.text(0.95, 0.02, f'{month_name} {year}', transform=ax.transAxes, fontsize=14, ha='right')

def create_animation(df):
    # Get unique frames (year-month combinations)
    df['Frame'] = df['Time'] * 100 + df['Month']  # Create unique frame IDs (e.g., 195001 for Jan 1950)
    frames = sorted(df['Frame'].unique())
    fig, ax = plt.subplots(figsize=(12, 6))

    def animate(frame):
        ax.clear()  # Clear the previous frame
        # Extract year and month from the frame
        year = frame // 100
        month = frame % 100
        # Filter data for the current frame
        pop_data_frame = df[(df['Time'] == year) & (df['Month'] == month)]
        # Get the top 15 countries and sort for a clean bar chart
        top_countries = pop_data_frame.nlargest(15, 'Population').sort_values('Population', ascending=True)
        # Create the horizontal bar chart
        ax.barh(top_countries['Location'], top_countries['Population'])

        # Add population values as text on the bars
        for i, row in top_countries.iterrows():
            ax.text(row['Population'], row['Location'], f'{row["Population"]:,.0f} m', ha='right', va='center')  # Format population numbers with commas

        setup_plot_styles(ax)  # Apply custom plot styles
        add_month_year_text(ax, year, month)  # Add year and month text
        plt.subplots_adjust(left=0.2, right=0.9, top=0.85, bottom=0.15)  # Adjust subplot to prevent clipping

    # Create the animation
    anim = anm.FuncAnimation(fig, animate, frames=frames, interval=50)
    return anim

if __name__ == '__main__':
    # Load data
    df = pd.read_csv('./data/cleaned-data-monthly.csv')
    # Create animation
    anim = create_animation(df)

    # Show the animation
    plt.show()
