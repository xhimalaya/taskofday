import pandas as pd
string_count=0
not_string_count=0
data_count=[]
########################################################################################################
class data_validation_check():
    def __init__(self,string_count,not_string_count,data_count,file_name):
        data=pd.read_csv(file_name)
        self.data=data
        self.col={i:str(data[i].dtypes) for i in data}
        for j in self.col:
            string_count=0
            not_string_count=0
            for k in data[j].values:
                x1=self.check_datatype(k)
                if x1 == "int64" or x1=="float64":
                    not_string_count+=1
                elif x1=="object":
                    string_count+=1
            data_count.append(
                {
                    "name":j,
                    'type':
                    {
                        "Float64":not_string_count,
                        "string":string_count
                    }
                }
            )
        self.data_count=data_count
##########################################################################################################
    def check_datatype(self,value):
        if str(value).isalpha():
            return "object"
        else:
            try:
                int(value)
                return "int64"
            except ValueError:
                try:
                    float(value)
                    return "float64"
                except:
                    return "object"
##############################################################################################################
file_name=input("Enter the file name with address:  ")
data_result=data_validation_check(string_count,not_string_count,data_count,file_name)
result={
    "result":{
        "column_types":data_result.col
    },
    "columns":list(data_result.data.columns),
    "mixedDataTypes":data_result.data_count,
     "rows": len(data_result.data)
}
##############################################################################
print(result)