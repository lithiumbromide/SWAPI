---
title: "Get Material Property Names Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Material_Property_Names_Example_VB.htm"
---

# Get Material Property Names Example (VBA)

This example shows how to get the names of the materials applied to a part and faces of the part.

```
'----------------------------------------------
' Preconditions:
' 1. Open a part to which materials are applied
'    to multiple faces.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of the material applied to
'    the part and to each face of the part.
' 2. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc
    Dim swPart As SldWorks.PartDoc
    Dim swConfig As SldWorks.Configuration
    Dim swBody As SldWorks.Body
    Dim swFace As SldWorks.Face
    Dim sMatName As String
    Dim sMatUserName As String
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swConfig = swModel.GetActiveConfiguration
```

```
    Set swBody = swPart.Body
    Set swFace = swBody.GetFirstFace
    Debug.Print "SOLIDWORKS revision number   = " & swApp.RevisionNumber
    Debug.Print "  File = " & swModel.GetPathName
    Debug.Print "    Configuration name       = " & swConfig.Name
    Debug.Print "    Part material name       = " & swPart.MaterialIdName
    Debug.Print "    Part material user name  = " & swPart.MaterialUserName
    Debug.Print ""
```

```
    Do While Not swFace Is Nothing
        sMatName = swFace.MaterialIdName
        sMatUserName = swFace.MaterialUserName
        If sMatName <> "" Then
            Debug.Print "    Face material name (" & i & ")      = " & sMatName
        End If
        If sMatUserName <> "" Then
            Debug.Print "    Face material user name (" & i & ") = " & sMatUserName
        End If
        i = i + 1
        Set swFace = swFace.GetNextFace
    Loop
```

```
End Sub
```
