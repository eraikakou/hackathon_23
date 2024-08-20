
# Parse the Java code
tree = parser.parse(bytes(java_code, "utf8"))
root_node = tree.root_node

# Function to extract a simplified representation
def extract_simplified_representation(node):
    representation = ""
    imports = []
    used_classes = set()

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

            # Traverse method body for external class usage
            method_body = node.child_by_field_name("body")
            if method_body:
                for child in method_body.children:
                    traverse(child, depth + 4)

        elif node.type == "import_declaration":
            # Handle full import path
            import_path_node = node.child_by_field_name("path")
            if import_path_node:
                import_name = ""
                for child in import_path_node.children:
                    if child.is_named:
                        import_name += child.text.decode("utf-8") + "."
                import_name = import_name.rstrip(".")
                imports.append(import_name)
                representation += f"  - Import: {import_name}\n"
            else:
                representation += "  - Import: UnknownImport\n"

        elif node.type == "type_identifier" or node.type == "object_creation_expression":
            # Handle type usage or object creation
            class_name = node.text.decode("utf-8")
            used_classes.add(class_name)

        # Traverse children for potential nested structures
        for child in node.children:
            if child.is_named:  # Skip non-named nodes (e.g., semicolons, brackets)
                traverse(child, depth)

    traverse(root_node)

    # Identify dependencies that are not part of imports or Java standard library
    external_dependencies = used_classes - set(imports)

    representation += "\nExternal Dependencies:\n"
    for dependency in external_dependencies:
        representation += f"  - {dependency}\n"

    return representation

# Generate and print the simplified representation
simplified_representation = extract_simplified_representation(root_node)
print(simplified_representation)
