import pandas

# 판다스 데이터 프레임에서 반복문을 사용하는 방법과
# 판다스 데이터 프레임을 반복하는 방법

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# lopping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame
# for (k, v) in student_data_frame.items():
#     print(v)

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)

