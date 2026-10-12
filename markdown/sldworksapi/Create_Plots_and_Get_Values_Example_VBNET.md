---
title: "Create Plots and Get Values Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Plots_and_Get_Values_Example_VBNET.htm"
---

# Create Plots and Get Values Example (VB.NET)

This example shows how to get the translational displacement and velocity values for a selected face and how to plot these values.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start SOLIDWORKS Premium, which includes SOLIDWORKS Motion.
 ' 2. In SOLIDWORKS Design:
 '    a. Start the SOLIDWORKS Motion Study add-in  (click Tools >
 '       Add-Ins > SOLIDWORKS Motion).
 '    b. Open public_documents\samples\tutorial\motionstudies\valve_cam.sldasm.
 '    c. Click the 1200 Motion Study tab in the lower-left corner of
 '       the MotionManager.
 '    d. Select Motion Analysis in the Type of Study list at the
 '       upper-left corner of the MotionManager.
 ' 3. In the IDE:
 '    a. Add a reference to the SOLIDWORKS Motion Study primary interop assembly
 '       (right-click the name of the project in the Project Explorer >
 '       click Add Reference > browse to install_dir\api\redist >
 '       click SolidWorks.Interop.swmotionstudy.dll).
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
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swmotionstudy
 Imports System
 Imports System.Diagnostics

 Partial  Class SolidWorksMacro

     Public  Sub Main()

         Dim swModel  As ModelDoc2
         Dim swSelMgr  As SelectionMgr
         Dim swModelDocExt As ModelDocExtension
         Dim MotionMgr As MotionStudyManager
         Dim MotionStudy As MotionStudy
         Dim MotionStudyResults As CosmosMotionStudyResults
         Dim status  As  Boolean
         Dim swSimPlotFeatureData As MotionPlotFeatureData
         Dim swSimPlotXAxisFeatureData As MotionPlotAxisFeatureData
         Dim swSimPlotYAxisFeatureData(0 To 1) As MotionPlotAxisFeatureData
         Dim swFace(0  To 0) As Face2
         Dim swFaceArray() As  Object
         Dim swYAxisArray() As  Object
         Dim PlotOutput As MotionPlotFeatureOutput
         Dim swPlotFeature1 As Feature
         Dim swPlotFeature2 As Feature
         Dim swXData  As  Object
         Dim swYData As  Object
         Dim nameYAxis(0 To 1)  As  String
         Dim i As  Integer
         Dim j As  Integer

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swModelDocExt = swModel.Extension

         ' Select the faces for which to calculate
         ' motion analysis, then calculate it and
         ' get the results
         swModel.ShowNamedView2("*Right", 4)
         status = swModelDocExt.SelectByID2("", "FACE", 0.03426699306681, 0.03342024416822, 0.02599934303839,  True, 0, Nothing, 0)
         status = swModelDocExt.SelectByID2("", "FACE", 0.03047373686337, 0.006937653650944, 0.02566622869226,  True, 0,  Nothing, 0)
         MotionMgr = swModelDocExt.GetMotionStudyManager()
         MotionStudy = MotionMgr.GetMotionStudy("1200")
         status = MotionStudy.Calculate
         MotionStudyResults = MotionStudy.GetResults(4)

         ' Create a plot feature data and create the  x and y axes feature data
         swSimPlotFeatureData = MotionStudyResults.CreatePlotFeatureData()
         swSimPlotXAxisFeatureData = MotionStudyResults.CreatePlotXAxisFeatureData()
         swSimPlotYAxisFeatureData(0) = MotionStudyResults.CreatePlotYAxisFeatureData()
         swSimPlotYAxisFeatureData(1) = MotionStudyResults.CreatePlotYAxisFeatureData()

         ' Set the type of plots
         nameYAxis(0) = "swMotionPlotAxisType_TRANS_DISP"
         swSimPlotYAxisFeatureData(0).Type = swMotionPlotAxisType_e.swMotionPlotAxisType_TRANS_DISP
         swSimPlotYAxisFeatureData(0).Component = 1
         nameYAxis(1) = "swMotionPlotAxisType_TRANS_VELOCITY"
         swSimPlotYAxisFeatureData(1).Type = swMotionPlotAxisType_e.swMotionPlotAxisType_TRANS_VELOCITY
         swSimPlotYAxisFeatureData(1).Component = 1

         ' Get the entity whose motion you want analyzed
         swFace(0) = swSelMgr.GetSelectedObject6(1, -1)
         swFaceArray = swFace
         swSimPlotYAxisFeatureData(0).Entities = swFaceArray
         swSimPlotYAxisFeatureData(1).Entities = swFaceArray

         ' Get the plot's x-axis and y-axes values
         swYAxisArray = swSimPlotYAxisFeatureData
         PlotOutput = MotionStudyResults.GetValues(swSimPlotFeatureData, swSimPlotXAxisFeatureData, (swYAxisArray))
         swXData = PlotOutput.GetXAxis()

         ' Print the x-axis values and the y-axis translational
         ' displacement values and the y-axes translational velocity
         ' values to the Immediate window
         Debug.Print("")
         For i = 0  To UBound(swYAxisArray)
             Debug.Print("------ YAxis Type : " & nameYAxis(i))
             swYData = PlotOutput.GetYAxis(swSimPlotYAxisFeatureData(i))
             For j = 0 To UBound(swXData)
                  Debug.Print(" (x, y) : (" & Strings.Format(swXData(j) & ", " & swYData(j) & ")"))
             Next j
         Next i

         ' Insert and display the translational displacement plot
         swPlotFeature1 = MotionStudyResults.InsertPlotFeature(swSimPlotFeatureData, swSimPlotXAxisFeatureData, swSimPlotYAxisFeatureData(0))
          Debug.Print("Name of plot feature: " & swPlotFeature1.Name)

         ' Insert and display the translational velocity plot
         swPlotFeature2 = MotionStudyResults.InsertPlotFeature(swSimPlotFeatureData, swSimPlotXAxisFeatureData, swSimPlotYAxisFeatureData(1))
          Debug.Print("Name of plot feature: " & swPlotFeature2.Name)

     End  Sub

     '''  <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     '''  </summary>
     Public swApp As SldWorks

 End  Class
```
