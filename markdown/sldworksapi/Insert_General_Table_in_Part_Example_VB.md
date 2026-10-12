---
title: "Insert General Table in Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_General_Table_in_Part_Example_VB.htm"
---

# Insert General Table in Part Example (VBA)

This example shows how to insert a general table annotation into a model document.

```
'---------------------------------------------------
' Preconditions: Open a part.
'
' Postconditions:
' 1. Inserts a general table in the part.
' 2. Examine the graphics area.
'---------------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim modelDocExt As SldWorks.ModelDocExtension
Dim myTable As SldWorks.TableAnnotation
```

```
Option Explicit
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    Set modelDocExt = Part.Extension
    Set myTable = modelDocExt.InsertGeneralTableAnnotation(True, 0, 0, swBOMConfigurationAnchor_TopLeft, "", 2, 2)
```

```
End Sub
```
