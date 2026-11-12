---
title: "Create Circular Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Circular_Pattern_Example_CSharp.htm"
---

# Create Circular Pattern Example (C#)

This example shows how to create a circular-pattern feature using selected direction axis, pattern seed features, and variable spacing between pattern instances.

```
//----------------------------------------------------------------------------
// Preconditions: Open public_documents\samples\tutorial\api\varyinstance.sldprt
//
// Postconditions: Creates a circular-pattern feature.
//
// NOTE: Because the model is used elsewhere, do not save changes.
//-----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace CreateCircularPatternCSharp.csproj
{

    partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureMgr = default(FeatureManager);
            bool boolstatus = false;
            int status = 0;

            swModel = (ModelDoc2)swApp.ActivateDoc3("varyInstance.sldprt", false, (int)swRebuildOnActivation_e.swUserDecision, ref status);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            boolstatus = swModelDocExt.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0.00843730075439453, 0.00364341890551145, -0.0354416044676498, false, 4, null, 0);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to select a seed feature"); }

            boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.00628473027779819, -0.168045059787516, -0.0496550391792034, true, 1, null, 0);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to select an edge for direction 1"); }

            boolstatus = swModelDocExt.SelectByID2("Fillet1", "BODYFEATURE", 0.000782948437176856, 0.00455320522434022, -0.0350770617062892, true, 4, null, 0);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to select a seed feature"); }

            swFeatureMgr = (FeatureManager)swModel.FeatureManager;

            boolstatus = swFeatureMgr.InsertVaryInstanceIncrement("D1@Sketch2@varyInstance.SLDPRT", 4, 1, 0, 0.003);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to add an increment value to dimension D1@Sketch2@varyInstance.SLDPRT"); }

            boolstatus = swFeatureMgr.InsertVaryInstanceIncrement("D1@Cut-Extrude1@varyInstance.SLDPRT", 4, 1, 0, -0.001);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to add an increment value to dimension D1@Cut-Extrude1@varyInstance.SLDPRT"); }

            boolstatus = swFeatureMgr.InsertVaryInstanceIncrement("D1@Fillet1@varyInstance.SLDPRT", 4, 1, 0, 0.0001);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to add an increment value to dimension D1@Fillet1@varyInstance.SLDPRT"); }

            boolstatus = swFeatureMgr.InsertVaryInstanceIncrement("Space Increment", 4, 2, 0, 0.0349065850398866);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to add an increment value to direction 1 spacing"); }

            boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Sketch2@varyInstance.SLDPRT", 4, 1, -1, 5, -1, 0.05);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to override value of dimension D1@Sketch2@varyInstance.SLDPRT at instance (5, 0)"); }

            boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Sketch2@varyInstance.SLDPRT", 4, 1, -1, 3, -1, 0.06);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to override value of dimension D1@Sketch2@varyInstance.SLDPRT at instance (3, 0)"); }

            boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Cut-Extrude1@varyInstance.SLDPRT", 4, 1, -1, 5, -1, 0.005);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to override value of dimension D1@Cut-Extrude1@varyInstance.SLDPRT at instance (5, 0)"); }

            boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Fillet1@varyInstance.SLDPRT", 4, 1, -1, 5, -1, 0.006);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to override value of dimension D1@Fillet1@varyInstance.SLDPRT at instance (5, 0)"); }

            boolstatus = swFeatureMgr.InsertVaryInstanceOverride("D1@Fillet1@varyInstance.SLDPRT", 4, 1, -1, 3, -1, 0.004);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to override value of dimension D1@Fillet1@varyInstance.SLDPRT at instance (3, 0)"); }

            boolstatus = swFeatureMgr.InsertVaryInstanceOverride("Space Increment", 4, 2, 0, 5, -1, 1.30899693899575);
            if (boolstatus == false) { ErrorMsg(swApp, "Failed to override value of direction 1 spacing increment at instance (3, 0)"); }

            Feature myFeature = default(Feature);
            myFeature = (Feature)swFeatureMgr.FeatureCircularPattern4(6, 0.174532925199434, true, "NULL", false, false, true);
            if (myFeature == null) { ErrorMsg(swApp, "Failed to create a vary instance circular pattern"); }

        }

        public string ErrorMsg(SldWorks SwApp, string Message)
        {
            SwApp.SendMsgToUser2(Message, 0, 0);
            SwApp.RecordLine("'*** WARNING - General");
            SwApp.RecordLine("'*** " + Message);
            SwApp.RecordLine("");
            return "";
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
