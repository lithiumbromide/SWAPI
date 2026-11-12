---
title: "Get Active Document Dependents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Active_Document_Dependents_Example_VB.htm"
---

# Get Active Document Dependents Example (VBA)

This example shows how to return all of the dependent files for the currently active document. You can run this program on any type of SOLIDWORKS Design document.

```vb
'----------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim vDepend                 As Variant
    Dim i                       As Long

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc

    vDepend = swModel.GetDependencies2(True, True, True)

    Debug.Print swModel.GetPathName
    For i = 0 To (UBound(vDepend) - 1) / 2
        Debug.Print "    " + vDepend(2 * i) + " --> " + vDepend(2 * i + 1)
    Next i
End Sub
'----------------------------------
```
