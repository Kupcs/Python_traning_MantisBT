from model.project import Project
import random


def test_add_project(app):
    if app.project.project_count() == 0:
        app.project.create(Project(p_name="project for removing"))
    old_project_list = app.project.get_projects_list()
    project = random.choice(old_project_list)
    app.project.delete_project_by_name(project.p_name)
    new_project_list = app.project.get_projects_list()
    old_project_list.remove(project)
    assert old_project_list == new_project_list
