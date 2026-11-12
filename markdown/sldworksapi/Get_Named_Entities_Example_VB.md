---
title: "Get Named Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Named_Entities_Example_VB.htm"
---

# Get Named Entities Example (VBA)

This example shows how to get named entities.

```
'-----------------------------------------------
' Preconditions:
' 1. Part document with one or more named entities
'    (faces, surfaces, bodies, or edges) is open.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number of named entities and their
'    names.
' 2. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
     Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swPart As SldWorks.PartDoc
     Dim vNamedEntity As Variant
     Dim swEnt As Entity
     Dim nEntCount As Long
     Dim i As Long
```

```
     Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swPart = swModel
```

```
    ' Get the full path name for the part
     Debug.Print "File = " & swModel.GetPathName
```

```
    ' Determine the total number of named entities
    ' in the part and print that value
     Debug.Print "  Number named entities = " & swPart.GetNamedEntitiesCount
     If swPart.GetNamedEntitiesCount = 0 Then
        Debug.Print "  No named entities."
        Exit Sub
     End If
     Debug.Print ""
     vNamedEntity = swPart.GetNamedEntities
     For i = 0 To UBound(vNamedEntity)
         Set swEnt = vNamedEntity(i)
        ' Print the name of each named entity
         Debug.Print "  Entity(" & i & ") = " & swPart.GetEntityName(swEnt)
     Next i
```

```
 End Sub
```
