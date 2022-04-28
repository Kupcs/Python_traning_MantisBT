from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_create_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()

    def fill_project_form(self, project):
        self.change_field_value("name", project.p_name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, project):
        wd = self.app.wd
        self.open_project_create_page()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        wd.find_element_by_link_text("Manage Users")
        self.project_cache = None

    project_cache = None

    def get_projects_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("table[class='width100'][cellspacing ='1'] tr")[2:]:
                cells = element.find_elements_by_tag_name("td")
                firstname_text = cells[0].text
                discription_text = cells[4].text
                self.project_cache.append(Project(p_name=firstname_text, description=discription_text, id=id))
        return list(self.project_cache)

    def project_count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        return len(wd.find_elements_by_css_selector("table[class='width100'][cellspacing ='1'] tr")[2:])

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        self.select_project_by_name(name)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

