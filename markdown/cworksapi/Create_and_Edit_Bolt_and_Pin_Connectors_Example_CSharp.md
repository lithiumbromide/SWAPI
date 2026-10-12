---
title: "Create and Edit Bolt and Pin Connectors Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm"
---

# Create and Edit Bolt and Pin Connectors Example (C#)

This example shows how to:

- add a bolt connector to the Connections in a SOLIDWORKS Simulation static study, using persistent reference identifier (PIDs) for entity selections.
- change the bolt connector's default values, apply library material, and set pre-load.
- edit an existing pin connector connection.

The model used in this example had four extrudes (three bosses and one cut resulting in four holes), a static study with a Pin Connector-1 connection, and looked like this:

NOTE: To get persistent reference identifiers (PIDs) for model selections, you can use [pidcollector.exe](GettingStarted-swsimulationapi.html) or IModelDocExtension::GetPersistReference3.

```vb
//---------------------------------------------------------------------------
// Preconditions:
// 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
//    Tools > Add-ins > SOLIDWORKS Simulation > OK).

// 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

//    (in the IDE, click Project > Add Reference > .NET >
//    SolidWorks.Interop.cosworks > OK).
// 3. Model shown is the active document in SOLIDWORKS.
// 4. Ensure that the specified material library exists.
//
// Postconditions: A bolt connector called Counterbore with Nut-2
// is added to the study.
//
//-------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;
using System.Collections;
using System.Text;
namespace BoltConnectorCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 Part = default(ModelDoc2);
            CosmosWorks COSMOSWORKS = default(CosmosWorks);
            CwAddincallback COSMOSObject = default(CwAddincallback);
            CWModelDoc ActDoc = default(CWModelDoc);
            CWStudyManager StudyMngr = default(CWStudyManager);
            CWStudy Study = default(CWStudy);
            CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
            CWBoltConnector CWBolt = default(CWBoltConnector);
            CWPinConnector CWPin = default(CWPinConnector);
            int errCode = 0;
            byte[] var1 = null;
            byte[] var2 = null;
            object pDisp1 = null;
            object pDisp2 = null;
            ArrayList PIDCollection = new ArrayList();

            PIDCollection = PIDInitializer();

            // Get SOLIDWORKS Simulation object
            COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
            if (COSMOSObject == null) ErrorMsg(swApp, "No CwAddincallback object");
            COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
            if (COSMOSWORKS == null) ErrorMsg(swApp, "No COSMOSWORKS object");

            // Get active SOLIDWORKS part document
            Part = (SolidWorks.Interop.sldworks.ModelDoc2)swApp.ActiveDoc;
            ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;

            // Get study manager and study
            StudyMngr = (CWStudyManager)ActDoc.StudyManager;
            Study = StudyMngr.GetStudy(0);

            // Get PIDs for the selections
            // Edge of a hole
            SelectByPID("selection1", PIDCollection, ref var1);
            // Opposite edge of hole
            SelectByPID("selection2", PIDCollection, ref var2);

            pDisp1 = (object)Part.Extension.GetObjectByPersistReference3((var1), out errCode);
            pDisp2 = (object)Part.Extension.GetObjectByPersistReference3((var2), out errCode);

            // Create and initialize object array
            object[] DispArray1 = { pDisp1 };
            object[] DispArray2 = { pDisp2 };

            LBCMgr = (CWLoadsAndRestraintsManager)Study.LoadsAndRestraintsManager;

            // Add bolt connector
            CWBolt = (CWBoltConnector)LBCMgr.AddBoltConnector((int)swsBoltType_e.swsBoltTypeStandardOrCounterboreNut, (DispArray1), (DispArray2), ref errCode);
            // Edit bolt connector
            CWBolt.BoltConnectorBeginEdit();
            CWBolt.HeadDiameterUnit = 0;
            CWBolt.HeadDiameterValue = 5;
            CWBolt.BoltShankDiameterUnit = 0;
            CWBolt.BoltShankDiameterValue = 2.9;
            CWBolt.MaterialType = 1;
            CWBolt.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron (SN)");
            CWBolt.BoltUnit = 0;
            CWBolt.PreLoadForceType = 0;
            CWBolt.PreLoadForceValue = 0.85;
            CWBolt.FrictionValue = 0.3;
            errCode = CWBolt.BoltConnectorEndEdit();

            // Get Pin Connector-1
            CWPin = (CWPinConnector)LBCMgr.GetLoadsAndRestraints(0, out errCode);

            // Edit Pin Connector-1
            CWPin.PinConnectorBeginEdit();
            CWPin.IncludeTypeWithKey = false;
            CWPin.IncludeTypeWithRetainerRing = false;
            CWPin.Unit = 0;
            CWPin.AxialStiffnessValue = 1000;
            CWPin.RotationalStiffnessValue = 10000000.0;
            errCode = CWPin.PinConnectorEndEdit();
        }

        private void SelectByPID(string PIDName, ArrayList PIDCollection, ref byte[] varEntity)
        {
            // Select by PID
            byte[] PID = null;
            string[] PIDVariant = null;
            string PIDString = null;
            int i = 0;

            // Get string from array
            PIDString = "";
            switch(PIDName)
            {
                case "selection1":
                    PIDString = (string)PIDCollection[0];
                    break;
                case "selection2":
                    PIDString = (string)PIDCollection[1];
                    break;
                default:
                    break;
            }

            // Parse the string into an array
            PIDVariant = PIDString.Split(new char[] {','});

            // Convert string array to byte array
            int sizeArray  = PIDVariant.Length;
            PID = new byte[sizeArray];
            for (i = 0; i < PIDVariant.Length - 1; i++)
            {
                PID[i] = Convert.ToByte(PIDVariant[i]);
            }
            varEntity = PID;

}
        public ArrayList PIDInitializer()
        {
            // Initialize PIDs
            ArrayList PIDCollection = new ArrayList();
            string selection1 = null;
            string selection2 = null;
            // Constants
            selection1 = "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,184,1,0,0,17,1,0,0,120,1,157,80,189,78,195,48,24,188,242,87,42,64,136,13,169,11,12,172,8,149,9,24,105,163,68,20,129,146,142,72,81,112,156,210,82,59,40,184,18,11,82,38,158,128,7,224,5,88,120,5,102,120,10,158,163,230,220,144,169,27,182,228,179,239,190,251,62,157,191,182,129,101,0,118,102,121,18,109,3,27,80,121,47,29,202,80,102,177,104,204,105,96,197,225,82,245,120,254,124,61,120,15,62,6,53,86,182,93,103,211,169,151,8,121,28,104,19,77,139,44,72,67,249,16,139,74,95,163,238,133,177,112,35,182,92,237,147,185,186,29,75,97,42,106,135,212,121,100,138,145,30,250,137,78,39,146,244,204,238,123,56,197,13,174,81,32,199,24,18,2,6,143,216,67,7,71,220,39,212,212,156,189,67,2,141,17,53,133,67,68,232,163,75,87,136,1,90,37,251,180,22,171,24,230,231,66,248,168,19,254,5,117,95,209,236,178,103,198,142,83,76,56,175,94,29,94,212,165,240,157,227,237,165,242,185,52,109,151,172,200,85,116,111,122,218,44,132,95,45,215,113,70,203,55,173,77,16";
            selection1 = selection1 + "2,229,34,96,179,4,254,163,57,239,47,9,100,114,100,0,0,0,0,0,0,0,0";
            selection1 = selection1 + ",Type=1";
            selection2 = "35,29,213,113,218,129,72,162,168,88,152,178,27,137,239,153,184,1,0,0,20,1,0,0,120,1,157,80,189,78,195,48,24,188,242,87,42,64,136,13,137,5,6,54,132,16,76,192,72,27,37,2,4,74,42,38,164,40,56,78,105,105,28,20,92,137,165,82,38,158,128,7,224,5,88,120,5,102,120,10,158,163,230,92,147,169,27,182,228,207,190,239,187,59,157,191,214,129,121,0,102,98,120,178,154,6,86,144,23,157,180,39,67,153,197,162,49,133,129,5,91,231,220,99,252,249,186,251,30,124,116,235,234,104,91,164,121,101,145,71,15,186,163,244,81,160,116,52,42,179,32,13,229,99,44,220,200,146,29,9,99,97,93,214,172,203,179,190,186,27,72,161,29,180,65,232,44,210,101,95,245,252,68,165,67,73,120,98,118,60,156,224,22,215,40,81,96,0,9,1,141,39,108,227,16,7,220,199,236,229,83,244,30,9,20,250,236,229,216,71,132,11,180,201,10,209,69,171,162,78,107,118,138,121,126,206,133,143,58,228,95,86,251,27,205,54,53,51,42,142,48,164,95,189,78,121,249,190,20,126,147,213,112,89,220,166,217,180,105,84,234,37,66,206,36,95,172,150,177,199,185,27,242,";
            selection2 = selection2 + "172,211,219,139,243,91,173,128,255,244,40,129,95,173,223,107,131,0,0,0,0,0,0,0,0";
            selection2 = selection2 + ",Type=1";

            // Store constants in arrays
            PIDCollection.Add(selection1);
            PIDCollection.Add(selection2);

            // Pass the arrays back
            return PIDCollection;
        }

        private void ErrorMsg(SldWorks SwApp, string Message)
        {
            swApp.SendMsgToUser2(Message, 0, 0);
            swApp.RecordLine("'*** WARNING - General");
            swApp.RecordLine("'*** " + Message);
            swApp.RecordLine("");
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

}
}
```
