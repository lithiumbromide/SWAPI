---
title: "Set Rounding of Decimal Units in Display Dimensions (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_VB.htm"
---

# Set Rounding of Decimal Units in Display Dimensions (VBA)

This example shows how to specify the rounding of decimal units in display dimensions.

```vb
'----------------------------------------------------------------------------
 ' Preconditions: Open:
 '    public_documents\samples\tutorial\api\box.slddrw
 '
 ' Postconditions:
 ' 1. Click the display dimension in the graphics area.
 ' 2. Under Dual Dimension on the Value tab, observe that Inward rounding
 '    is selected.
 ' 3. Under Override Units on the Other tab, observe that:
 '    * Decimal is clicked.
 '    * Feet & Inches is selected.
 '    * Truncate without rounding is selected.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
Dim swApp                   As SldWorks.SldWorks
 Dim Part                    As SldWorks.ModelDoc2
 Dim swSelMgr                As SldWorks.SelectionMgr
 Dim swDispDim               As SldWorks.DisplayDimension
 Dim boolstatus              As Boolean
 Dim longstatus              As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    Set swSelMgr = Part.SelectionManager
     boolstatus = Part.Extension.SelectByID2("RD1@Drawing View1", "DIMENSION", 0.305961854224123, 0.247549077953509, 0, False, 0, Nothing, 0)
     Set swDispDim = swSelMgr.GetSelectedObject6(1, 0)

    longstatus = swDispDim.SetUnits2(False, swLengthUnit_e.swFEETINCHES, swFractionDisplay_e.swDECIMAL, 0, False, swUnitsDecimalRounding_e.swUnitsDecimalRounding_Truncate)
     Call swDispDim.SetDual2(False, True)
End Sub
```
