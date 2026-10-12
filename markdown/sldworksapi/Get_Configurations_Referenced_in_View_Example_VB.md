---
title: "Get Configurations Referenced in View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Configurations_Referenced_in_View_Example_VB.htm"
---

# Get Configurations Referenced in View Example (VBA)

This example shows how to get the names and persistent reference IDs of the configurations referenced in each drawing view in the first drawing sheet.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a drawing document with multiple
'    drawing views and multiple referenced
'    configurations in the first drawing sheet
'    in the drawing.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the drawing views in the first
'    drawing sheet and gets each drawing view's:
'    *  name
'    *  referenced model name
'    *  referenced configuration name and
'       persistent reference ID
' 2. Examine the Immediate window.
'---------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    ' First drawing view is actually the first drawing sheet,
    ' so skip getting model name and configuration from
    ' the drawing sheet
    Set swView = swDraw.GetFirstView
    ' Get first drawing view in first drawing sheet
    Set swView = swView.GetNextView
    Do While Not swView Is Nothing
        Debug.Print "  Drawing view = " + swView.Name
        Debug.Print "    Referenced model name = " & swView.GetReferencedModelName
        Debug.Print "    Referenced configuration name = " & swView.ReferencedConfiguration
        Debug.Print "    Referenced configuration persistent reference ID = " & swView.ReferencedConfigurationID
        'Get next drawing view
        Set swView = swView.GetNextView
    Loop
```

```
End Sub
```
