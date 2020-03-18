from data.story_dict import STORY_DICT


class StoryPrinter:
    """
    Class to print story narratives and display options.
    """
    def __init__(self, current_index):
        self.current_index = current_index
        self.choices = list()
        # Run on construction
        self.print_message()
        self.print_options()

    def print_message(self):
        print(STORY_DICT[self.current_index]["message"])

    def print_options(self):
        print(STORY_DICT[self.current_index]["options"]["message"])
        self.choices = STORY_DICT[self.current_index]["options"]["list"]
