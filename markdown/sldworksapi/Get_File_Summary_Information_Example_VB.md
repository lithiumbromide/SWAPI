---
title: "Get File Summary Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_File_Summary_Information_Example_VB.htm"
---

# Get File Summary Information Example (VBA)

This example shows how to get the file summary information for an active SOLIDWORKS Design document.

```
'---------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the summary information for
'    the model document.
' 2. Examine the Immediate window.
'---------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    Debug.Print "File = " + swModel.GetPathName
```

```
    Debug.Print "  Title         = " + swModel.SummaryInfo(swSumInfoTitle)
    Debug.Print "  Subject       = " + swModel.SummaryInfo(swSumInfoSubject)
    Debug.Print "  Author        = " + swModel.SummaryInfo(swSumInfoAuthor)
    Debug.Print "  Keywords      = " + swModel.SummaryInfo(swSumInfoKeywords)
    Debug.Print "  Comment       = " + swModel.SummaryInfo(swSumInfoComment)
    Debug.Print "  Saved by      = " + swModel.SummaryInfo(swSumInfoSavedBy)
    Debug.Print "  Date created  = " + swModel.SummaryInfo(swSumInfoCreateDate)
    Debug.Print "  Date saved    = " + swModel.SummaryInfo(swSumInfoSaveDate)
    Debug.Print "  Date created  = " + swModel.SummaryInfo(swSumInfoCreateDate2)
    Debug.Print "  Date saved    = " + swModel.SummaryInfo(swSumInfoSaveDate2)
```

```
End Sub
```
