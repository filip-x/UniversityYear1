from assignmentrepo import AssignmentRepo
from assignment import Assignment
from services import Services
from repoassignmentfile import RepoAssignmentFile
import json


class RepoAssignmentJsonFile(RepoAssignmentFile):

    def read_repo(self):
        try:
            open_file = open(self.file_n, "r")
            save_assignments_lists = json.load(open_file)
            for assignment_list in save_assignments_lists:
                # we created a assignment
                file_assignment = Assignment(assignment_list[1], assignment_list[2], assignment_list[0])
                self.assignments.append(file_assignment)  # we got him in the list
            open_file.close()
        except EOFError:  # pickle will give an error if the file is empty
            pass
        except IOError as error:  # if it's an input error
            raise error
        except json.decoder.JSONDecodeError as error:  # json will give an error if the file is empty
            pass

    def write_repo(self):
        save_assignments_lists = []
        open_file = open(self.file_n, "w")
        for i in range(len(self.assignments)):
            # if the assignments is not  there it won't be written
            if self.assignments[i] != None:
                assignment_list = [self.assignments[i].get_aid(), self.assignments[i].get_description(), self.assignments[i].get_deadline()]
                save_assignments_lists.append(assignment_list)
        json.dump(save_assignments_lists, open_file)
        open_file.close()
