#shows components of given python package
import importlib
import inspect

def list_module_components(module_name):
    try:
        # Attempt to import the module
        module = importlib.import_module(module_name)
        print(f"Successfully imported {module_name}")
        
        # Get all attributes of the module using dir()
        print(f"\nComponents of {module_name} (via dir()):")
        for attr in dir(module):
            print(f" - {attr}")
        
        # Use inspect to get more detailed information
        print(f"\nDetailed components of {module_name} (via inspect):")
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                print(f" - Class: {name}")
            elif inspect.isfunction(obj):
                print(f" - Function: {name}")
            elif inspect.ismodule(obj):
                print(f" - Submodule: {name}")
            else:
                print(f" - Attribute: {name} (Type: {type(obj).__name__})")

    except ImportError as e:
        print(f"Failed to import {module_name}: {e}")
        print("Troubleshooting suggestions:")
        print("1. Ensure the module is installed: `pip install uagents-adapter` or `uv pip install uagents-adapter`")
        print("2. Check for typos in the module name or component name.")
        print("3. Verify the module version supports 'A2ARegisterTool'.")
        print("4. Check for circular imports in your code.")
        print("5. Ensure you're using the correct Python environment.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    module_name = "uagents_adapter"
    list_module_components(module_name)
