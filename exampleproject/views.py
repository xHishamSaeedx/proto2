from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import pandas as pd
from .pandafiles import *

def projects(request):
    projects1 = Classproject.objects.all()
    return render(request,'primprojects/projects.html',{"projects1":projects1})

def project(request,cookie):
    projectobj = Classproject.objects.get(id = cookie)  
    semester_temp =  semester.objects.filter(curriculum = projectobj.id).values_list("name","id")
    semesters = [list(x) for x in semester_temp]
    x = {"sem1":semesters}
    return render(request,'primprojects/single-project.html',{"projects2":projectobj,"sem":x})

def updateProject(request,pk):
    updproject = Classproject.objects.get(id=pk)
    form = ClassprojectForm(instance=updproject)
    if request.method == 'POST':
        form = ClassprojectForm(request.POST,request.FILES,instance=updproject)
        if form.is_valid():
            form.save()
            return redirect('projectslink')    


    context = {'form': form}
    return render(request,'primprojects/project_form.html',context)


def createProject(request):
    form = ClassprojectForm()
    if request.method == 'POST':
        form = ClassprojectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-semester')    


    context = {'form': form}
    return render(request,'primprojects/project_form.html',context)

def deleteproject(request,pk):
    delproject = Classproject.objects.get(id=pk)
    if request.method=='POST':
        delproject.delete()
        return redirect('projectslink')  
    context = {'object': delproject}
    return render(request, 'primprojects/delete.html',context)



def createSemester(request):
    form = semesterForm()
    if request.method == 'POST':
        form = semesterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-project')    


    context = {'form': form}
    return render(request,'primprojects/semester_form.html',context)

def createBranch(request):
    form = branchForm()
    if request.method == 'POST':
        form = branchForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-semester')    


    context = {'form': form}
    return render(request,'primprojects/branch.html',context)


def createSubject(request):
    form = subjectForm()
    if request.method == 'POST':
        form = subjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-semester')    


    context = {'form': form}
    return render(request,'primprojects/subject_form.html',context)


def createUnit(request):
    form = unitForm()
    if request.method == 'POST':
        form = unitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-subject')    


    context = {'form': form}
    return render(request,'primprojects/unit_form.html',context)


def createTopic(request):
    form = topicForm()
    if request.method == 'POST':
        form = topicForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-unit')    


    context = {'form': form}
    return render(request,'primprojects/topic_form.html',context)


def semestersh(request,pk):
    projectobj = semester.objects.get(id = pk)  
    return render(request,'primprojects/semesters.html',{"projects1":projectobj})


def branchesh(request,cookie):
    projectobj = branch.objects.get(id = cookie)  
    subject_temp =  subject.objects.filter(branch = projectobj.id).values_list("name","id")
    subjects = [list(x) for x in subject_temp]
    x = {"sem1":subjects}
    return render(request,'primprojects/branches.html',{"projects2":projectobj,"sem":x})

def subjectsh(request,pk):
    projectobj = subject.objects.get(id = pk)  
    return render(request,'primprojects/subject.html',{"projects1":projectobj})


def unitish(request,cookie):
    projectobj = unit.objects.get(id = cookie)  
    return render(request,'primprojects/schedule.html',{"projects1":projectobj})









def createTT(request):
    form = timetableForm()
    if request.method == 'POST':
        form = timetableForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
           
            
            return redirect('select-subjects')    


    context = {'form': form}
    return render(request,'primprojects/tt_form.html',context)





def change(dfss,ind,hrs):
    dfss.at[ind,"study_hrs"]=hrs



