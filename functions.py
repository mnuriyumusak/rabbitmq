import random


def entln_package_creator():
    result_str = ""
    flash_types = [0, 1, 9]
    result_str += str(flash_types[random.randint(0, 2)]) + ","
    result_str += "2016"+str("%02d" % random.randint(1, 12))+str("%02d" % random.randint(1, 30))+"T" +\
                  str("%02d" % random.randint(0, 23))+str("%02d" % random.randint(1, 59)) +\
                  str("%02d" % random.randint(1, 59))+"."+str("%03d" % random.randint(1, 999))+","
    result_str += "+"+str(random.uniform(37.1, 41.3))[0:10]+","
    result_str += "+0"+str(random.uniform(27.3, 43.0))[0:10]+","
    result_str += "+"+str("%09d" % random.randint(1, 25000))+","
    result_str += "000,"
    result_str += str("%05d" % random.randint(10000, 17000))+","
    result_str += str("%03d" % random.randint(1, 20))+","
    result_str += str("%03d" % random.randint(1, 6))
    result_str += "\r\n"
    return str(result_str)


