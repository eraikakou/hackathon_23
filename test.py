
# Parse the Java code
tree = parser.parse(bytes(java_code, "utf8"))
root_node = tree.root_node

# Function to extract a simplified representation
def extract_simplified_representation(node):
    representation = ""

    def traverse(node, depth=0):
        nonlocal representation

        if node.type == "class_declaration":
            class_name_node = node.child_by_field_name("name")
            class_name = class_name_node.text.decode("utf-8") if class_name_node else "UnknownClass"
            representation += f"Class: {class_name}\n"

            # Traverse class body
            class_body = node.child_by_field_name("body")
            if class_body:
                for child in class_body.children:
                    traverse(child, depth + 2)

        elif node.type == "method_declaration":
            method_name_node = node.child_by_field_name("name")
            parameters_node = node.child_by_field_name("parameters")
            return_type_node = node.child_by_field_name("return_type")
            
            method_name = method_name_node.text.decode("utf-8") if method_name_node else "UnknownMethod"
            return_type = return_type_node.text.decode("utf-8") if return_type_node else "void"
            
            # Extract parameter list if available
            param_list = ""
            if parameters_node:
                param_list = ", ".join(
                    [param.text.decode("utf-8") for param in parameters_node.children if param.is_named]
                )
                
            representation += f"{' ' * depth}- Method: {method_name}({param_list}) -> {return_type}\n"

        elif node.type == "import_declaration":
            import_name_node = node.child_by_field_name("path")
            import_name = import_name_node.text.decode("utf-8") if import_name_node else "UnknownImport"
            representation += f"  - Import: {import_name}\n"

        # Traverse children for potential nested structures
        for child in node.children:
            if child.is_named:  # Skip non-named nodes (e.g., semicolons, brackets)
                traverse(child, depth)

    traverse(root_node)
    return representation

# Generate and print the simplified representation
simplified_representation = extract_simplified_representation(root_node)
print(simplified_representation)
