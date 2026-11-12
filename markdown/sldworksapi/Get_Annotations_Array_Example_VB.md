---
title: "Get Annotations Arrays Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Annotations_Array_Example_VB.htm"
---

# Get Annotations Arrays Example (VBA)

Methods added to the IView interface in SOLIDWORKS API 2009 SP1 can return arrays of each annotation type in a drawing view. This example shows how to call these methods.

```
'-----------------------------------------------------------------------------
' Preconditions: Verify that the specified path and template file exist.
'
' Postconditions:
' 1. Creates a part with annotations.
' 2. Click Save.
' 3. Creates a drawing with third-angle views of the part
'    and annotations.
' 4. Iterates through each annotation array and pops up message boxes
'    containing information about each annotation in the drawing views.
' 5. Click OK to close each message box.
'---------------------------------------------------------------------------
Option Explicit
```

```
Const filedir As String = "C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\"
Const TemplateName As String = "C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\Drawing.drwdot"
Const TemplateSize As Long = swDwgTemplateBsize
Const PaperSize As Long = swDwgPaperBsize
Const ScaleNum As Double = 1#
Const ScaleDenom As Double = 2#
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeatMgr As SldWorks.FeatureManager
Dim Response As Integer
Dim ThirdAngle As Boolean
Dim swDraw As SldWorks.DrawingDoc
Dim swSheet As SldWorks.Sheet
Dim i As Long
Dim j As Long
Dim retval As Boolean
Dim swView As SldWorks.View
Dim count As Long
Dim Annotations As Variant
Dim msg As String
```

```
Sub main()
```

```
    'Create a part
    Build_Part
```

```
        'Create a drawing of the part
        Set swApp = Application.SldWorks
        Set swModel = swApp.ActiveDoc
        Set swDraw = swApp.NewDocument(TemplateName, PaperSize, 0#, 0#)
```

```
        ThirdAngle = False
        swDraw.ActivateSheet "Sheet1"
        Set swSheet = swDraw.GetCurrentSheet
        swSheet.SetSize PaperSize, 0#, 0#
        swSheet.SetScale ScaleNum, ScaleDenom, True, True

        ' Create third-angle drawing views
        ' Pop up Save As dialog
        ' Click Save in the dialog
        retval = swDraw.Create3rdAngleViews2(swModel.GetPathName)
```

```
        Dim LocX As Double
        Dim LocY As Double
        LocX = 0.2635088599471
        LocY = 0.1934578136726
```

```
        ' Create isometric drawing view
        swDraw.CreateDrawViewFromModelView3 swModel.GetPathName, "*Isometric", LocX, LocY, 0
        swDraw.ViewDisplayShaded
```

```
        ' Insert display dimension annotations
        ' from the current model
        swDraw.InsertModelAnnotations3 0, swInsertDimensionsMarkedForDrawing, True, True, False, True
```

```
         ' Insert datum target symbol annotations
         ' from the current model
        swDraw.InsertModelAnnotations3 0, swInsertDatumTargets, True, True, False, True
```

```
        ' Insert geometric tolerance annotations
        ' from the current model
        swDraw.InsertModelAnnotations3 0, swInsertGTols, True, True, False, True
```

```
        ' Insert surface finish symbol annotations
        ' from the current model
        swDraw.InsertModelAnnotations3 0, swInsertSFSymbols, True, True, False, True
```

```
        ' Insert datum tag annotations from the current model
        swDraw.InsertModelAnnotations3 0, swInsertDatums, True, True, False, True
```

```
        swDraw.ForceRebuild3 True
```

```
        ' Iterate through all the views on the
        ' drawing to find display dimensions
        Set swView = swDraw.GetFirstView
        Do While Not swView Is Nothing
            count = swView.GetDisplayDimensionCount
            Dim DisplayDimension As SldWorks.DisplayDimension
            Dim swDim As SldWorks.Dimension
            ' Iterate through all the display dimension
            ' annotations in each drawing view that has them
            If count > 0 Then
                Annotations = swView.GetDisplayDimensions
                For j = 0 To UBound(Annotations)
                    Set DisplayDimension = Annotations(j)
                    Set swDim = DisplayDimension.GetDimension
                    ' For each annotation in each drawing view,
                    ' pop up a message box with the
                    ' annotation name and corresponding dimension
                    msg = "Display dimension found: " & swView.GetName2 & ":" & DisplayDimension.GetAnnotation.GetName & " = " & swDim.GetSystemValue2("") & " meters"
                    swApp.SendMsgToUser2 msg, swMbInformation, swMbOk
                Next j
            End If
            Set swView = swView.GetNextView
        Loop
```

