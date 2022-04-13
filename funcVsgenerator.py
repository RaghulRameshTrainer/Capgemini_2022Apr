import memory_profiler as mem_profile
import random
from time import process_time

names = ['Raghul', 'Ramesh', 'Karthick', 'Surya', 'Prabha', 'Ramu', 'Durga', 'Devi']
majors = ['Maths', 'Engineering', 'Science', 'Arts', 'CompSci', 'Businss']

print("Memory {BEFORE}:" + str(mem_profile.memory_usage()) + 'MB')


def people_list(num_people):
    result = []
    for i in range(num_people):
        student = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(student)
    return result


def people_generator(num_people):
    for i in range(num_people):
        student = {
            'id': i,
            'name': random.choice(names),
            'major': rondom.choice(majors)
        }
        yield student


# start = process_time()
# course_details = people_list(1000000)
# end = process_time()
start = process_time()
course_details = people_generator(1000000)
end = process_time()
print("Memory {AFTER}:" + str(mem_profile.memory_usage()) + 'MB')
print("Time : {} Seconds".format((end - start)*1000))
