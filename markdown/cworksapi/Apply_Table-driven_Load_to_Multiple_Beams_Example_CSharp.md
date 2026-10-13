---
title: "Apply Table-driven Load to Multiple Beams Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Table-driven_Load_to_Multiple_Beams_Example_CSharp.htm"
---

# Apply Table-driven Load to Multiple Beams Example (C#)

This example shows how to apply a table-driven elliptical load to multiple beams on a part.

```vb
//-------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open the Immediate window.
 // 4. Ensure that the specified file to open exists.
 //
 // Postconditions:
 // 1. Applies a table-driven elliptical load to the part
 //    and prints its type and other force-related values
 //    in the Immediate window.
 // 2. To verify, examine the External Loads folder
 //    in Study 3 in the Simulation tree.
 // 3. Examine the Immediate window.
 //
 // NOTE: Because this part document is used elsewhere,
 // do not save any changes when closing it.
 //-------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 using System.Windows.Forms;
 using System.Diagnostics;

 namespace TableDrivenLoadsSWSimulationCSharp.csproj
 {

     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             SelectionMgr swSelMgr = default(SelectionMgr);
             CosmosWorks COSMOSWORKS = null;
             CwAddincallback COSMOSObject = default(CwAddincallback);
             CWModelDoc swsActDoc = default(CWModelDoc);
             CWStudyManager swsStudyMngr = default(CWStudyManager);
             CWStudy swsStudy = default(CWStudy);
             CWLoadsAndRestraintsManager swsLBCMgr = default(CWLoadsAndRestraintsManager);
             CWForce swsCWForce = default(CWForce);
             object selBeam1 = null;
             object selBeam2 = null;
             object selBeam3 = null;
             object selBeam4 = null;
             object selTrimExtend1 = null;
             object selTrimExtend2 = null;
             object selTrimExtend3 = null;
             object selFace = null;
             double[] data = new double[6];
             int rowNum = 0;
             double[] distValue = new double[3];
             double[] forceValue = new double[3];
             int errors = 0;
             int warnings = 0;
             int errCode = 0;
             string forceType = null;

             string fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\Loop.sldprt";

             // Open document
             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Get the SOLIDWORKS Simulation object
             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "No CWAddincallback object");
             COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No COSMOSWORKS object");

             // Get active document
             swsActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
             if (swsActDoc == null)
                 ErrorMsg(swApp, "No active document");

             // Create new static study
             swsStudyMngr = (CWStudyManager)swsActDoc.StudyManager;
             if (swsStudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             swsStudy = (CWStudy)swsStudyMngr.GetStudy(2);
             if (swsStudy == null)
                 ErrorMsg(swApp, "No CWStudy object");

             swsLBCMgr = (CWLoadsAndRestraintsManager)swsStudy.LoadsAndRestraintsManager;

             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             // Select entities
             swModel.Extension.SelectByID2("Structural Member1[3]", "SOLIDBODY", 0.2669983091512, -0.4441139265177, -0.05999999999995, true, 0, null, 0);
             selBeam1 = (object)swSelMgr.GetSelectedObject6(1, -1);

             swModel.Extension.SelectByID2("Structural Member1[1]", "SOLIDBODY", 0.5462661602309, 0.4984264234139, -0.02447052600974, true, 0, null, 0);
             selBeam2 = (object)swSelMgr.GetSelectedObject6(2, -1);

             swModel.Extension.SelectByID2("Structural Member1[4]", "SOLIDBODY", -0.364288009376, 0.3216654991368, -0.0596008827161, true, 0, null, 0);
             selBeam3 = (object)swSelMgr.GetSelectedObject6(3, -1);

             swModel.Extension.SelectByID2("Structural Member1[2]", "SOLIDBODY", 1.410399123355, -0.191782066378, -0.05999999999989, true, 0, null, 0);
             selBeam4 = (object)swSelMgr.GetSelectedObject6(4, -1);

             swModel.Extension.SelectByID2("Trim/Extend3[1]", "SOLIDBODY", 0.3090890041738, -0.1687816014703, -0.01999999999992, true, 0, null, 0);
             selTrimExtend1 = (object)swSelMgr.GetSelectedObject6(5, -1);

             swModel.Extension.SelectByID2("Trim/Extend3[2]", "SOLIDBODY", 0.7058778550122, -0.1651708212717, -0.01943888995868, true, 0, null, 0);
             selTrimExtend2 = (object)swSelMgr.GetSelectedObject6(6, -1);

             swModel.Extension.SelectByID2("Trim/Extend2[2]", "SOLIDBODY", 0.6681230178383, 0.1527188626094, -0.01999999999998, true, 0, null, 0);
             selTrimExtend3 = (object)swSelMgr.GetSelectedObject6(7, -1);

             swModel.Extension.SelectByID2("", "FACE", -0.4332349164914, -0.1431037474702, -0.05999999999989, true, 0, null, 0);
             selFace = (object)swSelMgr.GetSelectedObject6(8, -1);

             object[] beamArray = {
 selBeam1,
 selBeam2,
 selBeam3,
 selBeam4,
 selTrimExtend1,
 selTrimExtend2,
 selTrimExtend3
 };

             // Create the force
             data[0] = 100.0;
             data[1] = 100.0;
             data[2] = 100.0;
             data[3] = 100.0;
             data[4] = 100.0;
             data[5] = 100.0;

             object[] forceArray = {
 data[0],
 data[1],
 data[2],
 data[3],
 data[4],
 data[5]
 };

             rowNum = 3;

             distValue[0] = 10.0;
             distValue[1] = 50.0;
             distValue[2] = 100.0;

             forceValue[0] = 100.0;
             forceValue[1] = 0.0;
             forceValue[2] = 50.0;

             // Table-driven Load: Elliptical
             swsCWForce = (CWForce)swsLBCMgr.AddForce3((int)swsForceType_e.swsForceTypeForceOrMoment, (int)swsSelectionType_e.swsSelectionBeams, 2, (int)swsTableDrivenInterpolationType_e.swsLinear, (int)swsTableDrivenDistOption_e.swsPercentage, rowNum, distValue, forceValue, true, true,
             (int)swsBeamNonUniformLoadDef_e.swsTableDrivenLoad, (int)swsBeamNonUniformLoadType_e.swsEllipticalLoad, 4, 100, (forceArray), false, false, (beamArray), selFace, true,
             out errCode);
             forceType = "Table-drive Load: Multiple Beams";
             LoadError(swApp, forceType, errCode);
             Debug.Print("  Type as defined in swsForceType_e: " + swsCWForce.ForceType);
             Debug.Print("  Phase angle: " + swsCWForce.PhaseAngle);
             Debug.Print("  Phase unit as defined in swsPhaseAngle_e: " + swsCWForce.PhaseAngleUnit);
             Debug.Print("  Unit as defined in swsForceUnit_e: " + swsCWForce.Unit);
             Debug.Print("  Include nonuniform distribution (1 if nonuniform, 0 if uniform)? " + swsCWForce.IncludeNonUniformDistribution);
             Debug.Print("  Normal force or torque value: " + swsCWForce.IncludeNonUniformDistribution);

             swModel.ClearSelection2(true);

         }

         public void LoadError(object swApp, string force, long errorCode)
         {
             switch (errorCode)
             {
                 case 18:
                     ErrorMsg(swApp, "You cannot apply triangular and centered load distribution on multiple beams");
                     break;
                 case 19:
                     ErrorMsg(swApp, "You cannot apply a zero intensity load");
                     break;
                 case 20:
                     ErrorMsg(swApp, "Invalid selection");
                     break;
                 case 21:
                     ErrorMsg(swApp, "The table-driven data is invalid");
                     break;
                 case 22:
                     ErrorMsg(swApp, "In the table-driven distance data, the distance value from the previous row cannot be greater than the distance value in the next row");
                     break;
                 case 0:
                     Debug.Print(force);
                     break;
                 default:
                     ErrorMsg(swApp, "No forces applied");
                     break;
             }
         }

         public void ErrorMsg(SldWorks swApp, string Message)
         {
             MessageBox.Show(Message);
             MessageBox.Show("'*** WARNING - General");
             MessageBox.Show("'*** " + Message);
             MessageBox.Show("");

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
