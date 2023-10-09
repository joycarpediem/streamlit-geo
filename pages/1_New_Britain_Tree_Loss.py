import streamlit as st
import leafmap.foliumap as leafmap
import os

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

# st.sidebar.title("About")
# st.sidebar.info(markdown)
# logo = "https://i.imgur.com/UbOXYAU.png"
# st.sidebar.image(logo)


st.title("Tree Loss , New Britain, Papua New Guinea")
def display_html_file(file_path):
    with open(file_path, 'r') as html_file:
        html_content = html_file.read()
    st.components.v1.html(html_content, height=600, scrolling=True)
# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Specify the relative path to your HTML file
html_file_relative_path = "../content/nbr-treeloss.html"
    
    # Calculate the absolute path to the HTML file
html_file_path = os.path.join(script_dir, html_file_relative_path)


display_html_file(html_file_path)

# col1, col2 = st.columns([4, 1])
# options = list(leafmap.basemaps.keys())
# index = options.index("OpenTopoMap")

# with col2:

#     basemap = st.selectbox("Select a basemap:", options, index)


# with col1:

#     m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
#     m.add_basemap(basemap)
#     m.to_streamlit(height=700)
