import os
import sys


class FinalOutput:

    def __init__(self):
        """
        Creates an object Final Output.
        """
        # initialise an empty list for storing file names, class is used because
        #  classes are easily mutable and are easy to keep track of
        self.array = []

    def add_to_self(self, data):
        """
        adds data to self.array.
        :param data: list data
        :return: None
        : post-condition: self.array will have data appended to its last index
        """
        self.array.append(data)
        return

    def self_sort_based_on_second_column(self):
        """
        sorts its self.array, based on its second value in each index. This functions assumes self.array is a list of
        list, holding a list in each index, and attempts to sort it based on the second value each index's list.
        The function may not work as expected if the condition is not satisfied
        :return: None
        : post-condition: self.array will its data sorted, based on the second value of the list in each index
        : complexity: O(n.log n),
                        where n is the length of self.array
                                because we are using Python's built in function sort() and built-in sort's complexity
                                is O(n.log n)
        """

        self.array.sort(key=lambda x: x[1])
        return

    def self_print(self):
        """
        Joins all file names, and print and return them. This function assumes self.array is a list of list, and it
        holds the file names in its first value in each index's list.
        The function may not work as expected if this condition is not satisfied
        :return: the output from joining all file names
        """
        # join all filenames,
        # and then print and return them
        output = ""
        for x in self.array:
            output += x[0]  # index 0 because we want file_name only

        print(output)
        return output


def recursion(path, names):
    """
    This functions opens the directory, reads all its files, and stores the files' filenames and the file's contents
    :param path: path of the directory
    :param names: FinalOutput object, used for storing and keeping track of the files' filenames and the file's contents
    :return: None
    : post condition: the FinalOutput object gets updated to store all of the directory's
                            items' filenames and the file's contents
    : complexity: O(m+n),
                    where
                    m is the number of folders, and
                    n is the numbers of files in the directory.
    """
    for item in os.listdir(path):

        # set the directory for the item we are checking
        checking_dir = path + "/" + item

        # if it is a directory, check it
        if os.path.isdir(checking_dir):
            recursion(checking_dir, names)

        # if it is a file, save it for printing later
        elif os.path.isfile(checking_dir):
            # os.path.splitext is used to remove the file extension
            file_name_without_extension = os.path.splitext(item)[0]

            # opens the file and reads its contents
            reader = open(checking_dir)
            contents = reader.read()
            contents = contents.rstrip("\n")  # remove new lines
            contents = int(contents)  # convert to integer
            reader.close()

            names.add_to_self([file_name_without_extension, contents])

        # note that if the directory is empty, no files gets added

    return


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    checking_directory = "./" + sys.argv[1]

    the_names = FinalOutput()

    recursion(checking_directory, the_names)
    the_names.self_sort_based_on_second_column()
    the_names.self_print()
