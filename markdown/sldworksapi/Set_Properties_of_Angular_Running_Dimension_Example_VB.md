---
title: "Insert Angular Running Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Properties_of_Angular_Running_Dimension_Example_VB.htm"
---

# Insert Angular Running Dimension Example (VBA)

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
 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim selmgr As SldWorks.SelectionMgr
 Dim dispdimvar As Variant
 Dim dispdim As SldWorks.DisplayDimension
 Dim boolstatus As Boolean
 Dim errstatus as Long
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    boolstatus = Part.ActivateView("Drawing View1")
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.163726736787323, 0.199115091463415, 4.79999999993197E-03, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.220795425811714, 0.179644597560976, 4.79999999998881E-03, True, 0, Nothing, 0)

    Set dispdimvar = Part.Extension.AddAngularRunningDim(False, True, True, 0.154288188900673, 7.94194886913027E-02, 0, errstatus)
     Part.Extension.ReJogRunningDimension
     Part.Extension.AlignRunningDimension

    Part.SetPickMode

    boolstatus = Part.Extension.SelectByID2("D2@Sketch31@foodprocessor.SLDDRW", "DIMENSION", 4.08612062995185E-02, 0.166216670731707, 0, False, 0, Nothing, 0)
     Set selmgr = Part.SelectionManager
     Set dispdim = selmgr.GetSelectedObject6(1, -1)

    Debug.Print "Display chained angular dimensions? " & dispdim.DisplayAsChain
     Debug.Print "Run the angular dimensions bidirectionally? " & dispdim.RunBidirectionally
     Debug.Print "Extend extension lines from center of angular running dimension? " & dispdim.ExtensionLineExtendsFromCenterOfSet
     Debug.Print "Are extension lines jogged? " & dispdim.Jogged
     Debug.Print "Extension line style same as leader line style? " & dispdim.ExtensionLineSameAsLeaderStyle
     Debug.Print "Extension line uses document settings? " & dispdim.ExtensionLineUseDocumentDisplay

End Sub
```