```
        ' Iterate through all the views on the drawing
        ' to find datum target symbols
        Set swView = swDraw.GetFirstView
        Do While Not swView Is Nothing
            count = swView.GetDatumTargetSymCount
            Dim dtsymbol As SldWorks.DatumTargetSym
            ' Iterate through all the datum target symbol
            ' annotations in each drawing view that has them
            If count > 0 Then
                Annotations = swView.GetDatumTargetSyms
                For j = 0 To UBound(Annotations)
                    Set dtsymbol = Annotations(j)
                    ' For each annotation in each drawing view,
                    ' pop up a message box with the
                    ' annotation name and name of each
                    ' datum target symbol found
                    msg = "Datum target symbol found: " & swView.GetName2 & ":" & dtsymbol.GetAnnotation.GetName
                    swApp.SendMsgToUser2 msg, swMbInformation, swMbOk
                Next j
            End If
            Set swView = swView.GetNextView
        Loop
```

```
        ' Iterate through all the views on the drawing
        ' to find surface finish symbols
        Set swView = swDraw.GetFirstView
        Do While Not swView Is Nothing
            count = swView.GetSFSymbolCount
            Dim sfsymbol As SldWorks.sfsymbol
            ' Iterate through all the surface
            ' finish symbol annotations in each
            ' drawing view that has them
            If count > 0 Then
                Annotations = swView.GetSFSymbols
                For j = 0 To UBound(Annotations)
                    Set sfsymbol = Annotations(j)
                    ' For each annotation in each drawing
                    ' view, pop up a message box with the
                    ' annotation name and name of each
                    ' surface finish symbol found
                    msg = "Surface finish symbol found: " & swView.GetName2 & ":" & sfsymbol.GetAnnotation.GetName
                    swApp.SendMsgToUser2 msg, swMbInformation, swMbOk
                Next j
            End If
            Set swView = swView.GetNextView
        Loop
```

```
        ' Iterate through all the views on the
        ' drawing to find datum tags
        Set swView = swDraw.GetFirstView
        Do While Not swView Is Nothing
            count = swView.GetDatumTagCount
            Dim dTag As SldWorks.DatumTag
            ' Iterate through all the datum tags
            ' in each drawing view that has them
            If count > 0 Then
                Annotations = swView.GetDatumTags
                For j = 0 To UBound(Annotations)
                    Set dTag = Annotations(j)
                    ' For each annotation in each drawing view,
                    ' pop up a message box with the
                    ' annotation name and name
                    ' of each datum tag found
                    msg = "Datum tag found: " & swView.GetName2 & ":" & dTag.GetAnnotation.GetName
                    swApp.SendMsgToUser2 msg, swMbInformation, swMbOk
                Next j
            End If
            Set swView = swView.GetNextView
        Loop
```

```
        ' Iterate through all the views on the
        ' drawing to find geometric tolerances
        Set swView = swDraw.GetFirstView
        Do While Not swView Is Nothing
            count = swView.GetGTolCount
            Dim gtol As SldWorks.gtol
            ' Iterate through all the geometric
            ' tolerance symbols in each drawing view
            ' that has them
            If count > 0 Then
                Annotations = swView.GetGTols
                For j = 0 To UBound(Annotations)
                    Set gtol = Annotations(j)
                    ' For each annotation in each drawing
                    ' view, pop up a message box with the
                    ' annotation name and name of each
                    ' geometric tolerance found
                    msg = "Geometric tolerance symbol found: " & swView.GetName2 & ":" & gtol.GetAnnotation.GetName
                    swApp.SendMsgToUser2 msg, swMbInformation, swMbOk
                Next j
            End If
            Set swView = swView.GetNextView
        Loop
```

