import pandas as pd
import matplotlib.pyplot as plt
try:
    df=pd.read_csv('Rakesh/linehospital.csv')
    cost_series=df['Bill']
    data_seris=df['Admission_date']
    print("\n original Bill Series:\n", cost_series)
    print("\n original Admission Date Series:\n", data_seris)
    print('\n Fill the missing Bill vaue with nedian before plotting ?(yes/no):')
    fill_confirm=imput().strip().lower()
    print("Convert Admission Date Series to datetime format?(yes/no):")
    data_format_confirm=input().strip().lower()
    if fill_confirm == 'yes':
        median_cost=cost_series.median()
        cleaned_cost_series=cost_series.fillna(median_cost)
        print("\n Cleaned Bill Series with median fill:\n", cleaned_cost_series)
    else:
        print('\n no changes to medical cost series')
    cleaned_date_series=pd.to_datetime(data_seris, errors='coerce') 
    if data_format_confirm == 'yes':
        display_date_series=cleaned_date_series
    plt.figure(figsize=(10, 5))
    plt.plot(cleaned_date_series, cleaned_cost_series, color='blue', linestyle='-', linewidth=2, marker='o', markerfacecolor='red')
    plt.title('Hospital Bill Over Time')
    plt.xlabel('Admission Date')    
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    if fill_confirm == 'yes' or date_format_confirm == 'yes':
        df['Bill'] = cleaned_cost_series
        df['Admission_date'] = display_dates if date_format_confirm == 'yes' else cleaned 

                                       