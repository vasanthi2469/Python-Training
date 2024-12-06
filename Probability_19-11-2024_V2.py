import matplotlib.pyplot as plt
from matplotlib_venn import venn2
 
# Define the sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
 
# Create a Venn diagram
venn = venn2([set1, set2], ('Set 1', 'Set 2'))
 
# Customize the diagram (optional)
venn.get_label_by_id('10').set_text('Only Set 1')
venn.get_label_by_id('01').set_text('Only Set 2')
venn.get_label_by_id('11').set_text('Both Sets')
 
# Display the diagram
plt.title("Venn Diagram of Two Sets")
plt.show()
