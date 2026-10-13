---
title: "Create and Flip Flat-Pattern View of Sheet Metal Part Example (VB)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Flip_Flat-Pattern_View_of_Sheet_Metal_Part_Example_VB.htm"
---

# Create and Flip Flat-Pattern View of Sheet Metal Part Example (VB)

This example shows how to create and flip a flat-pattern view of a sheet metal part.

```vb
'------------------------------------------
'
' Problem:
'       The drawing view must be of the part in a flattened
'       state and without bend lines. This is necessary so the
'       file is suitable for export to DXF for subsequent import
'       into laser cutting software, which normally only requires
'       the outline of the profile to be cut.
'
' Preconditions:
'       1) Sheet metal part is open.
'       2) Adjust paper template size, height, and width.
'
' Postconditions:
'       Anew A1 sized drawing is generated with
'       a flattened view of the sheet metal part
'       with no bend lines showing.
'
'-------------------------------------------
Option Explicit

Public Enum swDwgPaperSizes_e
    swDwgPaperAsize = 0
    swDwgPaperAsizeVertical = 1
    swDwgPaperBsize = 2
    swDwgPaperCsize = 3
    swDwgPaperDsize = 4
    swDwgPaperEsize = 5
    swDwgPaperA4size = 6
    swDwgPaperA4sizeVertical = 7
    swDwgPaperA3size = 8
    swDwgPaperA2size = 9
    swDwgPaperA1size = 10
    swDwgPaperA0size = 11
    swDwgPapersUserDefined = 12
End Enum

Public Enum swDwgTemplates_e
    swDwgTemplateAsize = 0
    swDwgTemplateAsizeVertical = 1
    swDwgTemplateBsize = 2
    swDwgTemplateCsize = 3
    swDwgTemplateDsize = 4
    swDwgTemplateEsize = 5
    swDwgTemplateA4size = 6
    swDwgTemplateA4sizeVertical = 7
    swDwgTemplateA3size = 8
    swDwgTemplateA2size = 9
    swDwgTemplateA1size = 10
    swDwgTemplateA0size = 11
    swDwgTemplateCustom = 12
    swDwgTemplateNone = 13
End Enum

' Paper size in millimeters
'   A     216 x 279
'   B     279 x 432
'   C     432 x 559
'   D     559 x 864
'   E     864 x 1118
'
'   A0    841 x 1189
'   A1    594 x 841
'   A2    420 x 594
'   A3    297 x 420
'   A4    210 x 297

Const TemplateSize          As Long = swDwgTemplateA1size
Const PaperSize             As Long = swDwgPaperA1size
Const PaperWidth            As Double = 0.841   ' Meters
Const PaperHeight           As Double = 0.594   ' Meters

Sub main()

    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swDraw                  As SldWorks.DrawingDoc
    Dim swView                  As SldWorks.View
    Dim bRet                    As Boolean

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swDraw = swApp.NewDrawing2(TemplateSize, "", PaperSize, _
                    PaperWidth, PaperHeight)

     Set swView = swDraw.CreateFlatPatternViewFromModelView3( _
                    swModel.GetPathName, "", _
                    PaperWidth / 2, PaperHeight / 2, 0#, True, True)

     Debug.Print swView.GetName2
     Debug.Print swView.FlipView

     swView.FlipView = False
     Debug.Print swView.FlipView

End Sub
```