def custom_hrs(request):
    form = timetableForm2()
    if request.method == 'POST':
        form = timetableForm2(request.POST,request.FILES)
        if form.is_valid():
            form.save() 

            dfs = pd.DataFrame()
            start_date = list(Timetable1.objects.values_list("start_date",flat = True))
            end_date = list(Timetable1.objects.values_list("end_date",flat = True))
            weekday_hrs = list(Timetable1.objects.values_list("weekday_hrs",flat = True))
            weekend_hrs = list(Timetable1.objects.values_list("weekend_hrs",flat = True))
            date = pd.date_range(start_date[len(start_date)-1],end_date[len(end_date)-1])
            dfs['date'] = date
            dfs['year'] = pd.DatetimeIndex(dfs.date).year
            dfs['month'] = pd.DatetimeIndex(dfs.date).month
            dfs['day'] = pd.DatetimeIndex(dfs.date).day
            dfs['weekday'] = pd.DatetimeIndex(dfs.date).day_name()
            weekends = ["Sunday","Saturday"]
            study_hrs = []
            for i in dfs.weekday:
                if i in weekends:
                    study_hrs.append(weekend_hrs[len(weekend_hrs)-1])
                else:
                    study_hrs.append(weekday_hrs[len(weekday_hrs)-1])

            dfs["study_hrs"] = study_hrs

            customdate = list(Timetable2.objects.values_list("custom_date",flat=True))
            indx = int(dfs[dfs["date"]==customdate[len(customdate)-1]].index.values)
            customhrs = list(Timetable2.objects.values_list("custom_hrs",flat=True))
            change(dfs,indx,customhrs[len(customhrs)-1])
            theid = subjecthrs.objects.values_list("id",flat = True).last()
            subject_hrs_temp = list(subjecthrs.objects.filter(id = theid).values_list("subject_hrs",flat=True))
            priority_temp = list(subjecthrs.objects.filter(id = theid).values_list("priority",flat=True))

            zeid2 = whatsubjects.objects.values_list("id",flat = True).last()
            subjectids2 = whatsubjects.objects.filter(id = zeid2).values_list("subjects",flat = True)
            subjectnamestemp = list(subject.objects.filter(id__in = subjectids2).values_list("name",flat = True))

            subject_hrs1 = strtolist(subject_hrs_temp[0])
            priority1 = strtolist(priority_temp[0])
            if len(subjectnamestemp)>1:
                subjectnames = arrange(subjectnamestemp,priority1)
            else:
                subjectnames = [x for x in subjectnamestemp]

            subject_hrs = hrs_allot(subject_hrs1,sum(dfs.study_hrs))

            alloted_hrs = algo2(subjectnames,subject_hrs,dfs.study_hrs,priority1)
            for i in range(len(subjectnames)):
                dfs[subjectnames[i]] = alloted_hrs[i]
            
            x = str(dfs.to_json())
            b = FinalTT(zefile = x)
            b.save()
            return redirect('demo')    


    context = {'form': form}
    return render(request,'primprojects/customhrs.html',context)








def selectsubjects(request):
    form = whatsubjectForm()
    if request.method == 'POST':
        form = whatsubjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('select-units')    
    
    context = {'form': form}
    return render(request,'primprojects/tt_form.html',context)



def selectunits(request):
    form = timetableForm3()
    if request.method == 'POST':
        form = timetableForm3(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subjecthrs')    
    
    context = {'form': form}
    return render(request,'primprojects/tt_form.html',context)



def subjecthours(request):
    form = subjecthrsForm()
    zeid = whatsubjects.objects.values_list("id",flat = True).last()
    subjectids = whatsubjects.objects.filter(id = zeid).values_list("subjects",flat = True)
    subjectnames = subject.objects.filter(id__in = subjectids).values_list("name",flat = True)
    if request.method == 'POST':
        form = subjecthrsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            

            return redirect('custom_hrs')    
    
    context = {'form': form,'subjects':subjectnames}
    return render(request,'primprojects/subjecthrs.html',context)






def demo(request):
    zid = FinalTT.objects.values_list("id",flat = True).last()
    h = list(FinalTT.objects.filter(id = zid).values_list("zefile",flat = True))
    d = pd.read_json(h[0])

    subids = whatsubjects.objects.values_list("id",flat = True).last()
    subid = whatsubjects.objects.filter(id = subids).values_list("subjects",flat = True)
    subs = subject.objects.filter(id__in = subid)




    mydict = {
        "df":d.to_html(),
        "names" : subs,
    }

    return render(request,'primprojects/demo.html',context = mydict)



def schedule(request,pk):
    
    x = subject.objects.filter(id = pk).values_list("units",flat = True)
    y = sumn.objects.filter(units__in = x).values_list("units",flat = True)
    z = unit.objects.filter(id__in = y).values_list("topic",flat = True)
    a = sorts(list(topic.objects.filter(id__in = z).values_list("name","rating")))

    semesters = [list(x) for x in a]
    x = {"sem1":Reverse(semesters)}
    return render(request,'primprojects/schedule.html',{"sem":x})
