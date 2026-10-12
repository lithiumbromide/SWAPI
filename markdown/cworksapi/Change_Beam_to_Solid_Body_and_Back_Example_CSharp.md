---
title: "Change Beam to Solid Body and Back Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Change_Beam_to_Solid_Body_and_Back_Example_CSharp.htm"
---

# Change Beam to Solid Body and Back Example (C#)

This example shows how to change a beam to a solid body and then back to a beam.

```vb
//---------------------------------------------------------------------------
// Preconditions:
// 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
//    Tools > Add-ins > SOLIDWORKS Simulation > OK).

// 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

//    (in the IDE, click Project > Add Reference > .NET >
//    SolidWorks.Interop.cosworks > OK).
// 3. Open the Immediate window.

// 4. Ensure that the specified part exists.
//
// Postconditions: Examine the the Immediate window to verify
// that beams were converted to solid bodies and then back to beams.
// You can also expand and examine the Simulation Study tree to verify the
// macro.
//
// NOTES: Because the part document is used elsewhere, do not save changes.
//-------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;
namespace BeamToSolidSolidToBeamCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            CosmosWorks COSMOSWORKS = default(CosmosWorks);
            CwAddincallback COSMOSObject = default(CwAddincallback);
            CWModelDoc ActDoc = default(CWModelDoc);
            CWStudyManager StudyMngr = default(CWStudyManager);
            CWStudy Study = default(CWStudy);
            CWBeamManager BeamMgr = default(CWBeamManager);
            CWBeamBody BeamBody = default(CWBeamBody);
            CWSolidManager SolidMgr = default(CWSolidManager);
            CWSolidComponent SolidComponent = default(CWSolidComponent);
            CWSolidBody SolidBody = default(CWSolidBody);
            int nbrBeamBodies = 0;
            int beamBodyType = 0;
            int errors = 0;
            int warnings = 0;
            int errCode = 0;
            int j = 0;
            int nbrSolidComponents = 0;
            int nbrSolidBodies = 0;
            int k = 0;

            //Get the SOLIDWORKS Simulation object
            COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
            if (COSMOSObject == null) ErrorMsg("No CwAddincallback object");
            COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
            if (COSMOSWORKS == null) ErrorMsg("No COSMOSWORKS object");
            //Open and get the active document
            swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Beams\\Beam_Truss.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
            if (ActDoc == null) ErrorMsg("No active document");
            //Get the study
            StudyMngr = (CWStudyManager)ActDoc.StudyManager;
            if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
            StudyMngr.ActiveStudy = 0;
            Study = (CWStudy)StudyMngr.GetStudy(0);
            if (Study == null) ErrorMsg("No study at that index");

            //Get and set beams to solids and solids to beams
            Debug.Print("Beams...");
            BeamMgr = (CWBeamManager)Study.BeamManager;
            nbrBeamBodies = BeamMgr.BeamCount;
            Debug.Print(" Number of beams: " + nbrBeamBodies);
            BeamBody = null;
            //Convert beams to solid bodies
            for (j = 0; j <= (nbrBeamBodies - 1); j++)
            {
                BeamBody = (CWBeamBody)BeamMgr.GetBeamBodyAt(0, out errCode);
                if (errCode != 0) ErrorMsg("No beam body");
                Debug.Print("   Name of beam body: " + BeamBody.BeamBodyName);
                beamBodyType = BeamBody.BeamType;
                if (beamBodyType == 0)
                {
                    BeamBody.ConvertToSolidBody();
                    Debug.Print("     Beam converted to solid body");
                }
                BeamBody = null;
            }
            Debug.Print(" ");

            // Convert solid bodies to beams
            Debug.Print("Solid components and bodies...");
            // Get solid bodies and components
            SolidMgr = (CWSolidManager)Study.SolidManager;
            if (SolidMgr == null) ErrorMsg("No CWSolidManager object");
            nbrSolidComponents = SolidMgr.ComponentCount;
            Debug.Print(" Number of solid components: " + nbrSolidComponents);
            for (j = 0; j <= (nbrSolidComponents - 1); j++)
            {
                SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(j, out errCode);
                if (SolidComponent == null) ErrorMsg("No solid component");
                Debug.Print("   Name of solid components: " + SolidComponent.ComponentName);
                // Get solid bodies
                nbrSolidBodies = SolidComponent.SolidBodyCount;
                Debug.Print("     Number of solid bodies: " + nbrSolidBodies);
                for (k = 0; k <= (nbrSolidBodies - 1); k++)
                {
                    SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(0, out errCode);
                    if (errCode != 0) ErrorMsg("No solid body");
                    Debug.Print("       Name of solid body: " + SolidBody.SolidBodyName);
                    SolidBody.ConvertToBeamBody();
                    Debug.Print("         Solid body converted to beam");
                    SolidBody = null;
                }
            }
        }

        private void ErrorMsg(string Message)
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
