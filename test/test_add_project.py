from model.project import Project


def test_add_project(app):
    project = Project(p_name="test8", description="test description32")
    old_project_list = app.project.get_projects_list()
    check = Project(p_name=project.p_name)
    #проверка что проекта с таким названием еще нет. Если есть, то ничего создовать не будем
    if check not in old_project_list:
        app.project.create(project)
        old_project_list.append(project)
    new_project_list = app.project.get_projects_list()
    assert old_project_list == new_project_list


