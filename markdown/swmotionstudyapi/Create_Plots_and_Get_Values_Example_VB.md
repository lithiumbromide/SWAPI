---
title: "Create Plots and Get Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Create_Plots_and_Get_Values_Example_VB.htm"
---

# Create Plots and Get Values Example (VBA)

This example shows how to get the translational displacement and velocity values for a selected face and how to plot these values.

```
'---------------------------------------------------------------------
' Preconditions:
' 1. Start SOLIDWORKS Premium, which includes SOLIDWORKS Motion.
' 2. In SOLIDWORKS:
'    a. Start the SOLIDWORKS Motion Study add-in (click Tools >
'       Add-Ins > SOLIDWORKS Motion).
'    b. Open public_documents\samples\tutorial\motionstudies\valve_cam.sldasm.
'    c. Click the 1200 Motion Study tab in the lower-left corner of
'       the MotionManager.
'    d. Select Motion Analysis in the Type of Study list at the
'       upper-left corner of the MotionManager.
' 3. In the IDE:
'    a. Add a reference to the SOLIDWORKS MotionStudy type library.
'    b. Open the Immediate window.
'
' Postconditions:
' 1. Selects two faces.
' 2. Calculates the motion analysis for the two selected faces.
' 3. Gets the translational displacement and translational velocity
'    values for the first selected face.
' 4. Creates plots of the translational displacement and translational
'    velocity.
' 5. Prints the names of the plot features to the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'---------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                               As SldWorks.SldWorks
    Dim swModel                             As SldWorks.ModelDoc2
    Dim swSelMgr                            As SldWorks.SelectionMgr
    Dim swModelDocExt                       As SldWorks.ModelDocExtension
    Dim MotionMgr                           As SwMotionStudy.MotionStudyManager
    Dim MotionStudy                         As SwMotionStudy.MotionStudy
    Dim MotionStudyResults                  As SwMotionStudy.CosmosMotionStudyResults
    Dim status                              As Boolean
    Dim swSimPlotFeatureData                As SldWorks.MotionPlotFeatureData
    Dim swSimPlotXAxisFeatureData           As SldWorks.MotionPlotAxisFeatureData
    Dim swSimPlotYAxisFeatureData(0 To 1)   As SldWorks.MotionPlotAxisFeatureData
    Dim swFace(0 To 0)                      As SldWorks.Face2
    Dim swFaceArray                         As Variant
    Dim swYAxisArray                        As Variant
    Dim PlotOutput                          As SwMotionStudy.MotionPlotFeatureOutput
    Dim swPlotFeature1                      As SldWorks.Feature
    Dim swPlotFeature2                      As SldWorks.Feature
    Dim swXData                             As Variant
    Dim swYData                             As Variant
    Dim nameYAxis(0 To 1)                   As String
    Dim i                                   As Long
    Dim j                                   As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
```

```
    ' Select the faces for which to calculate
    ' motion analysis, then calculate it and
    ' get the results
    swModel.ShowNamedView2 "*Right", 4
    status = swModelDocExt.SelectByID2("", "FACE", 0.03426699306681, 0.03342024416822, 0.02599934303839, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 0.03047373686337, 0.006937653650944, 0.02566622869226, True, 0, Nothing, 0)
    Set MotionMgr = swModelDocExt.GetMotionStudyManager()
    Set MotionStudy = MotionMgr.GetMotionStudy("1200")
    status = MotionStudy.Calculate
    Set MotionStudyResults = MotionStudy.GetResults(4)
```

```
    ' Create a plot feature data and create the  x and y axes feature data
    Set swSimPlotFeatureData = MotionStudyResults.CreatePlotFeatureData()
    Set swSimPlotXAxisFeatureData = MotionStudyResults.CreatePlotXAxisFeatureData()
    Set swSimPlotYAxisFeatureData(0) = MotionStudyResults.CreatePlotYAxisFeatureData()
    Set swSimPlotYAxisFeatureData(1) = MotionStudyResults.CreatePlotYAxisFeatureData()
```

```
    ' Set the type of plots
    nameYAxis(0) = "swMotionPlotAxisType_TRANS_DISP"
    swSimPlotYAxisFeatureData(0).Type = SwConst.swMotionPlotAxisType_TRANS_DISP
    swSimPlotYAxisFeatureData(0).Component = 1
    nameYAxis(1) = "swMotionPlotAxisType_TRANS_VELOCITY"
    swSimPlotYAxisFeatureData(1).Type = SwConst.swMotionPlotAxisType_TRANS_VELOCITY
    swSimPlotYAxisFeatureData(1).Component = 1
```

```
    ' Get the entity whose motion you want analyzed
    Set swFace(0) = swSelMgr.GetSelectedObject6(1, -1)
    swFaceArray = swFace
    swSimPlotYAxisFeatureData(0).Entities = swFaceArray
    swSimPlotYAxisFeatureData(1).Entities = swFaceArray
```

```
    ' Get the plot's x-axis and y-axes values
    swYAxisArray = swSimPlotYAxisFeatureData
    Set PlotOutput = MotionStudyResults.GetValues(swSimPlotFeatureData, swSimPlotXAxisFeatureData, (swYAxisArray))
    swXData = PlotOutput.GetXAxis()
```

```
    ' Print the x-axis values and the y-axis translational
    ' displacement values and the y-axes translational velocity
    ' values to the Immediate window
    Debug.Print ""
    For i = 0 To UBound(swYAxisArray)
        Debug.Print "------ YAxis Type : " & nameYAxis(i)
        swYData = PlotOutput.GetYAxis(swSimPlotYAxisFeatureData(i))
        For j = 0 To UBound(swXData)
            Debug.Print " (x, y) : (" & Strings.Format(swXData(j)) & ", " & swYData(j) & ")"
        Next j
    Next i
```

```
    ' Insert and display the translational displacement plot
    Set swPlotFeature1 = MotionStudyResults.InsertPlotFeature(swSimPlotFeatureData, swSimPlotXAxisFeatureData, swSimPlotYAxisFeatureData(0))
    Debug.Print "Name of plot feature: " & swPlotFeature1.Name
```

```
    ' Insert and display the translational velocity plot
    Set swPlotFeature2 = MotionStudyResults.InsertPlotFeature(swSimPlotFeatureData, swSimPlotXAxisFeatureData, swSimPlotYAxisFeatureData(1))
    Debug.Print "Name of plot feature: " & swPlotFeature2.Name
```

```
End Sub
```
