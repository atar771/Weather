import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


secret = st.secrets["my_secret"]
st.text(f"my secret is {secret}, dont tell anyone")

st.markdown("""
# Title    
## Subtitle

- bullet 1
- bullet 2
- bullet 3

>Amazing Quote
""")

# Create a radio button widget for selecting the plot type
plot_type = st.radio("Which plot do you want to see?", ["Seaborn", "Plotly"])

# Load the dataset
df = sns.load_dataset("penguins")

if plot_type == "Seaborn":
    # Create a Seaborn scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=ax)
    st.pyplot(fig)
elif plot_type == "Plotly":
    # Create a Plotly scatter plot
    fig = px.scatter(
        df,
        x="flipper_length_mm",
        y="bill_length_mm",
        color="species",
        title="Penguins: Flipper Length vs Bill Length"
    )
    st.plotly_chart(fig)


##url ="https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"