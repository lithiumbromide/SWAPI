---
title: "Save Table to Microsoft Excel Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Table_to_Microsoft_Excel_Example_VB.htm"
---

# Save Table to Microsoft Excel Example (VBA)

This example shows how to save a BOM table annotation to a Microsoft Excel document.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing of an assembly with a BOM.
 ' 2. Click the move-table icon in the upper-left corner
 '    of the BOM table to open the table's PropertyManager page.
 '
 ' Postconditions: Saves the selected BOM to c:\temp\BOMTable.xls.
 '--------------------------------------------------------------------------
 Dim swApp As SldWorks.SldWorks
 Dim swModDoc As SldWorks.IModelDoc2
 Dim swTable As SldWorks.ITableAnnotation

Option Explicit
Public Sub Main()
     Set swApp = Application.SldWorks

     Set swModDoc = swApp.ActiveDoc
     Dim swSM As ISelectionMgr
     Set swSM = swModDoc.SelectionManager
     Set swTable = swSM.GetSelectedObject6(1, -1)
     swModDoc.ClearSelection2 (True)

     Dim swSpecTable As IBomTableAnnotation
     Set swSpecTable = swTable
    ' Save the selected BOM table to Microsoft Excel, including hidden cells
     ' and images
     status = swSpecTable.SaveAsExcel("c:\temp\BOMTable.xls", True, True)
End Sub
```
