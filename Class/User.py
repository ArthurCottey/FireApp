class User:

    #region Constructor
    def __init__(self, id, first_name, name):
        self.__id = id
        self.__first_name = first_name.upper()
        self.__name = name.capitalize()
    #endregion

    # region Getter & setter (id)
    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
    # endregion

    # region Getter & setter (first_name)
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name
    # endregion

    # region Getter & setter (name)
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    # endregion