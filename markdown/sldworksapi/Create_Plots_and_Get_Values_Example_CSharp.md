---
title: "Create Plots and Get Values Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Plots_and_Get_Values_Example_CSharp.htm"
---

# Create Plots and Get Values Example (C#)

This example shows how to get the translational displacement and velocity values of a selected face and how to plot these values.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Start SOLIDWORKS Premium, which includes SOLIDWORKS Motion.
 // 2. In SOLIDWORKS Design:
 //    a. Start the SOLIDWORKS Motion Study add-in (in
 //       SOLIDWORKS Design, click Tools > Add-Ins > SOLIDWORKS Motion).
 //    b. Open public_documents\samples\tutorial\motionstudies\valve_cam.sldasm.
 //    c. Click the 1200 Motion Study tab in the lower-left corner of
 //       the MotionManager.
 //    d. Select Motion Analysis in the Type of Study list at the
 //       upper-left corner of the MotionManager.
 // 3. In the IDE:
 //    a. Add a reference to the SOLIDWORKS Motion Study primary interop assembly
 //       (right-click the name of the project in the Project Explorer >
 //       click Add Reference > browse to install_dir\api\redist >
 //       click SolidWorks.Interop.swmotionstudy.dll).
 //    b. Open the Immediate window.
 //
 // Postconditions:
 // 1. Selects two faces.
 // 2. Calculates the motion analysis for the two selected faces.
 // 3. Gets the translational displacement and translational velocity
 //    values for the first selected face.
 // 4. Creates plots of the translational displacement and translational
 //    velocity.
 // 5. Prints the names of the plot features to the Immediate window.
 //
 // NOTE: Because the assembly is used elsewhere, do not save changes.
 //-------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swmotionstudy;
 using System;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace CreatePlotFeaturesCSharp.csproj
 {

     partial  class  SolidWorksMacro
     {

         public  void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             MotionStudyManager MotionMgr = default(MotionStudyManager);
             MotionStudy MotionStudy = default(MotionStudy);
             CosmosMotionStudyResults MotionStudyResults =  default(CosmosMotionStudyResults);
             bool status = false;
             MotionPlotFeatureData swSimPlotFeatureData =  default(MotionPlotFeatureData);
             MotionPlotAxisFeatureData swSimPlotXAxisFeatureData =  default(MotionPlotAxisFeatureData);
             MotionPlotAxisFeatureData[] swSimPlotYAxisFeatureData =  new MotionPlotAxisFeatureData[2];
             Face2 swFace = default(Face2);
             Entity swEntity = default(Entity);
             object[] swFaceArray = new  object[1];
             Entity[] swEntityArray = new Entity[1];
             MotionPlotFeatureOutput PlotOutput =  default(MotionPlotFeatureOutput);
             Feature swPlotFeature1 = default(Feature);
             Feature swPlotFeature2 = default(Feature);
             double[] swXData = null;
             double[] swYData = null;
             string[] nameYAxis = new  string[2];
             int i = 0;
             int j = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Select the faces for which to calculate
             // motion analysis, then calculate it and
             // get the results
             swModel.ShowNamedView2("*Right", 4);
             status = swModelDocExt.SelectByID2("", "FACE", 0.03426699306681, 0.03342024416822, 0.02599934303839,  true, 0, null, 0);
             status = swModelDocExt.SelectByID2("", "FACE", 0.03047373686337, 0.006937653650944, 0.02566622869226,  true, 0,  null, 0);
             MotionMgr = (MotionStudyManager)swModelDocExt.GetMotionStudyManager();
             MotionStudy = (MotionStudy)MotionMgr.GetMotionStudy("1200");
             status = MotionStudy.Calculate();
             MotionStudyResults = (CosmosMotionStudyResults)MotionStudy.GetResults(4);

             // Create a plot feature data and create the  x and y axes feature data
             swSimPlotFeatureData = (MotionPlotFeatureData)MotionStudyResults.CreatePlotFeatureData();
             swSimPlotXAxisFeatureData = (MotionPlotAxisFeatureData)MotionStudyResults.CreatePlotXAxisFeatureData();
             swSimPlotYAxisFeatureData[0] = (MotionPlotAxisFeatureData)MotionStudyResults.CreatePlotYAxisFeatureData();
             swSimPlotYAxisFeatureData[1] = (MotionPlotAxisFeatureData)MotionStudyResults.CreatePlotYAxisFeatureData();

             // Set the type of plots
             nameYAxis[0] =  "swMotionPlotAxisType_TRANS_DISP";
             swSimPlotYAxisFeatureData[0].Type = (int)swMotionPlotAxisType_e.swMotionPlotAxisType_TRANS_DISP;
             swSimPlotYAxisFeatureData[0].Component = 1;
             nameYAxis[1] = "swMotionPlotAxisType_TRANS_VELOCITY";
             swSimPlotYAxisFeatureData[1].Type = (int)swMotionPlotAxisType_e.swMotionPlotAxisType_TRANS_VELOCITY;
             swSimPlotYAxisFeatureData[1].Component = 1;

             // Get the entity whose motion you want analyzed
             swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
             swEntity = (Entity)swFace;
             swEntityArray[0] = swEntity;

             swSimPlotYAxisFeatureData[0].Entities = swEntityArray;
             swSimPlotYAxisFeatureData[1].Entities = swEntityArray;

             // Get the plot's x-axis and y-axes values
             DispatchWrapper[] swYAxisArray = new  DispatchWrapper[2];
             swYAxisArray[0] = new DispatchWrapper(swSimPlotYAxisFeatureData[0]);
             swYAxisArray[1] = new DispatchWrapper(swSimPlotYAxisFeatureData[1]);
             PlotOutput = (MotionPlotFeatureOutput)MotionStudyResults.GetValues(swSimPlotFeatureData, swSimPlotXAxisFeatureData, (swYAxisArray));
             swXData = (double[])PlotOutput.GetXAxis();

             // Print the x-axis values and the y-axis translational
             // displacement values and the y-axes translational velocity
             // values to the Immediate window
             Debug.Print("");
             string x = "";
             string y = "";
             for (i = 0; i <= swYAxisArray.GetUpperBound(0); i++)
             {
                 Debug.Print("------ YAxis Type : " + nameYAxis[i]);
                 swYData = (double[])PlotOutput.GetYAxis(swSimPlotYAxisFeatureData[i]);
                 for (j = 0; j <= swXData.GetUpperBound(0); j++)
                 {

                     x = swXData[j].ToString();
                     y = swYData[j].ToString();
                     Debug.Print(" (x, y) : (" + x + ", " + y + ")");
                 }
             }

             // Insert and display the translational displacement plot
             swPlotFeature1 = (Feature)MotionStudyResults.InsertPlotFeature(swSimPlotFeatureData, swSimPlotXAxisFeatureData, swSimPlotYAxisFeatureData[0]);
            Debug.Print("Name of plot feature: " + swPlotFeature1.Name);

             // Insert and display the translational velocity plot
             swPlotFeature2 = (Feature)MotionStudyResults.InsertPlotFeature(swSimPlotFeatureData, swSimPlotXAxisFeatureData, swSimPlotYAxisFeatureData[1]);
             Debug.Print("Name of plot feature: " + swPlotFeature2.Name);

         }

         ///  <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
