---
title: "Get and Set Beams and Joints Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_and_Set_Beams_and_Joints_Example_CSharp.htm"
---

# Get and Set Beams and Joints Example (C#)

This example shows how to get and set beams and joints.

```vb
//--------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified part exists.
 // 4. Ensure that the specified material library exists.
 // 5. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates static study, frame.
 // 2. Prints beam information to the Immediate window.
 // 3. Applies Plain Carbon Steel material to all beams.
 // 4. Calculates joints for all beams and displays a neutral axis for
 //    each beam.
 // 5. Prints the pinball tolerance value and unit to the Immediate window.
 // 6. Creates a mixed mesh and prints its type and state to the
 //    Immediate window.
 //
 // NOTES:
 // *  Creates beam elements by default for parts with structural members.
 // *  Because the part document is used elsewhere, do not save any changes.
 //----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;
namespace Macro1.csproj
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
            CWJoints Joints = default(CWJoints);
            CWMesh Mesh = default(CWMesh);
            int nbrBeamBodies = 0;
            int beamBodyType = 0;
            double ElementSize = 0;
            double Tolerance = 0;
            int errors = 0;
            int warnings = 0;
            int errCode = 0;
            bool boolCode = false;
            int j = 0;
             bool keepJointUpdates = true;

            //Get the SOLIDWORKS Simulation object
            COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
            if (COSMOSObject == null) ErrorMsg("COSMOSObject object not found");
            COSMOSWORKS = COSMOSObject.CosmosWorks;
            if (COSMOSWORKS == null) ErrorMsg("COSMOSWORKS object not found");

            //Open and get the active document
            swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\weldments\\weldment_box2.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
            if (ActDoc == null) ErrorMsg("No active document");

            //Create new static study named frame
            StudyMngr = (CWStudyManager)ActDoc.StudyManager;
            if (StudyMngr == null) ErrorMsg("StudyMngr object not there");
            Study = (CWStudy)StudyMngr.CreateNewStudy3("frame", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, 0, out errCode);
            if (Study == null) ErrorMsg("Study not created");

            //Get and set beam info
            BeamMgr = (CWBeamManager)Study.BeamManager;
            nbrBeamBodies = BeamMgr.BeamCount;
            Debug.Print("Beams...");
            Debug.Print(" Number of beams: " + nbrBeamBodies);
            BeamBody = null;
            for (j = 0; j <= (nbrBeamBodies - 1); j++)
            {
                BeamBody = (CWBeamBody)BeamMgr.GetBeamBodyAt(j, out errCode);
                if (errCode != 0) ErrorMsg("No beam body");
                Debug.Print(" Name of beam body: " + BeamBody.BeamBodyName);
                beamBodyType = BeamBody.BeamType;
                if (beamBodyType == 0)
                {
                    Debug.Print(" Type of beam body: beam");
                }
                else
                {
                    Debug.Print(" Type of beam body: truss");
                }
                 Debug.Print("      Beam cross-section properties:");

                 Debug.Print("         Maximum distance from the shear center to the furthest point: " + BeamBody.BeamDistForMaxShearStress);

                 Debug.Print("         Beam shear:");

                 Debug.Print("           Direction 1: " + BeamBody.BeamShearY);

                 Debug.Print("           Direction 2: " + BeamBody.BeamShearZ);

                 Debug.Print("         Beam torsional stiffness constant: " + BeamBody.BeamTorsionalConstant);

                 Debug.Print("           Units of length as defined in swsLinearUnit_e: " + BeamBody.BeamTorsionalConstantUnit);
                boolCode = BeamBody.SetLibraryMaterial2("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Plain Carbon Steel");
                if (boolCode == false) ErrorMsg("No material applied");
                BeamBody = null;
            }

            //Calculate joints
            Joints = (CWJoints)BeamMgr.GetJointGroup(out errCode);
            Debug.Print(" ");
            Debug.Print("Joints...");
            if (errCode != 0) ErrorMsg("No joint group");
            Joints.JointsBeginEdit();
            Joints.IncludeAllSelectedBeam = true;
            Joints.IncludeDisplayNeutralAxis = true;
            Joints.CalculateJoints();
            Joints.JointsEndEdit();
            Debug.Print(" Pinball radius: " + Joints.PinBallRadius * 0.001);
```

```vb
            keepJointUpdates = Joints.IncludeKeepModifiedJointOnUpdate;
            if (keepJointUpdates == true)
            {
               Debug.Print(" Keep joint updates: yes");
            }
               else
            Debug.Print(" Keep joint udpates: no");
            Debug.Print(" Overwrite pinball value: " + Joints.IncludeTreatAsJointForClearanceLessThan);
```

```vb
            switch (Joints.PinBallRadiusUnit)
            {
                case 0:
                    Debug.Print(" Pinball radius unit: mm");
                    break;
                case 1:
                    Debug.Print(" Pinball radius unit: cm");
                    break;
                case 2:
                    Debug.Print(" Pinball radius unit: m");
                    break;
                case 3:
                    Debug.Print(" Pinball radius unit: in");
                    break;
                case 4:
                    Debug.Print(" Pinball radius unit: ft");
                    break;
                case 5:
                    Debug.Print(" Pinball radius unit: ft-in");
                    break;
                case 6:
                    Debug.Print(" Pinball radius unit: am");
                    break;
                case 7:
                    Debug.Print(" Pinball radius unit: nm");
                    break;
                case 8:
                    Debug.Print(" Pinball radius unit: micron");
                    break;
                case 9:
                    Debug.Print(" Pinball radius unit: mil");
                    break;
                case 10:
                    Debug.Print(" Pinball radius unit: MicroIn");
                    break;
            }

            //Mesh the part
            Mesh = Study.Mesh;
            if (Mesh == null) ErrorMsg("No mesh object");
            Mesh.Quality = (int)swsMeshQuality_e.swsMeshQualityHigh;
            Mesh.GetDefaultElementSizeAndTolerance((int)swsLinearUnit_e.swsLinearUnitMillimeters, out ElementSize, out Tolerance);
            errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, ElementSize, Tolerance);
            if (errCode != 0) ErrorMsg("Mesh failed");
            Debug.Print(" ");
            Debug.Print("Mesh...");
            Debug.Print(" Time to create mesh (hh:mm:ss): " + Mesh.TimeToCompleteMesh);
            switch (Mesh.MeshType)
            {
                case 0:
                    Debug.Print(" Mesh type: solid");
                    break;
                case 1:
                    Debug.Print(" Mesh type: midsurface");
                    break;
                case 2:
                    Debug.Print(" Mesh type: surface");
                    break;
                case 3:
                    Debug.Print(" Mesh type: mixed");
                    break;
                case 4:
                    Debug.Print(" Mesh type: beam");
                    break;
            }
            Debug.Print(" Number of mesh controls: " + Mesh.MeshControlCount);
            switch (Mesh.MeshState)
            {
                case 0:
                    Debug.Print(" Mesh state: no mesh");
                    break;
                case 1:
                    Debug.Print(" Mesh state: exists and is current");
                    break;
                case 2:
                    Debug.Print(" Mesh state: exists and is not current");
                    break;
                case 3:
                    Debug.Print(" Mesh state: failed");
                    break;
                case 4:
                    Debug.Print(" Mesh state: interrupted");
                    break;
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
