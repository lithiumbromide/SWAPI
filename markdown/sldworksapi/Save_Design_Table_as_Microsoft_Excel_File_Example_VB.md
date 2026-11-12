---
title: "Save Design Table as Microsoft Excel File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Design_Table_as_Microsoft_Excel_File_Example_VB.htm"
---

# Save Design Table as Microsoft Excel File Example (VBA)

This example shows how to save a design table to a Microsoft Excel file.

```vb
'-----------------------------------
'
' Preconditions: Document that has a design table is open
'
' Postcoditions: Design table is saved as a Microsoft
'                Excel file named DesignTable.xls
'
'------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks

Sub main()

    Dim swModel         As SldWorks.ModelDoc2
    Dim swDesignTable   As SldWorks.DesignTable
    Dim strFileName     As String
    Dim bValue          As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc

    Set swDesignTable = swModel.GetDesignTable

    swDesignTable.Attach

    bValue = swDesignTable.SaveAsExcelFile(swApp.GetCurrentMacroPathFolder & "\DesignTable.xls")

    ' Do not detach if table is not active
    If (Not (swDesignTable.IsActive = False)) Then
        swDesignTable.Detach
    End If

End Sub
```
