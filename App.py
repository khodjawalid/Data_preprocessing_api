import re
import streamlit as st

def update_netlist(netlist_content):
    """Removes '$', 'wc', and 'gausssigma' from a netlist string.

    Args:
        netlist_content: The input netlist string.

    Returns:
        The updated netlist string.
    """

    updated_netlist = netlist_content.replace('$', '')
    updated_netlist = re.sub(r"[Ww][Cc]", "", updated_netlist)  # Case-insensitive removal of wc
    updated_netlist = updated_netlist.replace('gausssigma', '')
    
    lines = updated_netlist.splitlines()
    updated_lines = []
    for line in lines:
        if not (line.startswith(".options") or line.startswith("+") or line.startswith(".sensmeas") or line.startswith(".GRAPH")):
            updated_lines.append(line)
    
    return "\n".join(updated_lines)
    


st.title('Modelwise input processing tool inference')

st.subheader('Upload your Simetrix netlist')

with st.sidebar : 
    st.header('Data requirements')
    st.caption('A SIMetrix netlist file is required. The preprocessor will automatically remove or modify certain directives (e.g., .GRAPH, .sensmeas) to ensure compatibility with the target simulator. Please review the preprocessed netlist before use')
    with st.expander('Data format') : 
        st.markdown('Netlist file')
        
    st.divider()
    st.caption("<p style = 'text-align:center' > Made by Walid </p>", unsafe_allow_html = True)


if 'clicked' not in st.session_state : 
    st.session_state.clicked = {1:False}

def clicked(button) : 
    st.session_state.clicked[button] = True 

st.button("Upload", on_click = clicked, args = [1])

if st.session_state.clicked[1] : 
    uploaded_file = st.file_uploader("Choose a file", type = 'net')
    
    if uploaded_file is not None : 
        netlist_content = uploaded_file.read().decode("utf-8")

        st.write('File uploaded successfully')
        
        updated_netlist = update_netlist(netlist_content)

        st.download_button('Download new data', updated_netlist, 'updated_netlist.net','text/net', key = 'download-net')
        
        
        