---
title: "Get Material Database Paths of Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Material_Database_Paths_of_Document_Example_VB.htm"
---

# Get Material Database Paths of Document Example (VBA)

This example shows how to get the paths and names of the material databases for a part.

NOTE: Material database names must be unique. Do not re-use the name of a material database.

```
'----------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\fillets\knob.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of the part's material databases.
' 2. Examine the Immediate window.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim dbs As Variant
    Dim sMatName As String
    Dim sMatDB As String
    Dim bRet As Boolean
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
```

```
    dbs = swApp.GetMaterialDatabases
```

```
    sMatName = swPart.GetMaterialPropertyName2("Default", sMatDB)
    For i = 0 To LBound(dbs)
        If StrComp(Left(Right(dbs(i), Len(sMatDB) + 7), Len(sMatDB)), sMatDB) = 0 Then
            Debug.Print dbs(i)
        End If
    Next i
```

```
End Sub
```
