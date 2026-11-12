---
title: "Get Chamfer Display Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Chamfer_Display_Dimension_Example_VBNET.htm"
---

# Get Chamfer Display Dimension Example (VB.NET)

This example shows how to get chamfer display dimension properties. This example also shows how to set and get lower display dimension text.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt.
' 2. Create a drawing from the part:
'    a. File > Make Drawing from Part.
'    b. Drag and drop the isometric view onto the sheet.
' 3. Create a chamfer display dimension.
'    a. Select Tools > Dimensions > Chamfer.
'    b. Select a chamfer edge.
'    c. Select a leading edge.
'    d. Click outside the part to place the display dimension.
'    e. Modify display dimension text in the PropertyManager:
'           1. In Dimension Text, click before <DIM>.
'           2. Select the diameter symbol.
'           3. Click after <DIM>.
'           4. Select the +/- symbol.
'           5. Type 0.5.
'           6. On the Other tab, select Override Units.
'           7. Click the green check mark to accept the
'              display dimension.
' 4. Open an Immediate Window.
' 5. Run the macro.
'
' Postconditions: Inspect the Immediate Window and the display
' dimension in the graphics area.
'
' NOTE: Because the part document is used elsewhere,
' do not save any changes when closing it.
'----------------------------------------------------------------
```

```vb
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swDispDim As DisplayDimension
     Dim bRet As Boolean
     Sub main()

         swModel = swApp.ActiveDoc

         swSelMgr = swModel.SelectionManager

         bRet = swModel.Extension.SelectByID2("RD1@Drawing View1",  "DIMENSION", 0.4935677398765, 0.3280800260301, 0, False, 0, Nothing, 0)
         swDispDim = swSelMgr.GetSelectedObject6(1, 0)
         swModel.ClearSelection2(True)

         Debug.Print("Dimension type as defined in swDimensionType_e: " & swDispDim.Type2) '10=swChamferDimension
         Debug.Print("")
         Debug.Print("Uses document units? " & swDispDim.GetUseDocUnits)  'false if uses local override units

         If swDispDim.GetUseDocUnits = False Then
             Dim LenUnit As Long
             Dim AngUnit As Long
             bRet = swDispDim.GetChamferUnits(LenUnit, AngUnit)
             Debug.Print("Uses local length unit as defined in swLengthUnit_e: " & LenUnit)  '0=swMM
             Debug.Print("Uses local angle unit as defined in swAngleUnit_e: " & AngUnit)   '0=swDegrees, 3=swRadians
         End If
         Debug.Print("")

         Dim indx As Long
         indx = swDispDim.ChamferPrecision(0)
         Debug.Print("Precision of chamfer distance: " & indx   " decimal places")
         indx = swDispDim.ChamferPrecision(1)
         Debug.Print("Precision of chamfer angle: " & indx   " decimal places")

         Dim tokenformats As Object = Nothing
         Dim tokenvalues As Object = Nothing
         Dim n As  Long

         Debug.Print("")
         Debug.Print("Text format items in " & swDispDim.GetNameForSelection   ":")
         Debug.Print("")
         Dim count As Long

         count = swDispDim.GetTextFormatItems(swDimensionTextParts_e.swDimensionTextCalloutAbove, tokenformats, tokenvalues)
         Debug.Print("Number of callout above items: " & count)

         If Not count = 0 Then
             Debug.Print("  tokenformats: ")
             For n = LBound(tokenformats) To UBound(tokenformats)
                 Debug.Print("  " & tokenformats(n))

             Next n
             Debug.Print("  tokenvalues: ")
             For n = LBound(tokenvalues) To UBound(tokenvalues)
                 Debug.Print("  " & tokenvalues(n))

             Next n
         End If
         Debug.Print("")
         count = swDispDim.GetTextFormatItems(swDimensionTextParts_e.swDimensionTextPrefix, tokenformats, tokenvalues)
         Debug.Print("Number of prefix items: " & count)
         If Not count = 0 Then
             Debug.Print("  tokenformats: ")
             For n = LBound(tokenformats) To UBound(tokenformats)
                 Debug.Print("  " & tokenformats(n))

             Next n
             Debug.Print("  tokenvalues: ")
             For n = LBound(tokenvalues) To UBound(tokenvalues)
                 Debug.Print("  " & tokenvalues(n))

             Next n
         End If
         Debug.Print("")
         count = swDispDim.GetTextFormatItems(swDimensionTextParts_e.swDimensionTextSuffix, tokenformats, tokenvalues)
         Debug.Print("Number of suffix items: " & count)

         If Not count = 0 Then
             Debug.Print("  tokenformats: ")
             For n = LBound(tokenformats) To UBound(tokenformats)
                 Debug.Print("  " & tokenformats(n))

             Next n
             Debug.Print("  tokenvalues: ")
             For n = LBound(tokenvalues) To UBound(tokenvalues)
                 Debug.Print("  " & tokenvalues(n))

             Next n
         End If
         Debug.Print("")
         count = swDispDim.GetTextFormatItems(swDimensionTextParts_e.swDimensionTextCalloutBelow, tokenformats, tokenvalues)
         Debug.Print("Number of callout below items: " & count)

         If Not count = 0 Then
             Debug.Print("  tokenformats: ")
             For n = LBound(tokenformats) To UBound(tokenformats)
                 Debug.Print("  " & tokenformats(n))

             Next n
             Debug.Print("  tokenvalues: ")
             For n = LBound(tokenvalues) To UBound(tokenvalues)
                 Debug.Print("" & tokenvalues(n))

             Next n
         End If
```

```
        ' Create lower display dimension text and enclose
        ' in parentheses
        swDispDim.SetLowerText("Example of lower text")
        swDispDim.ShowLowerParenthesis = True
```

```
        Debug.Print("")
        Debug.Print("Lower Dimension Text: " & swDispDim.GetLowerText)
        Debug.Print("  Show lower parenthesis: " & swDispDim.ShowLowerParenthesis)
        Debug.Print("  Show lower inspection:  " & swDispDim.LowerInspection)
        Debug.Print("  Split dual dimensions:  " & swDispDim.Split)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
