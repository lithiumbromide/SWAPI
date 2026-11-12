---
title: "Get General Table Annotation Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_General_Table_in_Part_Example_VB.htm"
---

# Get General Table Annotation Example (VBA)

This example shows how to create a general table annotation for 3D PDF files in SOLIDWORKS MBD.

```
'--------------------------------------------------------------------------
' Preconditions: Open a part.
'
' Postconditions: None.
'--------------------------------------------------------------------------
```

```
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
    Set myTable = modelDocExt.GetGeneralTableAnnotation(True, 0, 0, swBOMConfigurationAnchor_TopLeft, "", 2, 2)
```

```
End Sub
```
