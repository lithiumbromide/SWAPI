---
title: "Create Motion Studies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Create_Motion_Studies_Example_VB.htm"
---

# Create Motion Studies Example (VBA)

This example shows how to create, rename, and delete motion studies.

```vb
'--------------------------------------------------------
'
' Preconditions:
'                 (1) Part or assembly is open.
'                 (2) MotionManager tab is visible. If it is not visible,
'                     click View, MotionManager.
'                 (3) SOLIDWORKS nnnn MotionStudy Type Library, where
                      nnnn is the version number of the release, is
'                     selected on Tools, References.
'
' Postconditions: Two motion studies exist: Motion Study 1 and TestName.
'
'-------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMotionMgr As SwMotionStudy.MotionStudyManager
Dim swMotionStudy1 As SwMotionStudy.MotionStudy
Dim swMotionStudy2 As SwMotionStudy.MotionStudy
Dim swMotionStudy3 As SwMotionStudy.MotionStudy
Dim swSaveAVIData As SwMotionStudy.AVIParameter
Dim boolstatus As Boolean

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension

    ' Get the MotionManager
    Set swMotionMgr = swModelDocExt.GetMotionStudyManager()
    If (swMotionMgr Is Nothing) Then
          End
    End If

    ' Create new motion studies
    Set swMotionStudy2 = swMotionMgr.CreateMotionStudy()
    If (swMotionStudy2 Is Nothing) Then
        MsgBox "Motion Study 2 is not available."
        End
    End If

    Set swMotionStudy3 = swMotionMgr.CreateMotionStudy()
    If (swMotionStudy3 Is Nothing) Then
        MsgBox "Motion Study 3 is not available."
        End
    End If

    ' Get number of motion studies
    Debug.Print "Number of motion studies = " & swMotionMgr.GetMotionStudyCount

    ' Get motion study
    Set swMotionStudy1 = swMotionMgr.GetMotionStudy("Motion Study 1")
    If (swMotionStudy1 Is Nothing) Then
        MsgBox "Motion Study 1 is not available."
        End
    End If

    ' Get number and names of motion studies and whether they've been activated
    Dim vNames As Variant
    Dim i As Long
    vNames = swMotionMgr.GetMotionStudyNames()
    For i = 0 To UBound(vNames)
        Debug.Print vNames(i);
        boolstatus = swMotionMgr.ActivateMotionStudy(vNames(i))
        Debug.Print " activated = " & boolstatus
    Next i

   ' Attempt to activate a non-existing motion study
    boolstatus = swMotionMgr.ActivateMotionStudy("Motion Study 4") ' Should return False
    Debug.Print "Motion Study 4 activated = " & boolstatus

    ' Delete Motion Study2 and non-existing motion study
    boolstatus = swMotionMgr.DeleteMotionStudy("Motion Study 2")
        Debug.Print "Motion Study 2 deleted = " & boolstatus
    boolstatus = swMotionMgr.DeleteMotionStudy("Motion Study 4")
        Debug.Print "Motion Study 4 deleted = " & boolstatus ' Should return False

    ' Rename Motion Study 3 to TestName
    swMotionStudy3.Name = "TestName"

    ' Set and save AVI parameters
    Set swSaveAVIData = swMotionMgr.CreateAVIParameter()
    swSaveAVIData.FramePerSecond = 7.5
    swSaveAVIData.SaveEntireAnimation = True
    swSaveAVIData.OutputType = 1 ' Save as an .avi file

End Sub
```
