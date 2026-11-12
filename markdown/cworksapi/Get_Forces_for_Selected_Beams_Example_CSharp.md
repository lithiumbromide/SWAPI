---
title: "Get Forces for Selected Beams (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Forces_for_Selected_Beams_Example_CSharp.htm"
---

# Get Forces for Selected Beams (C#)

## Get Forces for Selected Beams Example (C#)

This example shows how to get the force load values for structural members.

```vb
//--------------------------------------------------------------------------
// Preconditions:
// 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
//    Tools > Add-ins > SOLIDWORKS Simulation > OK).

// 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

//    (in the IDE, click Project > Add Reference > .NET >
//    SolidWorks.Interop.cosworks > OK).
// 3. Open the Immediate window.
// 4. Open a SOLIDWORKS model that has structural members and a
//    Simulation static study with structural force loads on the
//    beams.
// 5. Select the Simulation study tab.
// 6. Click the Run button on the Simulation CommandManager to
//    refresh the study results.
// 7. In the Simulation Study tree, select the beams for which
//    you want to know their force loads.
// 8. Run the macro.
//
// Postconditions: The selected beams' forces are printed to the
// the Immediate window.
//-------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;
namespace ListBeamForcesCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            CosmosWorks COSMOSWORKS = default(CosmosWorks);
            CwAddincallback COSMOSObject = default(CwAddincallback);
            CWModelDoc ActDoc = default(CWModelDoc);
            CWStudyManager StudyMngr = default(CWStudyManager);
            CWStudy Study = default(CWStudy);
            CWBeamManager BeamMgr = default(CWBeamManager);
            CWResults Results = default(CWResults);
            int actStudy = 0;
            int beamForce = 0;
            int nbrSteps = 0;
            int unit = 0;
            int errCode = 0;
            object[] selBeams = null;
            int nbrSelectedBeams = 0;
            int i = 0;
            int k = 0;

            // Connect to SOLIDWORKS
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            // Get the SOLIDWORKS Simulation object
            COSMOSObject = (CwAddincallback)swApp.GetAddInObject("Sldworks.Simulation");
            if (COSMOSObject == null) ErrorMsg("COSMOSObject object not found");
            COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
            if (COSMOSWORKS == null) ErrorMsg("COSMOSWORKS object not found");

            // Get the active document
            ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
            if (ActDoc == null) ErrorMsg("No active document");

            // Get the active study
            StudyMngr = (CWStudyManager)ActDoc.StudyManager;
            if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
            actStudy = StudyMngr.ActiveStudy;
            Study = (CWStudy)StudyMngr.GetStudy(actStudy);
            if (Study == null) ErrorMsg("Study not created");

            // Get the results
            Results = (CWResults)Study.Results;

            // Get the selected beams' forces
            BeamMgr = (CWBeamManager)Study.BeamManager;
            beamForce = (int)swsBeamForceType_e.swsBeamForceMomentDirection1;
            nbrSteps = 1;
            unit = (int)swsUnit_e.swsUnitSI;

            nbrSelectedBeams = swSelMgr.GetSelectedObjectCount2(-1);
            selBeams = new object[nbrSelectedBeams];
            for (k = 1; k <= nbrSelectedBeams; k++)
            {
                selBeams[k-1] = (object)swSelMgr.GetSelectedObject6(k, -1);
            }

            Object arrBeamForces = Results.GetBeamForcesForEntities(beamForce, nbrSteps, (selBeams), unit, out errCode);
            Array BeamForces = (Array)arrBeamForces;

            for (i = 0; i <= BeamForces.GetUpperBound(0); i++)
            {
                string beamForceElement = "";
                beamForceElement = Convert.ToString(BeamForces.GetValue(i));
                Debug.Print (beamForceElement);
            }

        }

        //Error routine
        private void ErrorMsg(string Message)
        {
            swApp.SendMsgToUser2(Message, 0, 0);
            swApp.RecordLine("'*** WARNING - General");
            swApp.RecordLine("'*** " + Message);
            swApp.RecordLine("");
        }
        public SldWorks swApp;
    }

}
```
