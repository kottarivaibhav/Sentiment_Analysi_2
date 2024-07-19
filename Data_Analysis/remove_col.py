import pandas as pd

def remove_column_from_csv(input_file, output_file, column_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Check if the column exists in the DataFrame
    if column_name in df.columns:
        # Drop the specified column
        df.drop(column_name, axis=1, inplace=True)
    else:
        print(f"Column '{column_name}' does not exist in the CSV file.")
        return
    
    # Write the DataFrame back to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Column '{column_name}' has been removed and the new CSV is saved as '{output_file}'.")

# Example usage
input_file = './mobile_phone_.csv'
output_file = 'output.csv'
column_name = 'sentiments'

remove_column_from_csv(input_file, output_file, column_name)
