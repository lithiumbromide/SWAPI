---
title: "Get and Set File Summary Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_File_Summary_Information_Example_VB.htm"
---

# Get and Set File Summary Information Example (VBA)

This example shows how to get and set the file summary information in a SOLIDWORKS Design document.

```
'-----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Sets summary information for the part document.
' 3. Examine the Immediate window.
' 4. Click File > Properties and examine the Summary
'    Information dialog.
'-----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim Text As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
```

```
    ' Set and get the Title KeyWord in the File Summary Info
    swModel.SummaryInfo(swSumInfoTitle) = "TitleXX"
    Text = swModel.SummaryInfo(swSumInfoTitle)
```

```
    ' Set and get the Subject KeyWord in the File Summary Info
    swModel.SummaryInfo(swSumInfoSubject) = "SubjectXX"
    Text = swModel.SummaryInfo(swSumInfoTitle)
```

```
    ' Set and get the Author KeyWord in the File Summary Info
    swModel.SummaryInfo(swSumInfoAuthor) = "AuthorXX"
    Text = swModel.SummaryInfo(swSumInfoAuthor)
```

```
    ' Set and get the Keywords KeyWord in the File Summary Info
    swModel.SummaryInfo(swSumInfoKeywords) = "KeywordsXX"
    Text = swModel.SummaryInfo(swSumInfoKeywords)
```

```
    ' Set and get the Comment KeyWord in the File Summary Info
    swModel.SummaryInfo(swSumInfoComment) = "CommentXX"
    Text = swModel.SummaryInfo(swSumInfoComment)
```

```
    ' Get the read-only Summary info fields
    Text = swModel.SummaryInfo(swSumInfoSavedBy)
    Debug.Print "Last saved by: " & Text
    Text = swModel.SummaryInfo(swSumInfoCreateDate)
    Debug.Print "Created: " & Text
    Text = swModel.SummaryInfo(swSumInfoSaveDate)
    Debug.Print "Last saved: " & Text
```

```
End Sub
```
