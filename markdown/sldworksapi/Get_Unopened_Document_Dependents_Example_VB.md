---
title: "Get Unopened Document Dependents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Unopened_Document_Dependents_Example_VB.htm"
---

# Get Unopened Document Dependents Example (VBA)

This example shows how to return all of the dependent files for the specified closed document. You can run this program on any type of SOLIDWORKS Design document.

```vb
'-----------------------------------------------
Option Explicit

Sub main()
    Const sDefaultName      As String = "D:\docs\claw-mechanism.sldasm"
    Dim swApp               As SldWorks.SldWorks
    Dim swModel             As SldWorks.ModelDoc2
    Dim sDocName            As String
    Dim vDepend             As Variant
    Dim bRet                As Boolean
    Dim i                   As Long

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc

    If Not swModel Is Nothing Then
        sDocName = swModel.GetPathName
    Else
        sDocName = sDefaultName
    End If

    vDepend = swApp.GetDocumentDependencies2(sDocName, True, True, False)

    Debug.Print sDocName
    If IsEmpty(vDepend) Then
        Debug.Print "    No dependencies"
        Exit Sub
    End If

    For i = 0 To (UBound(vDepend) - 1) / 2
        Debug.Print "    " + vDepend(2 * i) + " --> " + vDepend(2 * i + 1)
    Next i
End Sub
'-----------------------------------------------
```
