import re

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
    
    



# Example usage (assuming you have the netlist content in a variable)
with open("design.net", "r") as f:
    netlist_content = f.read()

updated_netlist = update_netlist(netlist_content)
print(updated_netlist)

# To save to a new file:
with open("updated_netlist.net", "w") as f:
    f.write(updated_netlist)