---
title: "Apply Loads to Beams Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Loads_to_Beam_Example_CSharp.htm"
---

# Apply Loads to Beams Example (C#)

This example shows how to apply the total force, or load, along the length of a beam in various types of distributions.

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
 // Postconditions:
 // 1. Loads are applied to the part, and their
 //    distribution types are shown in the Immediate
 //    window.
 // 2. To verify, examine the External Loads folder
 //    in Study 3 in the Simulation tree.
 //
 // NOTE: Because this part document is used elsewhere do not save changes.
 //-------------------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 using System.Diagnostics;
 using System.Windows.Forms;

 namespace LoadsSWSimulationCSharp.csproj
 {

     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt =  default(ModelDocExtension);
             SelectionMgr swSelMgr = default(SelectionMgr);
             CosmosWorks COSMOSWORKS = null;
             CwAddincallback COSMOSObject =  default(CwAddincallback);
             CWModelDoc swsActDoc = default(CWModelDoc);
             CWStudyManager swsStudyMngr =  default(CWStudyManager);
             CWStudy swsStudy = default(CWStudy);
             CWLoadsAndRestraintsManager swsLBCMgr =  default(CWLoadsAndRestraintsManager);
             CWForce swsCWForce = default(CWForce);
             object selBeam = null;
             object selFace = null;
             double[] data = new double[6];
             int rowNum = 0;
             double[] distValue = new double[3];
             double[] forceValue = new double[3];
             int errors = 0;
             int warnings = 0;
             int errCode = 0;
             string forceType = null;

             const string fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\Loop.sldprt";

             // Open document
             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             // Get the SOLIDWORKS Simulation object
             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "No CwAddincallback object");
             COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No COSMOSWORKS object");

             // Open and get active document
             swsActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
             if (swsActDoc == null)
                 ErrorMsg(swApp, "No active document",  true);

             // Create new static study
             swsStudyMngr = (CWStudyManager)swsActDoc.StudyManager;
             if (swsStudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             swsStudy = (CWStudy)swsStudyMngr.GetStudy(2);
             if (swsStudy == null)
                 ErrorMsg(swApp, "No CWStudy object");

             swsLBCMgr = (CWLoadsAndRestraintsManager)swsStudy.LoadsAndRestraintsManager;

             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             // Select the beam and the face to which apply the force
             swModel.Extension.SelectByID2("Structural Member1[3]",  "SOLIDBODY", 0.2669983091512, -0.4441139265177, -0.05999999999995,  true, 0,  null, 0);
             selBeam = (object)swSelMgr.GetSelectedObject6(1, -1);

             swModel.Extension.SelectByID2("", "FACE", -0.4332349164914, -0.1431037474702, -0.05999999999989,  true, 0,  null, 0);
             selFace = (object)swSelMgr.GetSelectedObject6(2, -1);

             object[] beamArray = { selBeam };

             // Create the force
             data[0] = 100.0;
             data[1] = 100.0;
             data[2] = 100.0;
             data[3] = 100.0;
             data[4] = 100.0;
             data[5] = 100.0;

             object[] forceArray = { data[0], data[1], data[2], data[3], data[4], data[5] };

             rowNum = 3;

             distValue[0] = 10.0;
             distValue[1] = 50.0;
             distValue[2] = 100.0;

             forceValue[0] = 100.0;
             forceValue[1] = 0.0;
             forceValue[2] = 50.0;

             // Add force: Total Load - Triangular
             swsCWForce = (CWForce)swsLBCMgr.AddForce3((int)swsForceType_e.swsForceTypeForceOrMoment, (int)swsSelectionType_e.swsSelectionBeams, 2, (int)swsTableDrivenInterpolationType_e.swsLinear, (int)swsTableDrivenDistOption_e.swsPercentage, rowNum, distValue, forceValue, true, true,
             (int)swsBeamNonUniformLoadDef_e.swsTotalLoad, (int)swsBeamNonUniformLoadType_e.swsTriangularLoad, 4, 100, (forceArray), false, false, (beamArray), selFace, true,
             out errCode);
             forceType = "Total Load - Triangular";
             LoadError(swApp, forceType, errCode);

             // Add force: Total Load - Elliptical
             swsCWForce = (CWForce)swsLBCMgr.AddForce3((int)swsForceType_e.swsForceTypeForceOrMoment, (int)swsSelectionType_e.swsSelectionBeams, 2, (int)swsTableDrivenInterpolationType_e.swsLinear, (int)swsTableDrivenDistOption_e.swsPercentage, rowNum, distValue, forceValue, true, true,
             (int)swsBeamNonUniformLoadDef_e.swsTotalLoad, (int)swsBeamNonUniformLoadType_e.swsEllipticalLoad, 4, 100, (forceArray), false, false, (beamArray), selFace, true,
             out errCode);
             forceType = "Total Load - Elliptical";
             LoadError(swApp, forceType, errCode);

             // Add force: Total Load - Parabolic
             swsCWForce = (CWForce)swsLBCMgr.AddForce3((int)swsForceType_e.swsForceTypeForceOrMoment, (int)swsSelectionType_e.swsSelectionBeams, 2, (int)swsTableDrivenInterpolationType_e.swsLinear, (int)swsTableDrivenDistOption_e.swsPercentage, rowNum, distValue, forceValue, true, true,
             (int)swsBeamNonUniformLoadDef_e.swsTotalLoad, (int)swsBeamNonUniformLoadType_e.swsParabolicLoad, 4, 100, (forceArray), false, false, (beamArray), selFace, true,
             out errCode);
             forceType = "Total Load - Parabolic";
             LoadError(swApp, forceType, errCode);

             // Add force: Centered Load - Triangular
             swsCWForce = (CWForce)swsLBCMgr.AddForce3((int)swsForceType_e.swsForceTypeForceOrMoment, (int)swsSelectionType_e.swsSelectionBeams, 2, (int)swsTableDrivenInterpolationType_e.swsLinear, (int)swsTableDrivenDistOption_e.swsPercentage, rowNum, distValue, forceValue, true, true,
             (int)swsBeamNonUniformLoadDef_e.swsCentralLoad, (int)swsBeamNonUniformLoadType_e.swsTriangularLoad, 4, 100, (forceArray), false, false, (beamArray), selFace, true,
             out errCode);
             forceType = "Centered Load - Triangular";
             LoadError(swApp, forceType, errCode);

             // Add force: Centered Load - Elliptical
             swsCWForce = (CWForce)swsLBCMgr.AddForce3((int)swsForceType_e.swsForceTypeForceOrMoment, (int)swsSelectionType_e.swsSelectionBeams, 2, (int)swsTableDrivenInterpolationType_e.swsLinear, (int)swsTableDrivenDistOption_e.swsPercentage, rowNum, distValue, forceValue, true, true,
             (int)swsBeamNonUniformLoadDef_e.swsCentralLoad, (int)swsBeamNonUniformLoadType_e.swsEllipticalLoad, 4, 100, (forceArray), false, false, (beamArray), selFace, true,
             out errCode);
             forceType = "Centered Load - Elliptical";
             LoadError(swApp, forceType, errCode);

             // Add force: Centered Load - Parabolic
             swsCWForce = (CWForce)swsLBCMgr.AddForce3((int)swsForceType_e.swsForceTypeForceOrMoment, (int)swsSelectionType_e.swsSelectionBeams, 2, (int)swsTableDrivenInterpolationType_e.swsLinear, (int)swsTableDrivenDistOption_e.swsPercentage, rowNum, distValue, forceValue, true, true,
             (int)swsBeamNonUniformLoadDef_e.swsCentralLoad, (int)swsBeamNonUniformLoadType_e.swsParabolicLoad, 4, 100, (forceArray), false, false, (beamArray), selFace, true,
             out errCode);
             forceType = "Centered Load - Parabolic";
             LoadError(swApp, forceType, errCode);

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
                     ErrorMsg(swApp,  "Invalid selection");
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

         public void ErrorMsg(object swApp, string Message)
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
