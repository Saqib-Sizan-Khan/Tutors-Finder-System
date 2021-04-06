from django.shortcuts import render,redirect
from studentParent.models import StudentParent,TemporarySP
from educator.models import HomeEducator,OutsideEducator,HomeEducatorSubjects,OutsideEducatorSubjects,TemporaryE
from .models import Request,Deals
from django.contrib import messages
from django.db.models import Q


def homePage(request):
    return render(request,'home/home.html')


def aboutus(request):
    return render(request,'home/aboutus.html')


def confirmRequest(request):
    if request.method == "POST":
        educatortype = request.POST["educatortype"]
        educatorid = request.POST["educatorid"]
        parentid = request.POST["parentid"]

        if educatortype == "Home Educator":
            if HomeEducator.objects.filter(id=educatorid).exists():
                if StudentParent.objects.filter(id=parentid).exists():

                    parent = StudentParent.objects.get(id=parentid)
                    x = TemporarySP.objects.get(id=1)

                    if parent.parentName == x.parentName and parent.parentPassword == x.parentPassword:

                        y = HomeEducator.objects.get(id=educatorid)
                        req = Request(educatorType=educatortype,educatorId=educatorid,educatorName=y.homeTutorName,
                                      parentId=parentid,parentName=x.parentName)

                        req.save()
                        return redirect("confirmrequest")
                    else:
                        messages.info(request, "Invalid Parent Id")
                else:
                    messages.info(request,"Invalid Parent Id")
            else:
                messages.info(request,"Invalid Educator Id")

        else:
            if OutsideEducator.objects.filter(id=educatorid).exists():
                if StudentParent.objects.filter(id=parentid).exists():

                    parent = StudentParent.objects.get(id=parentid)
                    x = TemporarySP.objects.get(id=1)

                    if parent.parentName == x.parentName and parent.parentPassword == x.parentPassword:

                        y = OutsideEducator.objects.get(id=educatorid)
                        req = Request(educatorType=educatortype,educatorName=y.outsideTutorName,educatorId=educatorid,
                                        parentId=parentid,parentName=x.parentName)

                        req.save()
                        messages.info(request,"Request Sent")
                    else:
                        messages.info(request, "Invalid Parent Id")
                else:
                    messages.info(request,"Invalid Parent Id")
            else:
                messages.info(request,"Invalid Educator Id")

    return render(request, "home/confirmrequest.html")


def showRequest(request):
    if request.method == "POST":
        educatortype = request.POST["educatortype"]
        educatorid = request.POST["educatorid"]

        if educatorid == "":
            messages.info(request, "Invalid Educator ID")
            return redirect('showrequest')

        if educatortype == "Home Educator":

            x = HomeEducator.objects.get(id=educatorid)
            y = TemporaryE.objects.get(id=1)

            if x.homeTutorName == y.tutorName:
                req = Request.objects.filter(Q(educatorId=educatorid) & Q(educatorType=educatortype))
                context = {"req":req}
                return render(request, 'home/showrequest.html', context)

            else:
                messages.info(request,"Invalid Educator ID")

        else:
            x = OutsideEducator.objects.get(id=educatorid)
            y = TemporaryE.objects.get(id=1)

            if x.outsideTutorName == y.tutorName:
                req = Request.objects.filter(Q(educatorId=educatorid) & Q(educatorType=educatortype))
                context = {"req": req}
                return render(request, 'home/showrequest.html', context)

            else:
                messages.info(request,"Invalid Educator ID")


    return render(request, "home/showrequest.html")


def acceptRequest(request):

    if request.method == "POST":
        educatortype = request.POST["educatortype"]
        educatorid = request.POST["educatorid"]
        parentid = request.POST["parentid"]

        if educatortype == "Home Educator":
            if HomeEducator.objects.filter(id=educatorid).exists():
                if StudentParent.objects.filter(id=parentid).exists():

                    home_tutor = HomeEducator.objects.get(id=educatorid)
                    x = TemporaryE.objects.get(id=1)

                    if home_tutor.homeTutorName == x.tutorName and home_tutor.homeTutorPassword == x.tutorPassword:

                        y = StudentParent.objects.get(id=parentid)
                        deal = Deals(educatorType=educatortype,educatorId=educatorid,educatorName=x.tutorName,
                                      parentId=parentid,parentName=y.parentName)

                        if Request.objects.filter(Q(parentId=parentid) & Q(educatorId=educatorid)).exists():
                            req = Request.objects.get(Q(parentId=parentid) & Q(educatorId=educatorid))

                            deal.save()
                            req.delete()
                            messages.info(request, "Request accepted")
                        else:
                            messages.info(request,"Invalid Parent Id")
                            return redirect("acceptrequest")

                        messages.info(request,"Request accepted")
                    else:
                        messages.info(request, "Invalid Educator Id")
                else:
                    messages.info(request,"Invalid Parent Id")
            else:
                messages.info(request,"Invalid Educator Id")

        else:
            if OutsideEducator.objects.filter(id=educatorid).exists():
                if StudentParent.objects.filter(id=parentid).exists():

                    outside_tutor = OutsideEducator.objects.get(id=educatorid)
                    x = TemporaryE.objects.get(id=1)

                    if outside_tutor.outsideTutorName == x.tutorName and outside_tutor.outsideTutorPassword == x.tutorPassword:

                        y = StudentParent.objects.get(id=parentid)
                        deal = Deals(educatorType=educatortype, educatorId=educatorid, educatorName=x.tutorName,
                                     parentId=parentid, parentName=y.parentName)

                        if Request.objects.filter(Q(parentId=parentid) & Q(educatorId=educatorid)).exists():
                            req = Request.objects.get(Q(parentId=parentid) & Q(educatorId=educatorid))

                            deal.save()
                            req.delete()
                            messages.info(request, "Request accepted")
                        else:
                            messages.info(request, "Invalid Parent Id")
                            return redirect("acceptrequest")
                    else:
                        messages.info(request, "Invalid Educator Id")
                else:
                    messages.info(request,"Invalid Parent Id")
            else:
                messages.info(request,"Invalid Educator Id")

    return render(request,'home/acceptrequest.html')


def showDeals(request):
    if request.method == "POST":
        parentid = request.POST["parentid"]

        if parentid == "":
            messages.info(request, "Invalid parent ID")
            return redirect('showdeals')

        if StudentParent.objects.filter(id=parentid).exists():

            x = StudentParent.objects.get(id=parentid)
            y = TemporarySP.objects.get(id=1)

            if x.parentName == y.parentName:

                deal = Deals.objects.filter(parentId=parentid)

                context = {"deal":deal}
                return render(request, 'home/showdeals.html', context)

            else:
                messages.info(request,"Invalid Parent ID")

        else:
            messages.info(request, "Invalid Parent ID")

    return render(request,'home/showdeals.html')