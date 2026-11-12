---
title: "Get GTol Witness Line Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_GTol_Witness_Line_Example_VBNET.htm"
---

# Get GTol Witness Line Example (VB.NET)

This example shows how to get the witness line of a geometric tolerance frame.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\GTolWitnessLine.slddrw
 ' 2. Select the geometric tolerance frame.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. The position of the Gtol is modified.
 ' 2. Inspect the Immediate window for the witness line
 '    start and end point coordinates.
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 '--------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim selGtol As Gtol
     Dim i As  Long
     Dim params As Object

     Sub main()

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swSelMgr = swModel.SelectionManager
         selGtol = swSelMgr.GetSelectedObject6(1, 0)

         selGtol.SetPosition(0.433, 0.432, 0#)
         swModel.ForceRebuild3(False)

         params = selGtol.GetWitnessLine

         For i = 0 To UBound(params)
             Debug.Print(params(i))
         Next i
     End Sub

     Public swApp As SldWorks

 End  Class
```
