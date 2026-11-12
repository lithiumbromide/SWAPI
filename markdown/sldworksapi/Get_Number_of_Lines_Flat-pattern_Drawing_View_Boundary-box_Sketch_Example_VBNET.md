---
title: "Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm"
---

# Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)

This example shows how to get the number of lines in a flat-pattern drawing view's boundary-box sketch.

```vb
'----------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\SMGussetAPI.SLDPRT.
 ' 2. Create a new drawing document.
 ' 3. Select SMGussetAPI.SLDPRT in the View
 '    Palette's dropdown list box.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Examine the Immediate window and the drawing.
 ' 2. If necessary, drag the drawing onto the drawing sheet
 '    and zoom in on the drawing view.
 '
 ' NOTE: Because the part is used elsewhere, do not save
 ' changes.
 '---------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial  Class SolidWorksMacro

     Public  Sub Main()

         Dim swModel  As ModelDoc2
         Dim swDrawing As DrawingDoc
         Dim swView  As View
         Dim swSheet  As Sheet
         Dim swDisplayData As DisplayData
         Dim sheetProperties As  Object
         Dim sheetScale As  Double
         Dim paperSize As swDwgPaperSizes_e
         Dim width  As  Double
         Dim height As  Double
         Dim numViews As  Long
         Dim viewName As  Object
         Dim viewNames As  Object
         Dim viewPaletteName As  String =  ""
         Dim drawingViewName As  String =  ""
         Dim status As  Boolean

         swModel = swApp.ActiveDoc
         swDrawing = swModel

         ' Get current sheet
         swSheet = swDrawing.GetCurrentSheet
         sheetProperties = swSheet.GetProperties
         sheetScale = sheetProperties(2) / sheetProperties(3)
         paperSize = swSheet.GetSize(width, height)

         ' Get number of views on View Palette
         numViews = 0
         viewNames = swDrawing.GetDrawingPaletteViewNames

         ' Iterate through views on View Palette
         ' When view name equals "Flat pattern", drop
         ' that view in drawing
         If Not (IsNothing(viewNames)) Then
             numViews = (UBound(viewNames) - LBound(viewNames))
             For  Each viewName  In viewNames
                 viewPaletteName = viewName
                 If (viewPaletteName = "Flat pattern")  Then
                     Debug.Print("Dropping View Palette view named: " & viewPaletteName)
                     swView = swDrawing.DropDrawingViewFromPalette2(viewPaletteName, 0.0#, 0.0#, 0.0#)
                     drawingViewName = swView.GetName2
                     Debug.Print("Dropped View Palette view into drawing view named: " & drawingViewName)
                     Exit For
                 End  If
             Next viewName
         End  If

         ' Activate view and get number of lines in
         ' its boundary box sketch
         status = swDrawing.ActivateView(drawingViewName)
         swView = swDrawing.ActiveDrawingView

         ' Make sure the bounding box sketch is visible
         status = swModel.Extension.SelectByID2("Bounding-Box2@SMGussetAPI-1@DrawingView1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.UnblankSketch()
        swDisplayData = swView.GetSMBoundaryBoxDisplayData2
         Debug.Print("Number of lines in boundary box of flat-pattern drawing view: " & swDisplayData.GetLineCount)

     End  Sub

     '''  <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     '''  </summary>
     Public swApp As SldWorks

 End   Class
```
