---
title: "Get Error Codes for Features (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Error_Codes_for_Features_Example_VB.htm"
---

# Get Error Codes for Features (VBA)

This example shows how to get the error codes and warnings for the features in a part document.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: Features with errors have error codes of non-zero.
' Only examine warnings if error codes are non-zero.
' Otherwise, values for warnings are irrelevant.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Model As SldWorks.ModelDoc2
Dim feat As SldWorks.Feature
Dim featureName As String
Dim IsWarning As Boolean
Dim Error As Long
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set Model = swApp.ActiveDoc
```

```
    If Model Is Nothing Then
        Exit Sub
    End If
```

```
    ' Get the first feature in part
    Set feat = Model.FirstFeature
    ' While we have a valid feature
    Do While Not feat Is Nothing
        ' Get the name of the feature
        Debug.Print feat.Name
        Error = feat.GetErrorCode2(IsWarning)
        Debug.Print "Error:          " & Error
        Debug.Print "Warning:        " & IsWarning
        Set feat = feat.GetNextFeature() ' Get the next feature
    Loop ' Continue until no more features exist
```

```
End Sub
```
