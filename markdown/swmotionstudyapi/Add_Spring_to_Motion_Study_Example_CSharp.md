---
title: "Add Spring to Motion Study (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Add_Spring_to_Motion_Study_Example_CSharp.htm"
---

# Add Spring to Motion Study (C#)

This example shows how to add a spring to a motion study.

```vb
//////////////////////////////////////////////////////////////////////////////////
//
// Preconditions:  (1) Open wrench.sldasm in any SOLIDWORKS 2009
//                    <install dir>\samples\whats new\motion study
//                     folder.
//
//                 (2) The MotionManager tab is visible. If it is not visible,
//                     click View, MotionManager.
//
//                 (3) SOLIDWORKS MotionStudy type library is
//                     referenced.
//
// Postconditions: Spring feature is added between the grips of the wrench.
//
//                NOTE: Do not save the model after running the macro. The model
//                      is intended for use with the SOLIDWORKS 2009 "What's New"
//                      book. The model is used in this example for demonstration
//                      purposes only.
//////////////////////////////////////////////////////////////////////////////////
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SwMotionStudy;
using System;
using System.Diagnostics;
namespace ExampleCS.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            MotionStudyManager swMotionMgr;
            MotionStudy swMotionStudy1;
            SimulationSpringFeatureData swSpringFeat;
            bool boolstatus;
            Feature swFeat;
            SelectionMgr swSelMgr;

            swModel = swApp.ActiveDoc as ModelDoc2;
            swModelDocExt = swModel.Extension;
            swSelMgr = swModel.SelectionManager as SelectionMgr;

            // Get the MotionManager
            swMotionMgr = swModelDocExt.GetMotionStudyManager() as MotionStudyManager;
            if ((swMotionMgr == null))
            {
                return;
            }

            // Get "MotionStudy1_Distance=0.5in"
            swMotionStudy1 = swMotionMgr.GetMotionStudy("MotionStudy1_Distance=0.5in");
            if ((swMotionStudy1 == null))
            {
                swApp.SendMsgToUser("MotionStudy1_Distance=0.5in is not available.");
                return;
            }

            // Activate swMotionStudy1
            swMotionStudy1.Activate();

            // Define spring feature
            swSpringFeat = swMotionStudy1.CreateDefinition((int)swFeatureNameID_e.swFmAEMLinearMotionSpring) as SimulationSpringFeatureData;
            if (swSpringFeat == null)
            {
                Debug.Print("ERROR: Creation of Spring feature data object failed.");
                return;
            }

            // Select spring's endpoints
            Face2 swFace1;
            Face2 swFace2;
            swModel.ShowNamedView2("*Left", 3);
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03344586330968, 0.0525345575174, 0, true, 0, null, 0);
            swFace1 = swSelMgr.GetSelectedObject6(1, -1) as Face2;
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02244533711473, 0.0131288302002, 2.238961779386E-04, true, 0, null,
0);
            swFace2 = swSelMgr.GetSelectedObject6(2, -1) as Face2;

           // Set spring's characteristics
            swSpringFeat.SetEndPoints(swFace1, swFace2);
            swSpringFeat.CoilDiameter = 0.0102;
            swSpringFeat.NumberOfCoils = 3;
            swSpringFeat.WireDiameter = 0.00152;
            swSpringFeat.FreeLength = 0.02;

            // Create Spring feature
            swFeat = swMotionStudy1.CreateFeature(swSpringFeat) as Feature;
            if (swFeat == null)
            {
                Debug.Print(" ERROR: Creation of the Spring feature failed.");
            }
            else
            {
                Debug.Print("Type of the feature added: " + swFeat.GetTypeName2());
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
