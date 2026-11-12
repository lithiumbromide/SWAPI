---
title: "Get Version History Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Version_History_Example_VB.htm"
---

# Get Version History Example (VBA)

This example shows how to get the version history of a SOLIDWORKS Design model document.

```
'------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the version number of the model document.
' 2. Examine the Immediate window.
'------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim vVerStr As Variant
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    If IsEmpty(vVerStr) Then
       vVerStr = swApp.VersionHistory(swModel.GetPathName)
    End If
```

```
    If Not IsEmpty(vVerStr) Then
        For i = 0 To UBound(vVerStr)
            Debug.Print "  " & vVerStr(i)
        Next i
    Else
        Debug.Print "  No version information."
    End If
```

```
End Sub
```
