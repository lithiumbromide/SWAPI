---
title: "Create Base-Flange Feature Using Gauge Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm"
---

# Create Base-Flange Feature Using Gauge Table Example (VBA)

This examples shows how to create a sheet metal part with a base-flange feature using a gauge table.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template and sheet
'    metal gauge table files exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a part document containing a sketch.
' 2. Sets some values for the base flange feature.
' 3. Gets and prints the sheet metal gauge table thickness names
'    and available bend radii to the Immediate window.
' 4. Using the sketch, creates a sheet metal part with
'    a base flange feature.
' 5. Examine the FeatureManager design tree and Immediate window.
'-----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSketchManager As SldWorks.SketchManager
    Dim featDef As SldWorks.BaseFlangeFeatureData
    Dim sketchLines As Variant
    Dim thicknessNames As Variant
    Dim radii As Variant
    Dim override As Boolean
    Dim boolstatus As Boolean
    Dim feat As Object
    Dim i As Long
    Dim j As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
```

```
    swModel.ClearSelection2 True
```

```
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    boolstatus = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    Set swSketchManager = swModel.SketchManager
    sketchLines = swSketchManager.CreateCornerRectangle(0, 0, 0, 0.107090305712461, -6.06697840413517E-02, 0)
    swSketchManager.InsertSketch True
```

```
    Set swFeatMgr = swModel.FeatureManager
    Set featDef = swFeatMgr.CreateDefinition(swFmBaseFlange)
    featDef.BendRadius = 0.02
    featDef.D1OffsetDistance = 0.04
    featDef.D1OffsetType = 1
    featDef.D1ReverseOffset = True
    featDef.D2OffsetDistance = 0.001
    featDef.D2OffsetType = 1
    featDef.D2ReverseOffset = True
    featDef.OffsetDirections = 1
    featDef.ReverseDirection = False
    featDef.ReverseThickness = False
```

```
    ' All of the following values depend on the previous values;
    ' you must set these values in sequence
    featDef.UseGaugeTable = True
```

```
    ' Set the path to the sheet metal gauge tables
    featDef.GaugeTablePath = "c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\Sheet Metal Gauge Tables\sample table - steel - english units.xls"
```

```
    thicknessNames = featDef.GetTableThicknesses()
```

```
    If (IsEmpty(thicknessNames)) Then
        MsgBox "Invalid path to sheet metal gauge table file."
        End
    End If
```

```
    Debug.Print "Sheet metal gauge table thickness names and available bend radii:"
    For i = 0 To UBound(thicknessNames)
        Debug.Print "  " & thicknessNames(i)
        radii = featDef.GetTableRadii(thicknessNames(i))
        For j = 0 To UBound(radii)
            Debug.Print "    " & radii(j)
        Next
    Next i
```

```
    ' Use the values from the previously called method to set the following values
    Debug.Print ""
    featDef.ThicknessTableName = thicknessNames(3)
    Debug.Print "Table thickness name for this sheet metal part: " & thicknessNames(3)
    'Convert meters to inches by multiplying value by 39.37
    Debug.Print "  Thickness: " & (featDef.TableThickness * 39.37) & " inches"
```

```
    ' Get updated radii for new table, which was previously set
    radii = featDef.GetTableRadii(thicknessNames(3))
    featDef.TableRadius = radii(3)
    'Convert meters to inches by multiplying value by 39.37
    Debug.Print "  Bend radius: " & (radii(3) * 39.37) & " inches"
```

```
    ' Set override values
    override = False
    If (override = True) Then
        featDef.OverrideRadius = True
        featDef.OverrideThickness = True
        featDef.OverrideKFactor = True
    Else
        featDef.OverrideRadius = False
        featDef.OverrideThickness = False
        featDef.OverrideKFactor = False
    End If
```

```
    ' If above override value is true, then use following properties to set override value
    If (override = True) Then
        featDef.Thickness = "0.06"
        featDef.BendRadius = 0.012
        featDef.KFactor = 0.75
    End If
```

```
    swModel.ShowNamedView2 "*Trimetric", 8
    boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
```

```
    ' Create the feature
    Set feat = swFeatMgr.CreateFeature(featDef)
```

```
End Sub
```
