"""
Project Management
Estimate: 30 minutes
Actual:   40 minutes
"""
from project import Project

import csv
import datetime

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
def main():
    """The main function to manage the project"""
    filename = 'projects.txt'
    projects = []

    print("Welcome to Pythonic Project Management")
    print("Loaded 5 projects from projects.txt")

    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            load_projects(filename, projects)
        elif choice == 's':
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_by_data(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()
    save_choice = input("Would you like to save to projects.txt? ").lower()
    if save_choice in ['yes', 'y']:
        save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename, projects):
    in_file = open(filename,'r')
    for line in in_file:
        parts = line.strip().split(',')
        project = Project(parts[0],parts[1],parts[2],parts[3],parts[4])
        projects.append(project)
    in_file.close()
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects

def save_projects(filename, projects):
    """save the project"""
    in_file = open(filename, 'w')
    for project in projects:
        in_file.write(project.to_string())
    print(f"Saved {len(projects)} projects from {filename}")
    in_file.close()


def display_projects(projects):
    complete = [project for project in projects if project.is_complete()]
    complete_sorted = sorted(complete, key=lambda project: project.priority)
    incomplete = [project for project in projects if not project.is_complete()]
    incomplete_sorted = sorted(incomplete, key=lambda project: project.priority)
    print("Incomplete projects:")
    for project in incomplete_sorted:
        print(project)
    print("Complete projects:")
    for project in complete_sorted:
        print(project)

def filter_by_data(projects):
    data_string = print("Show projects that start after date (dd/mm/yy): ")
    data = datetime.datetime.strptime(data_string, "%d/%m/%Y").date()
    filtered = [project for project in projects if project.start_date >= data]
    filtered_sorted = sorted(key=lambda project: project.start_date)
    for project in filtered_sorted:
        print(filtered_sorted)

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yy): ")
    start_data = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_data, priority, cost_estimate, completion_percentage))

def update_project(projects):
    for i, project in enumerate(projects, 0):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    if 0 <= project_choice <= len(projects):
        project = projects[project_choice]
        print(project)
        new_percentage = int(input("New percentage: "))
        new_priority = int(input("New priority: "))
        project.update_percentage(new_percentage)
        project.update_priority(new_priority)

main()