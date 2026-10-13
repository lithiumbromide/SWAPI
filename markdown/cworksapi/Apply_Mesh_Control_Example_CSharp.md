---
title: "Apply Mesh Control Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Mesh_Control_Example_CSharp.htm"
---

# Apply Mesh Control Example (C#)

This example shows how to get and set beams and joints, create a mesh, and apply a mesh control.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
  // 3. Ensure that the specified part and material library exist.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates a static study named frame.
 // 2. Gets beam information.
  // 3. Applies Plain Carbon Steel material to all beams.
  // 4. Calculates joints for all beams, gets a neutral axis for each beam,
  //    and gets the pinball tolerance value and unit.
 // 5. Sets the mesher type to alternate curvature based.
 // 6. Applies a mesh control and gets its values.
  // 7. Creates a mixed mesh and gets its type and state.
  //    NOTE: This can take several seconds to complete.
 // 8. Inspect the Immediate window.
 //
 // NOTES:
  // *  Beam elements are created by default for parts with structural members.
  // *  Because the part is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 using System.Runtime.InteropServices;
 namespace ApplyMeshControl_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             SelectionMgr swSelMgr = default(SelectionMgr);
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback COSMOSObject = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWBeamManager BeamMgr = default(CWBeamManager);
             CWBeamBody BeamBody = default(CWBeamBody);
             CWJoints Joints = default(CWJoints);
             CWMesh Mesh = default(CWMesh);
             CWMeshControl MeshControl = default(CWMeshControl);
             int nbrBeamBodies = 0;
             int beamBodyType = 0;
             double ElementSize = 0;
             double Tolerance = 0;
             int errors = 0;
             int warnings = 0;
             int errCode = 0;
             int j = 0;
             int bApp = 0;
             bool keepJointUpdates = false;
             bool status = false;
             object selEntity = null;
             object[] selEntities = new object[8];

             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "COSMOSObject object not found");
             COSMOSWORKS = COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "COSMOSWORKS object not found");

             swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\weldments\\weldment_box2.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             Study = StudyMngr.CreateNewStudy3("frame", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, 0, out errCode);
             if (Study == null)
                 ErrorMsg(swApp, "Study not created");

             BeamMgr = Study.BeamManager;
             nbrBeamBodies = BeamMgr.BeamCount;
             Debug.Print("Beams...");
             Debug.Print("  Number of beams: " + nbrBeamBodies);
             BeamBody = null;
             for (j = 0; j <= (nbrBeamBodies - 1); j++)
             {
                 BeamBody = BeamMgr.GetBeamBodyAt(j, out errCode);
                 if (errCode != 0)
                     ErrorMsg(swApp, "No beam body");
                 Debug.Print("    Name of beam body: " + BeamBody.BeamBodyName);
                 beamBodyType = BeamBody.BeamType;
                 if (beamBodyType == 0)
                 {
                     Debug.Print("      Type of beam body: beam");
                 }
                 else
                 {
                     Debug.Print("      Type of beam body: truss");
                 }
                 bApp = BeamBody.SetLibraryMaterial("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Plain Carbon Steel");
                 if (bApp == 0)
                     ErrorMsg(swApp, "No material applied");
                 BeamBody = null;
             }

             // Calculate joints
             Joints = BeamMgr.GetJointGroup(out errCode);
             Debug.Print(" ");
             Debug.Print("Joints...");
             if (errCode != 0)
                 ErrorMsg(swApp, "No joint group");
             Joints.JointsBeginEdit();
             Joints.IncludeAllSelectedBeam = true;
             Joints.IncludeDisplayNeutralAxis = true;
             Joints.CalculateJoints();
             Joints.JointsEndEdit();
             keepJointUpdates = Joints.IncludeKeepModifiedJointOnUpdate;
             if ((keepJointUpdates == true))
             {
                 Debug.Print("  Keep joint updates? yes");
             }
             else
             {
                 Debug.Print("  Keep joint updates? no");
             }
             Debug.Print("  Overwrite the pinball value: " + Joints.IncludeTreatAsJointForClearanceLessThan);
             Debug.Print("  Pinball radius: " + Joints.PinBallRadius * 0.001);
             switch (Joints.PinBallRadiusUnit)
             {
                 case 0:
                     Debug.Print("  Pinball radius unit: mm");
                     break;
                 case 1:
                     Debug.Print("  Pinball radius unit: cm");
                     break;
                 case 2:
                     Debug.Print("  Pinball radius unit: m");
                     break;
                 case 3:
                     Debug.Print("  Pinball radius unit: in");
                     break;
                 case 4:
                     Debug.Print("  Pinball radius unit: ft");
                     break;
                 case 5:
                     Debug.Print("  Pinball radius unit: ft-in");
                     break;
                 case 6:
                     Debug.Print("  Pinball radius unit: am");
                     break;
                 case 7:
                     Debug.Print("  Pinball radius unit: nm");
                     break;
                 case 8:
                     Debug.Print("  Pinball radius unit: micron");
                     break;
                 case 9:
                     Debug.Print("  Pinball radius unit: mil");
                     break;
                 case 10:
                     Debug.Print("  Pinball radius unit: micronIn");
                     break;
             }

             Mesh = Study.Mesh;
             if (Mesh == null)
                 ErrorMsg(swApp, "No mesh object");
             Mesh.Quality = (int)swsMeshQuality_e.swsMeshQualityHigh;
             Mesh.MesherType = (int)swsMesherType_e.swsMesherTypeAlternateCB;
             Mesh.GetDefaultElementSizeAndTolerance((int)swsLinearUnit_e.swsLinearUnitMillimeters, out ElementSize, out Tolerance);

             // Select structural members for mesh control
             Debug.Print("");
             Debug.Print("Mesh control...");

             status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[4]", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             selEntity = swSelMgr.GetSelectedObject6(1, -1);
             selEntities[0] = selEntity;
             selEntity = null;

             status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[3]", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             selEntity = swSelMgr.GetSelectedObject6(1, -1);
             selEntities[1] = selEntity;
             selEntity = null;

             status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[2]", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             selEntity = swSelMgr.GetSelectedObject6(1, -1);
             selEntities[2] = selEntity;
             selEntity = null;

             status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[1]", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             selEntity = swSelMgr.GetSelectedObject6(1, -1);
             selEntities[3] = selEntity;
             selEntity = null;

             status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[8]", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             selEntity = swSelMgr.GetSelectedObject6(1, -1);
             selEntities[4] = selEntity;
             selEntity = null;

             status = swModelDocExt.SelectByID2("Square tube 30 X 30 X 2.6(1)[6]", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             selEntity = swSelMgr.GetSelectedObject6(1, -1);
             selEntities[5] = selEntity;
             selEntity = null;

             status = swModelDocExt.SelectByID2("Sb beam 80 X 6(1)[2]", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             selEntity = swSelMgr.GetSelectedObject6(1, -1);
             selEntities[6] = selEntity;
             selEntity = null;

             status = swModelDocExt.SelectByID2("Sb beam 80 X 6(1)[1]", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             selEntity = swSelMgr.GetSelectedObject6(1, -1);
             selEntities[7] = selEntity;
             selEntity = null;

             MeshControl = Mesh.ApplyMeshControl(selEntities, out errCode);
             MeshControl.MeshControlBeginEdit();
             MeshControl.BeamSelected2 = 0;
             MeshControl.MinimumElementSize_BlendedCurved = 4;
             MeshControl.MinNumOfElementsPerCircle_BlendedCurved = 8;
             MeshControl.MeshControlEndEdit();
             Debug.Print("  Name of mesh control: " + MeshControl.Name);
             Debug.Print("  Beam selected? (true = yes; false = no) " + MeshControl.BeamSelected2);
             Debug.Print("  Element size for mesh control (m): " + MeshControl.ElementSize);
             Debug.Print("  Number of entities in mesh control: " + MeshControl.EntityCount);
             Debug.Print("  Number of elements for beams: " + MeshControl.NumofElementsforBeams);
             Debug.Print("  Ratio of the average element size (layer i)/(layer i-1): " + MeshControl.Ratio);
             Debug.Print("  State of mesh control (0 = suppressed; 1 = not suppressed): " + MeshControl.State);
             Debug.Print("  Minimum element size for boundaries with highest curvature: " + MeshControl.MinimumElementSizeForBlendedCurveMesher);
             Debug.Print("  Minimum number of elements in a circle to determine the maximum angle: " + MeshControl.MinNumOfElementsPerCircleForBlendedCurveMesher);

             Debug.Print("  Number of mesh controls: " + Mesh.MeshControlCount);

             errCode = Study.CreateMeshForMeshControl(MeshControl.Name);

             // Mesh the part
             Debug.Print(" ");
             Debug.Print("*** Creating a mesh next, which can take several seconds. Please wait. ***");
             errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, ElementSize, Tolerance);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed");

             Debug.Print(" ");
             Debug.Print("Mesh...");
             Debug.Print("  Time to create (hh:mm:ss): " + Mesh.TimeToCompleteMesh);
             Debug.Print("  Type: ");
             switch (Mesh.MeshType)
             {
                 case 0:
                     Debug.Print("    Solid");
                     break;
                 case 1:
                     Debug.Print("    Midsurface");
                     break;
                 case 2:
                     Debug.Print("    Surface");
                     break;
                 case 3:
                     Debug.Print("    Mixed");
                     break;
                 case 4:
                     Debug.Print("    Beam");
                     break;
             }

             Debug.Print("  State: ");
             switch (Mesh.MeshState)
             {
                 case 0:
                     Debug.Print("    No mesh");
                     break;
                 case 1:
                     Debug.Print("    Exists and is current");
                     break;
                 case 2:
                     Debug.Print("    Exists and is not current");
                     break;
                 case 3:
                     Debug.Print("    Failed");
                     break;
                 case 4:
                     Debug.Print("    Interrupted");
                     break;
             }

         }
         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
