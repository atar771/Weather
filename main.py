import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


st.markdown("""

# Title    
## Subtitle

- bullet 1
- bullet 2
- bullet 3

>Amazing Quote

""")

st.radio("witch dessert is best? " , ["Cake", "Ice cream", "pie"])

df = sns.load_dataset("pengiuns")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="flipper_length_mm", y="bill_length_mm", hue="species"
                , ax=ax)
st.pyplot(fig)
