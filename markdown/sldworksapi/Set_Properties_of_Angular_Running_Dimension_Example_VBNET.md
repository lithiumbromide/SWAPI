---
title: "Insert Angular Running Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm"
---

# Insert Angular Running Dimension Example (VB.NET)

This example shows how to insert an angular running dimension and get its properties.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. The specified angular running dimension is inserted into the drawing.
 ' 2. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes to it.
 ' ---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim Part As ModelDoc2
         Dim selmgr As SelectionMgr
         Dim dispdim As DisplayDimension
         Dim dispdimvar As Object
         Dim boolstatus As Boolean
         Dim errstatus as Integer

         Part = swApp.ActiveDoc

         boolstatus = Part.ActivateView("Drawing View1")
         boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.163726736787323, 0.199115091463415, 0.00479999999993197,  True, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.220795425811714, 0.179644597560976, 0.00479999999998881,  True, 0, Nothing, 0)

         dispdimvar = Part.Extension.AddAngularRunningDim(False, True, True, 0.154288188900673, 0.0794194886913027, 0, errstatus)
         Part.Extension.ReJogRunningDimension()
         Part.Extension.AlignRunningDimension()

         Part.SetPickMode()

         boolstatus = Part.Extension.SelectByID2("D2@Sketch31@foodprocessor.SLDDRW", "DIMENSION", 0.0408612062995185, 0.166216670731707, 0,  False, 0, Nothing, 0)
         selmgr = Part.SelectionManager
         dispdim = selmgr.GetSelectedObject6(1, -1)

         Debug.Print("Display chained angular dimensions? " & dispdim.DisplayAsChain)
         Debug.Print("Run the angular dimensions bidirectionally? " & dispdim.RunBidirectionally)
         Debug.Print("Extend extension lines from center of angular running dimension? " & dispdim.ExtensionLineExtendsFromCenterOfSet)
         Debug.Print("Are extension lines jogged? " & dispdim.Jogged)
         Debug.Print("Extension line style same as leader line style? " & dispdim.ExtensionLineSameAsLeaderStyle)
         Debug.Print("Extension line uses document settings? " & dispdim.ExtensionLineUseDocumentDisplay)

     End Sub

     Public swApp As SldWorks

 End Class
```
