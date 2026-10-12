---
title: "Get GTol Witness Line Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_GTol_Witness_Line_Example_VB.htm"
---

# Get GTol Witness Line Example (VBA)

This example shows how to get the witness line of a geometric tolerance frame.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\GTolWitnessLine.slddrw
 ' 2. Select the frame.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. The position of the Gtol is modified.
 ' 2. Inspect the Immediate window for the witness line
 '    start and end point coordinates.
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 '---------------------------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim selGtol As SldWorks.Gtol
 Dim i As Long
 Dim params As Variant
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager
     Set selGtol = swSelMgr.GetSelectedObject6(1, 0)

    selGtol.SetPosition 0.433, 0.432, 0#
     swModel.ForceRebuild3 False
    params = selGtol.GetWitnessLine

    For i = 0 To UBound(params)
         Debug.Print params(i)
     Next i

End Sub
```
