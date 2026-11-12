---
title: "Create General Table Annotation for SOLIDWORKS MBD 3D PDF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_General_Table_for_SOLIDWORKS_3D_PDF_Example_VB.htm"
---

# Create General Table Annotation for SOLIDWORKS MBD 3D PDF Example (VBA)

This example shows how to create a general table annotation for SOLIDWORKS MBD 3D PDF.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a general table annotation for SOLIDWORKS MBD 3D PDF.
' 2. Examine the Immediate window.
'--------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swTable As SldWorks.TableAnnotation
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swTable = swModelDocExt.GetGeneralTableAnnotation(True, 0, 0, swBOMConfigurationAnchor_TopLeft, "", 2, 2)
```

```
    Set swTable = swModelDocExt.GetGeneralTableAnnotation(True, 0, 0, swBOMConfigurationAnchor_TopLeft, "", 2, 2)
    If (swTable Is Nothing) Then
        Debug.Print "Failed to create general table annotation!"
        Exit Sub
    Else
        Debug.Print "Succeeded in creating general table annotation!"
    End If
```

```
    Debug.Print " Total number of rows: " & swTable.TotalRowCount
    Debug.Print " Total number of columns: " & swTable.TotalColumnCount
```

```
End Sub
```
