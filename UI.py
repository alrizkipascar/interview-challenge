import time
import streamlit as st
import numpy as np
import pandas as pd
from io import BytesIO
import simple_lead_ai
from simple_lead_ai import first_prompt,prompt_company_info

# Create download content
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# def convert_df_to_excel(df):
    
#     with pd.ExcelWriter("output.xlsx", engine='xlsxwriter') as writer:
#         return df.to_excel(writer, index=False, sheet_name='Sheet1')

def convert_df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    return output.getvalue()


def main():
    dataf = 0
    st.write("# Caprae ML intern challenge") 
    
    st.write("This is a simple Streamlit UI designed for this challenge. It demonstrates how the application processes data. The data must be uploaded in CSV or Excel format, and the first row should contain lead links.") 


    st.write("## First Step - Upload data")
    # Choose file type
    file_type = st.selectbox("Choose file type to download:", ["CSV", "Excel"])
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "json"])

    if uploaded_file is not None:
        first_prompt()
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            df = pd.read_json(uploaded_file)
        else:
            st.error("Unsupported file type")
            
        dataf = df
        headers = df.columns.tolist()
        headers = headers[1:]
        
        st.write("### Preview of Data:")
        st.dataframe(df)
        
        for i in range(len(dataf)):
            print(i)
            # dataf['column_name'] = df['column_name'].astype(str)
            row = dataf.iloc[i].tolist()
            for j in range(len(row)):
                if j == 0:
                    continue
                else:    
                    dataf.iloc[i, j] = prompt_company_info(dataf.iloc[i, 0],headers[j-1])
                    # Delay for 2 seconds
                    time.sleep(2)
        
        

        st.write("### Preview of Result:")
        st.dataframe(dataf)


        # Generate and show download button
        if file_type == "CSV":
            csv = convert_df_to_csv(dataf)
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name="result.csv",
                mime="text/csv"
            )
        elif file_type == "Excel":
            excel = convert_df_to_excel(dataf)
            st.download_button(
                label="📥 Download Excel",
                data=excel,
                file_name="result.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    
if __name__ == "__main__":
    # 
    main()