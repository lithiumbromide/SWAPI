---
title: "Create General Table Annotation for SOLIDWORKS MBD 3D PDF Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_General_Table_for_SOLIDWORKS_3D_PDF_Example_VBNET.htm"
---

# Create General Table Annotation for SOLIDWORKS MBD 3D PDF Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swTable As TableAnnotation

    Sub main()

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swTable = swModelDocExt.GetGeneralTableAnnotation(True, 0, 0, swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, "", 2, 2)
        If (swTable Is Nothing) Then
            Debug.Print("Failed to create general table annotation!")
            Exit Sub
        Else
            Debug.Print("Succeeded in creating general table annotation!")
        End If
        Debug.Print(" Total number of rows: " & swTable.TotalRowCount)
        Debug.Print(" Total number of columns: " & swTable.TotalColumnCount)

    End Sub

    Public swApp As SldWorks

End Class
```
