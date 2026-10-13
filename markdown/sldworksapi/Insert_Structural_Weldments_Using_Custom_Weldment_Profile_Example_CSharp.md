---
title: "Insert Structural Weldments Using Custom Weldment Profile Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_CSharp.htm"
---

# Insert Structural Weldments Using Custom Weldment Profile Example (C#)

This example shows how to insert a structural weldment feature using a custom weldment profile configuration and structural member groups.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified library feature and part document template
//    exist.
// 2. Verify that a valid pathname exists in Parts in Tools > Options >
//    System Options > Default Templates.
// 3. Create C:\Test\Pipes.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified library feature, adds the nxn configuration,
//    saves the library feature as nxn.sldlfp, and closes the new library
//    feature, which is called a custom weldment profile when used to create
//    structural weldment features.
// 2. Creates a new part document that contains a sketch of two
//    rectangles.
// 3. Creates a weldment and two structural member features using the
//    sketch and the nxn configuration of the custom weldment profile created in
//    step 1.
// 4. Rotates Pipes nxn(1).
// 5. Examine the FeatureManager design tree, graphics area, and
//    the Immediate window.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatMgr = default(FeatureManager);
            SelectionMgr swSelMgr = default(SelectionMgr);
            SketchManager swSketchMgr = default(SketchManager);
            FeatureManager swFeatureMgr = default(FeatureManager);
            ConfigurationManager swConfigMgr = default(ConfigurationManager);
            Configuration swConfig = default(Configuration);
            Feature swFeature = default(Feature);
            StructuralMemberGroup swStructuralMemberGroup1 = default(StructuralMemberGroup);
            StructuralMemberGroup swStructuralMemberGroup2 = default(StructuralMemberGroup);
            Feature swWeldFeat = default(Feature);
            StructuralMemberFeatureData swStructuralMemberFeatData = default(StructuralMemberFeatureData);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string libFeature = null;
            string newLibFeature = null;
            string macroFolder = null;
            string template = null;
            object sketchLines = null;
            SketchSegment[] segs1 = new SketchSegment[2];
            object[] groupArray1 = new object[1];
            DispatchWrapper[] groups1 = new DispatchWrapper[1];
            SketchSegment[] segs2 = new SketchSegment[2];
            DispatchWrapper[] groups2 = new DispatchWrapper[1];
            object[] groupArray2 = new object[1];
            StructuralMemberGroup group = default(StructuralMemberGroup);
            object[] groups = new object[2];
            object[] segs = new object[2];
            string weldmentProfile = null;
            string weldmentConfigurationName = null;

            //Open existing library feature, add nxn configuration,
            //and save library feature as nxn.sldlfp
            libFeature = "C:\\Program Files\\SolidWorks Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\pipe\\0.5 sch 40.sldlfp";
            swModel = (ModelDoc2)swApp.OpenDoc6(libFeature, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("0.5 sch 40.SLDPRT", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swConfigMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConfig = (Configuration)swConfigMgr.AddConfiguration("nxn", "", "", (int)swConfigurationOptions2_e.swConfigOption_DontActivate, "", "");
            newLibFeature = "C:\\Test\\Pipes\\nxn.sldlfp";
            status = swModelDocExt.SaveAs(newLibFeature, (int)swSaveAsVersion_e.swSaveAsCurrentVersion, (int)swSaveAsOptions_e.swSaveAsOptions_Silent, null, ref errors, ref warnings);
            swModel = null;
            swApp.CloseDoc(newLibFeature);

            //Open new part document and
            //create weldment and structural members
            macroFolder = swApp.GetCurrentMacroPathFolder();
            swApp.SetCurrentWorkingDirectory(macroFolder);
            template = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);
            swModel = (ModelDoc2)swApp.NewDocument(template, 0, 0, 0);
            swFeatMgr = (FeatureManager)swModel.FeatureManager;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModel.ClearSelection2(true);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            sketchLines = (object)swSketchMgr.CreateCornerRectangle(-0.1872393706766, 0.1133237194389, 0, -0.07003610048208, 0.009188409684237, 0);
            swModel.ClearSelection2(true);
            sketchLines = (object)swSketchMgr.CreateCornerRectangle(0.06513561531715, 0.03369083550887, 0, 0.1807053904567, -0.08106219210316, 0);
            swSketchMgr.InsertSketch(true);
            swModel.ViewZoomtofit2();
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureMgr.InsertWeldmentFeature();
            swStructuralMemberGroup1 = (StructuralMemberGroup)swFeatMgr.CreateStructuralMemberGroup();
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.1495427140733, 0.1133237194389, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.1872393706766, 0.08238014634844, 0, true, 0, null, 0);
            segs1[0] = (SketchSegment)swSelMgr.GetSelectedObject6(1, 0);
            segs1[1] = (SketchSegment)swSelMgr.GetSelectedObject6(2, 0);
            swStructuralMemberGroup1.Segments = segs1;
            swStructuralMemberGroup1.Angle = 0.785714285714286; //radians
            swStructuralMemberGroup1.ApplyCornerTreatment = true;
            swStructuralMemberGroup1.CornerTreatmentType = (int)swSolidworksWeldmentEndCondOptions_e.swEndConditionMiter;
            swStructuralMemberGroup1.MirrorProfile = true;
            swStructuralMemberGroup1.MirrorProfileAxis = (int)swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical;

            groupArray1[0] = (object)swStructuralMemberGroup1;
            groups1[0] = new DispatchWrapper(groupArray1[0]);

            weldmentProfile = "C:\\Test\\Pipes\\nxn.SLDLFP";
            weldmentConfigurationName = "nxn";
            swFeature = (Feature)swFeatureMgr.InsertStructuralWeldment5(weldmentProfile, (int)swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, false, (groups1), weldmentConfigurationName);
            swModel.ClearSelection2(true);

            swStructuralMemberGroup2 = (StructuralMemberGroup)swFeatMgr.CreateStructuralMemberGroup();
            status = swModelDocExt.SelectByID2("Line5@Sketch1", "EXTSKETCHSEGMENT", 0.1185825251083, 0.03369083550887, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line6@Sketch1", "EXTSKETCHSEGMENT", 0.06513561531715, -0.02774616865332, 0, true, 0, null, 0);
            segs2[0] = (SketchSegment)swSelMgr.GetSelectedObject6(1, 0);
            segs2[1] = (SketchSegment)swSelMgr.GetSelectedObject6(2, 0);

            swStructuralMemberGroup2.Segments = segs2;
            swStructuralMemberGroup2.AlignAxis = (int)swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical;

            groupArray2[0] = (object)swStructuralMemberGroup2;
            groups2[0] = new DispatchWrapper(groupArray2[0]);

            swFeature = (Feature)swFeatureMgr.InsertStructuralWeldment5(weldmentProfile, (int)swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, false, (groups2), weldmentConfigurationName);
            swModel.ClearSelection2(true);

            //Get feature data for each structural member group
            status = swModelDocExt.SelectByID2("Pipes nxn(1)", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swWeldFeat = (Feature)swSelMgr.GetSelectedObject6(1, 0);
            swStructuralMemberFeatData = (StructuralMemberFeatureData)swWeldFeat.GetDefinition();
            swStructuralMemberFeatData.AccessSelections(swModel, null);
            Debug.Print("");
            Debug.Print("Groups count: " + swStructuralMemberFeatData.GetGroupsCount());
            Debug.Print("  Feature name: " + swWeldFeat.Name);
            Debug.Print("    Custom weldment profile configuration name: " + swStructuralMemberFeatData.ConfigurationName);
            Debug.Print("    Transfer material? " + swStructuralMemberFeatData.TransferMaterial);
            Debug.Print("    Library material profile: " + swStructuralMemberFeatData.LibraryProfileMaterial);

            groups = (object[])swStructuralMemberFeatData.Groups;
            long i = 0;
            long j = 0;
            Debug.Print("    Group:");
            for (i = 0; i < groups.Length; i++)
            {
                group = (StructuralMemberGroup)groups[i];
                Debug.Print("      Segment count: " + group.GetSegmentsCount());
                Debug.Print("      Rotational angle: " + group.Angle);
                Debug.Print("      Apply corner treatment: " + group.ApplyCornerTreatment);
                Debug.Print("      Corner treatment type: " + group.CornerTreatmentType);
                Debug.Print("      Mirror profile: " + group.MirrorProfile);
                Debug.Print("      Mirror profile axis: " + group.MirrorProfileAxis);
                Debug.Print("      Gap within: " + group.GapWithinGroup);
                segs = (object[])group.Segments;
                for (j = 0; j < segs.Length; j++)
                {
                    ((SketchSegment)segs[j]).Select(false);
                }
            }
            swStructuralMemberFeatData.ReleaseSelectionAccess();

            status = swModelDocExt.SelectByID2("Pipes nxn(2)", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swWeldFeat = (Feature)swSelMgr.GetSelectedObject6(1, 0);
            swStructuralMemberFeatData = (StructuralMemberFeatureData)swWeldFeat.GetDefinition();
            swStructuralMemberFeatData.AccessSelections(swModel, null);
            Debug.Print("");
            Debug.Print("Groups count: " + swStructuralMemberFeatData.GetGroupsCount());
            Debug.Print("  Feature name: " + swWeldFeat.Name);
            Debug.Print("    Custom weldment profile configuration name: " + swStructuralMemberFeatData.ConfigurationName);
            Debug.Print("    Transfer material? " + swStructuralMemberFeatData.TransferMaterial);
            Debug.Print("    Library material profile: " + swStructuralMemberFeatData.LibraryProfileMaterial);

            groups = (object[])swStructuralMemberFeatData.Groups;
            Debug.Print("    Group:");
            for (i = 0; i < groups.Length; i++)
            {
                group = (StructuralMemberGroup)groups[i];
                Debug.Print("      Segment count: " + group.GetSegmentsCount());
                Debug.Print("      Rotational angle: " + group.Angle);
                Debug.Print("      Apply corner treatment: " + group.ApplyCornerTreatment);
                Debug.Print("      Corner treatment type: " + group.CornerTreatmentType);
                Debug.Print("      Mirror profile: " + group.MirrorProfile);
                Debug.Print("      Mirror profile axis: " + group.MirrorProfileAxis);
                Debug.Print("      Gap within: " + group.GapWithinGroup);
                segs = (object[])group.Segments;
                for (j = 0; j < segs.Length; j++)
                {
                    ((SketchSegment)segs[j]).Select(false);
                }
            }
            swStructuralMemberFeatData.ReleaseSelectionAccess();
            swModel.ClearSelection2(true);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
