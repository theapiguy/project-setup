import os


project_files = ['requirements.txt', '.env']

project_directories = {
 "configs": {
    "env": ['dev.env', 'staging.env', 'live.env']
 },
 "docs": [],
 "src": ['main.py', 'utils.py'],
 "tests": ['test_']
}

def create_directory(dir_name):
    print(f"Creating {dir_name}")
    try:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            return "Success"
    except:
        print(f"Error creating {dir_name}")
        return "Failure"
        
        
def create_file(file_name):
    print(f"Creating {file_name}")
    with open(file_name, "w") as f:
        f.write("#  Created by project-setup.py")
        

if __name__ == '__main__':
    print("Starting Script")
    #  Ask for the project name
    project_name = input("Enter the project name with dashes:  ")
    project_name_safe = project_name.replace("-", "_")
    main_path = f"./{project_name}"
    status = create_directory(main_path)
    if status == 'Failure':
        exit(-1)
        
    #  Create the top level files - requirements.txt, .env
    for the_file in project_files:
        temp_file = os.path.join(main_path, the_file)
        create_file(temp_file)
        
    #  Now create directories within the project - configs, docs, src, tests
    for key, val in project_directories.items():
        temp_file = os.path.join(main_path, key)
        status = create_directory(temp_file)
        if status == 'Failure':
            exit(-1)
            
        if type(val) == dict:
            #  We have another directory to create
            for s_key, s_val in val.items():
                temp_file = os.path.join(main_path, key, s_key)
                status = create_directory(temp_file)
                if status == 'Failure':
                    exit(-1)
                    
                if type(s_val) == list:
                    for s_file in s_val:
                        temp_file = os.path.join(main_path, key, s_key, s_file)
                        create_file(temp_file)
        elif type(val) == list:
            #  Create all files in the list
            for s_file in val:
                if key == 'tests':
                    s_file = f"{s_file}{project_name_safe}.py"
                temp_file = os.path.join(main_path, key, s_file)
                create_file(temp_file)
        else:
            print(f"Type {type(val)} definition not found.")
    
    
    print("Ending Script")
    
    
