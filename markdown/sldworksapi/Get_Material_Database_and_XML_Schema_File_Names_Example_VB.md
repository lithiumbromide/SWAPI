---
title: "Get Material Database and XML Schema File Names Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Material_Database_and_XML_Schema_File_Names_Example_VB.htm"
---

# Get Material Database and XML Schema File Names Example (VBA)

This example shows how to get the names of the the path of the XML material schema file and the names of the material databases.

```
'-------------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions:
' 1. Gets the path of the XML material schema file
'    and the names of the material databases.
' 2. Examine the Immediate window.
'-------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim vMatDBarr As Variant
    Dim vMatDB As Variant
```

```
    Set swApp = Application.SldWorks
    vMatDBarr = swApp.GetMaterialDatabases
    Debug.Print "Material schema path name = " & swApp.GetMaterialSchemaPathName
    For Each vMatDB In vMatDBarr
        Debug.Print "  " & vMatDB
    Next
```

```
End Sub
```
