class CsvBuilder:

    def __init__(self, file_path):
        self.file_path= file_path
        self.data = []

    def add_data(self, string):
        """
        adds a new data element to data[]
        args:
            string: string to be appended to data[]
        """
        self.data.append(string)

    def write_to_csv(self):
        """
        writes all strings held in data[] to specifeid csv filepath
        """
        data = self.data
        if len(data) > 0:
            file = open(self.file_path, "a")
            file.write("HASH BATCH\n")
            for i in range(1, len(self.data) + 1):
                string = self.data[i - 1]
                file.write(string + ',')
                if(i % 19 == 0):
                    file.write("\n")
            file.write("\n")
            file.close()


    def clear_csv(self):
        """
        clears the file associated with the specified file_path
        """
        file = open(self.file_path, "w")
        file.close()