```
        ' In a similar fashion:
        ' Get other annotations on the drawing, if they exist
        ' Iterate through all the views on the drawing
        ' Get the annotation count, and if greater than zero,
        ' get the annotation array
        ' Iterate on each array, and set an annotation object
        ' to each array member
        ' Annotations = swView.GetDowelSymbols
        ' Annotations = swView.GetMultiJogLeaders
        ' Annotations = swView.GetDatumOrigins
        ' Annotations = swView.GetCenterLines
        ' Annotations = swView.GetCThreads
        ' Annotations = swView.GetWeldSymbols
        ' Annotations = swView.GetWeldBeads
        ' Annotations = swView.GetTableAnnotations
```

```
        swApp.SetUserPreferenceToggle swInputDimValOnCreate, True
        swModel.SetUserPreferenceToggle swDisplayAnnotations, False
```

```
    End Sub
```

```
    Private Sub Build_Part()
    ' Build a part with these annotations:
    ' display dimensions, geometric tolerance
    ' symbol, surface finish symbol,
    ' datum tag symbol, and datum target symbol
        Set swApp = Application.SldWorks
        Set swModel = swApp.NewDocument(filedir + "Part.prtdot", 0, 0#, 0#)
        swModel.SetUserPreferenceIntegerValue swUnitsLinear, swMETER
        swModel.SetUserPreferenceDoubleValue swMaterialPropertyDensity, 7800
        swModel.SetUserPreferenceStringValue swMaterialPropertyCrosshatchPattern, "ISO (Steel)"
        swModel.SketchManager.InsertSketch False

        Dim Height As Double
        Dim Width As Double
        Height = 0.05
        Width = 0.05
```

```
        swApp.SetUserPreferenceToggle swInputDimValOnCreate, False
        swModel.SketchManager.CreateLine 0.01, 0.01, 0, 0.01, 0.01 + Height, 0

        swModel.ViewZoomtofit2
```

```
        ' Add display dimension to line
        swModel.AddDimension2 0, 0.01 + Height / 2, 0
```

```
        ' Add geometric tolerance to line
        swModel.InsertGtol
        swModel.SketchManager.CreateLine 0.01, 0.01, 0, 0.01 + Width, 0.01, 0

        swModel.ViewZoomtofit2
```

```
        ' Add display dimension
        swModel.AddDimension2 0.01 + Width / 2, 0, 0
```

```
        ' Add surface finish symbol to line
        swModel.Extension.InsertSurfaceFinishSymbol3 swSFBasic, swSTRAIGHT, 0.01, 0.01, 0.01, swSFCircular, swDOT_ARROWHEAD, "", "", "", "", "", "", ""
```

```
        swModel.SketchManager.CreateLine(0, 0, 0, 0, 0.01, 0).ConstructionGeometry = True
```

```
        swModel.ClearSelection2 True
        swModel.ViewZoomtofit2
```

```
        Dim Thick As Double
        Thick = 0.05
```

```
        Dim Depth As Double
        Depth = 0.05
        Set swFeatMgr = swModel.FeatureManager
        swFeatMgr.FeatureExtrusionThin2 True, False, True, 0, 0, Depth, 0, False, False, False, False, 0, 0, False, False, False, False, False, Thick, 0, 0, 0, 0, False, False, False, False, swStartSketchPlane, 0#, False
```

```
        swModel.ViewZoomtofit2
        swModel.SetUserPreferenceToggle swDisplayAnnotations, True
        swModel.ShowNamedView2 "Isometric", 7
        swModel.ViewZoomtofit2
```

```
        ' Add datum tag to line
        retval = swModel.Extension.SelectByID2("", "EDGE", 0.06001738353251, -0.01284975502705, -0.05001738353241, False, 0, Nothing, 0)
        Dim dTag As SldWorks.DatumTag
        Set dTag = swModel.InsertDatumTag2
```

```
       ' Add datum target symbol to line
        retval = swModel.Extension.SelectByID2("", "EDGE", 0.06001738353251, -0.01284975502705, -0.05001738353241, False, 0, Nothing, 0)
        Dim myDatumTarget As Object
        Set myDatumTarget = swModel.Extension.InsertDatumTargetSymbol2("", "", "", 0, False, 0.03, 0.03, "", "", True, 12, 0, False, True, True)
```

```
End Sub
```
