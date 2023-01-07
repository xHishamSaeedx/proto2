import pandas as pd
import numpy as np
import math

def strtolist(st):
    tempo = st.split(",")
    lst = [int(x) for x in tempo if x.isalnum()]
    return lst

def arrange(lst,prio):
    temp = []
    for i in prio:
        temp.append(lst[int(i)-1])

    return temp


def hrs_allot(time_req,total_time):
    count = 5
    while(1):
        per = 100
        total_req_time = sum(time_req)
        if total_req_time > total_time:
            for i in range(len(time_req)):
                time_req[i] = time_req[i] * ((per-count)*0.01)
        else:
            break
    count += 5
    time_req2 = [math.floor(x) for x in time_req]
    return time_req2




def algo2(subjectList,topics_hrs,calendar,priority):



    calendar2 = [x for x in calendar]
    calendar3 = [x for x in calendar]
    z = []
    truth = True

    # it is day 2
    available_hrs = 5

     # BE AND DM AND DSA

    priority_temp = [x for x in priority]
    priority_temp2 = [x for x in priority]
    num_of_subject = 5
    priority_subjectlist = []


    def positive_checker(list):
        z = []
        for x in list:
            for y in x:
                z.append(y)
        return all(x >= 0 for x in z)


    def chkList(lst):
        return len(set(lst)) == 1


    # now starts the operations

    def remove_adjacent(nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                i -= 1
            i += 1
        return nums

    global timetable

    timetable = []


    def adjuster(list1, hrs):
        if sum(list1) > hrs:
            x = sum(list1) - hrs
            y = len(list1)
            while x > 0:
                if list1[y - 1] <= x:
                    x = x - list1[y - 1]

                    list1.pop()
                    y -= 1

                else:
                    list1[y - 1] -= x

                    x = 0


    def multiple_subject_adjuster(list1, list2):
        a = sum(list1)
        b = sum(list2)

        while (len(list1) > len(list2)):
            i = 0
            if list1[i] + list2[i] > a:

                b = a - list1[i]
                list1[i] += b
                list2[i] -= b

                c = b
                temp_list = []
                for h in range(len(list1) - 1, -1, -1):
                    if c > list1[h]:
                        c -= list1[h]
                        temp_list.append(list1[h])
                        list1.pop()

                    else:
                        list1[h] -= c
                        list2.append(c)

                for z in temp_list[::-1]:
                    list2.append(z)

                adjuster(list1, a)
                adjuster(list2, b)
                for x in list1[::-1]:
                    if x == 0:
                        list1.pop()
                    elif x != 0:
                        break

            else:

                list1[i] += list2[i]
                s = list2[i]
                list2[i] -= s
                temp_list2 = []
                for w in range(len(list1) - 1, -1, -1):
                    if list1[w] >= s:
                        list1[w] -= s
                        list2.append(s)
                        break

                    else:
                        s = s - list1[w]
                        temp_list2.append(list1[w])
                        list1.pop()

                for r in temp_list2[::-1]:
                    list2.append(r)

                adjuster(list1, a)
                adjuster(list2, b)
                for x in list1[::-1]:
                    if x == 0:
                        list1.pop()
                    elif x != 0:
                        break

            i += 1

    # the abobe logic needs to be rewritten
    def time_divider(j, prio, timetbl, subj1=[]):
        sub1 = [x for x in subj1]
        sub2 = []

        calendar2 = [x for x in calendar3]
        # calendar needs to revert back if j increases like how sub1 and sub2 r getting empty
        count = 0

        global timetable
        timetable = [x for x in timetbl]
        priority_temp = [x for x in prio]

        sub1_hrs = topics_hrs[priority_temp.index(min(priority_temp))]

        z = []
        # to make sure calendar2 doesnt reset from 0 position

        # fill in sub1 with respective hrs

        for x in timetable:
            for y in range(len(x)):
                calendar2[y] -= x[y]

        count2 = 0
        for k in calendar2:
            if k == 0:
                count2 += 1
            else:
                break

        def most_priority_adder(list1, hrs):
            count1 = 0
            for i in calendar2[count2:]:
                if (sum(list1) < hrs) and i > j:

                    list1.append(i - j)
                    count1 += 1
                elif (sum(list1) < hrs) and i <= j:

                    list1.append(j)
                    count1 += 1
                else:
                    break

            return count1

        count = most_priority_adder(sub1, sub1_hrs)

        # adjusts the allotted hrs to match the hrs required

        adjuster(sub1, sub1_hrs)

        if sum(sub1) != sub1_hrs:
            return 0
        # timetable adder of first element
        timetable.append(sub1)

        # calendar2 gets updated with how many hrs left

        if count2 == 0:


            for i in timetable:
                for x in range(len(i)):
                    calendar2[x] -= i[x]

        else:

            calendar2 = [x for x in calendar3]

            for i in timetable[:len(timetable) - 1]:
                for ju in range(len(i)):
                    calendar2[ju] -= i[ju]

            for i in range(len(sub1)):
                calendar2[i] -= sub1[i]  # last change hopefully

        # we dealt with first priority , so we eliminate it
        priority_temp[priority_temp.index(min(priority_temp))] = 1000

        # allotting sub2 hrs
        sub2_hrs = topics_hrs[priority_temp.index(min(priority_temp))]

        def remaining_hrs_adder(list2, hrs):
            for i in range(len(calendar2)):
                list2.append(calendar2[i])
                if sum(list2) > hrs:
                    break
                calendar2[i] = 0

        remaining_hrs_adder(sub2, sub2_hrs)

        adjuster(sub2, sub2_hrs)

        if sum(sub2) == sub2_hrs and len(sub2) < len(sub1):
            multiple_subject_adjuster(sub1, sub2)
            timetable.append(sub1)
            timetable.append(sub2)

            return 1

        else:
            timetable.append(sub1)
            timetable.append(sub2)

            priority_temp = [x for x in priority_temp2]
            return 2

    # passing in values

    timetable2 = [x for x in timetable]

    for i in range(len(subjectList)):  #

        sub1hrs = topics_hrs[priority_temp2.index(min(priority_temp2))]
        for j in range(1, max(calendar)):
            if len(timetable2) == 0:
                if not positive_checker(timetable):
                    calendar3 = calendar2[:]
                    time_divider(j - 2, priority_temp2, timetable2)
                    break
                if time_divider(j, priority_temp2, timetable2) == 1:
                    time_divider(j - 1, priority_temp2, timetable2)
                    break
                elif time_divider(j, priority_temp2, timetable2) == 2:
                    continue
                elif time_divider(j, priority_temp2, timetable2) == 0:
                    time_divider(j - 1, priority_temp2, timetable2)
                    break
                else:
                    break

            else:
                x = time_divider(j - 2, priority_temp2, timetable2, timetable2[len(timetable2) - 1])
                if not positive_checker(timetable):
                    calendar3 = calendar2[:]
                    time_divider(j - 2, priority_temp2, timetable2, timetable2[len(timetable2) - 1])
                    break
                if x == 1:
                    time_divider(j - 1, priority_temp2, timetable2, timetable2[len(timetable2) - 1])
                    break
                elif x == 2:
                    continue
                elif x == 0:
                    time_divider(j - 1, priority_temp2, timetable2, timetable2[len(timetable2) - 1])
                    break
                else:
                    break

     # here lies the issue
        calendar3 = [x for x in calendar2]

        priority_temp2[priority_temp2.index(min(priority_temp2))] = 1000

        timetable = remove_adjacent(timetable)

        timetable2 = [x for x in timetable]

        if priority_temp2.count(1000) == len(priority) - 1:
            break

    if sum(timetable[len(timetable) - 1]) != topics_hrs[priority.index(max(priority_temp))]:
        for x in timetable:
            for i in range(len(x)):
                calendar3[i] -= x[i]

        count4 = 0
        h = timetable[len(timetable) - 1]
        for i in range(len(h)):
            if sum(h) == topics_hrs[priority.index(max(priority_temp))]:
                break
            else:
                h[i] += calendar3[i]

        if sum(h) != topics_hrs[priority.index(max(priority_temp))]:

            for i in range(len(h), len(calendar3)):
                if sum(h) == topics_hrs[priority.index(max(priority_temp))]:
                    break

                else:
                    h.append(topics_hrs[priority.index(max(priority_temp))] - sum(h))
                    calendar3[i] = calendar3[i] - h[len(h) - 1]

    for x in timetable:
        while (len(x) < len(calendar3)):
            x.append(0)

    return timetable



def dataf(dfs,start_dates,end_dates,weekend_hrss,weekday_hrss):
    date = pd.date_range(start_dates[len(start_dates)-1],end_dates[len(end_dates)-1])
    dfs['date'] = date
    dfs['year'] = pd.DatetimeIndex(dfs.date).year
    dfs['month'] = pd.DatetimeIndex(dfs.date).month
    dfs['day'] = pd.DatetimeIndex(dfs.date).day
    dfs['weekday'] = pd.DatetimeIndex(dfs.date).day_name()
    weekends = ["Sunday","Saturday"]

    study_hrs = []

    for i in dfs.weekday:
        if i in weekends:
            study_hrs.append(weekend_hrss[len(weekend_hrss)-1])
        else:
            study_hrs.append(weekday_hrss[len(weekday_hrss)-1])

    dfs["study_hrs"] = study_hrs

def sorts(tuples): 
    # Sorts in Ascending order 
    a = sorted(tuples, key = lambda a: a[1])
    return a

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst