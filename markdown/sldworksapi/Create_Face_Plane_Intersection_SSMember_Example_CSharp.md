---
title: "Create Face Plane Intersection Structure System Member (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Face_Plane_Intersection_SSMember_Example_CSharp.htm"
---

# Create Face Plane Intersection Structure System Member (C#)

This example shows how to create a structure system member along the intersection of a face and a plane.

```vb
 // ==========================================================================================
 // Preconditions:
  // 1. Ensure the specified part template exists.
 // 2. Open an Immediate window.
 // 3. Press F5.
 //
 // Postconditions:
 // 1. Creates Boss-Extrude1 and Plane1 in a new part.
 // 2. Selects a parameter face on the extrusion.
 // 3. Selects Plane1.
 // 4. Creates a face plane intersection member along the intersection of the selected face and plane.
 // 5. Creates a Structure System1.
 // 6. Inspect the member on Plane1 in the graphics area.
 // 7. Press F5 to edit the structure system.
 // 8. Gets all of the structure system members in all of the profile group folders.
 // 9. Changes the member extension lengths in directions 1 and 2.
 // 10. Selects the Right Plane to intersect the parameter face.
 // 11. Modifies the structure system.
 // 12. Inspect the member move to the Right Plane in the graphics area.
 // ========================================================================

 using System.Diagnostics;
 using System.Runtime.InteropServices;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace PrimaryMemberFacePlaneIntersection_CSharp
 {
     public partial class SolidWorksMacro
     {
         private ModelDoc2 modDoc;
         private FeatureManager swFeatMgr;
         private SelectionMgr swSelMgr;
         private ModelDocExtension modDocExt;
         private StructureSystemMemberFeatureData structMemDef;
         private StructureSystemMemberProfile profDef;
         private PrimaryStructuralMemberFeatureData PrimDef;
         private PrimaryMemberFacePlaneIntersectionFeatureData facePlaneIntrSecDef;
         private object[] faces = new object[1];
         private bool stat;
         private object[] IntSecPlane = new object[1];
         private StructureSystemMemberFeatureData[] memData = new StructureSystemMemberFeatureData[1];
         private object[] memDataArray;
         private Feature structSys;
         private StructureSystemFolder structSysModDef;
         private object[] outProfiles;
         private StructureSystemMemberFeatureData MemberData;
         private object[] memberArray;
         private Feature profileGrpFeat;
         private ProfileGroupFolder profileGrp;
         private StructureSystemMemberFeatureData memTochange;
         private PrimaryMemberFacePlaneIntersectionFeatureData faceIntrMemberToChange;
         private object[] newIntSecPlane = new object[1];
         private Feature feat;
         private int I;
         private int J;

         public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)
         {
             int ArraySize;
             ArraySize = Objects.GetUpperBound(0);
             var d = new DispatchWrapper[ArraySize + 1];
             int ArrayIndex;
             var loopTo = ArraySize;
             for (ArrayIndex = 0; ArrayIndex <= loopTo; ArrayIndex++)
                 d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);
             return d;
         }

         public void Main()
         {
             double swSheetWidth;
             swSheetWidth = 0d;
             double swSheetHeight;
             swSheetHeight = 0d;
             modDoc = (ModelDoc2)swApp.NewDocument(@"C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Part.PRTDOT", 0, swSheetWidth, swSheetHeight);
             PartDoc swPart;
             swPart = (PartDoc)modDoc;
             modDoc = (ModelDoc2)swApp.ActiveDoc;
             modDocExt = modDoc.Extension;
             swSelMgr = (SelectionMgr)modDoc.SelectionManager;
             stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
             modDoc.SketchManager.InsertSketch(true);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
             stat = modDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
             object[] vSkLines;
             vSkLines = (object[])modDoc.SketchManager.CreateCornerRectangle(-0.0168788132580097d, 0.0116544186781496d, 0, 0.0139317188796271d, -0.00736773594595662d, 0);
             modDoc.ShowNamedView2("*Trimetric", 8);
             modDoc.ViewZoomtofit2();
             Feature myFeature;
             myFeature = modDoc.FeatureManager.FeatureExtrusion2(false, false, false, 0, 0, 0.2d, 0.2d, false, false, false, false, 0.0174532925199433d, 0.0174532925199433d, false, false, false, false, true, true, true, 0, 0, false);
             swSelMgr.EnableContourSelection = false;
             stat = modDocExt.SelectByRay(0.199999999999932d, 0.00280649656951937d, 0.000880259028576802d, -0.400036026779314d, -0.515038074910018d, -0.758094294050287d, 0.00111139990390966d, 2, false, 0, 0);
             RefPlane myRefPlane;
             myRefPlane = (RefPlane)modDoc.FeatureManager.InsertRefPlane(4, 0, 0, 0, 0, 0);
             modDoc.ClearSelection2(true);

             // Configure a structure system face plane intersection member
             structMemDef = (StructureSystemMemberFeatureData)modDocExt.CreateStructureSystemMemberData(3);
             Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " + structMemDef.StructureSystemMemberType);
             structMemDef.StartEndExtendD1 = 0.4d;
             Debug.Print("Extend length in direction 1: " + structMemDef.StartEndExtendD1);
             structMemDef.StartEndExtendD2 = 0.15d;
             Debug.Print("Extend length in direction 2: " + structMemDef.StartEndExtendD2);
             profDef = (StructureSystemMemberProfile)structMemDef.MemberProfile;
             profDef.ProfileStandard = "ansi inch";
             profDef.ProfileType = "c channel";
             profDef.ProfileSize = "3 x 5";
             PrimDef = (PrimaryStructuralMemberFeatureData)structMemDef;
             Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " + PrimDef.PrimaryMemberType);
             facePlaneIntrSecDef = (PrimaryMemberFacePlaneIntersectionFeatureData)PrimDef;
             facePlaneIntrSecDef.MergeTangentMembers = false;

             // Select parameter face and intersecting plane
             stat = modDocExt.SelectByRay(-0.00017443058891331d, 0.0116544186780629d, -0.000426704146832435d, -0.400036026779314d, -0.515038074910018d, -0.758094294050287d, 0.000189520697225961d, 2, false, 0, 0);
             faces[0] = swSelMgr.GetSelectedObject6(1, -1);
             stat = modDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, 0);
             IntSecPlane[0] = swSelMgr.GetSelectedObject6(1, -1);
             DispatchWrapper[] dArray;
             DispatchWrapper[] eArray;
             DispatchWrapper[] fArray;
             dArray = ObjectArrayToDispatchWrapperArray(faces);
             stat = facePlaneIntrSecDef.SetParameterFaces(dArray);
             Debug.Print("Member's parameter face set successfully: " + stat);
             eArray = ObjectArrayToDispatchWrapperArray(IntSecPlane);
             stat = facePlaneIntrSecDef.SetIntersectingPlanesAndFaces(eArray);
             Debug.Print("Member's intersecting plane set successfully: " + stat);
             memData[0] = structMemDef;
             fArray = ObjectArrayToDispatchWrapperArray(memData);

             // Create Structure System1 in the FeatureManager design tree
             structSys = modDocExt.CreateStructureSystem(fArray, null);
             modDoc.ViewZoomtofit2();
             Debugger.Break();
             Debug.Print("");
             Debug.Print("Edit Structure System1...");
             structSysModDef = (StructureSystemFolder)structSys.GetSpecificFeature2();
             Debug.Print("Number of structure system profile groups: " + structSysModDef.GetProfileGroupFoldersCount());
             outProfiles = (object[])structSysModDef.GetProfileGroupFolders();
             if (outProfiles.Length > 0)
             {
                 var loopTo = outProfiles.GetUpperBound(0);
                 for (I = 0; I <= loopTo; I++)
                 {
                     profileGrpFeat = (Feature)outProfiles[(int)I];
                     profileGrp = (ProfileGroupFolder)profileGrpFeat.GetSpecificFeature2();
                     if (profileGrp is object)
                     {
                         Debug.Print("Number of members inside group: " + profileGrp.GetStructureSystemMemberCount());
                         memberArray = (object[])profileGrp.GetStructureSystemMembers();
                         if (memberArray.Length > 0)
                         {
                             var loopTo1 = memberArray.GetUpperBound(0);
                             for (J = 0; J <= loopTo1; J++)
                             {
                                 MemberData = (StructureSystemMemberFeatureData)memberArray[(int)J];
                                 break;
                             }
                         }
                     }
                 }
             }

             memTochange = MemberData;
             feat = memTochange.GetFeature();
             Debug.Print("Change member extensions in directions 1 and 2...");
             memTochange.StartEndExtendD1 = 0.1d;
             memTochange.StartEndExtendD2 = 0.2d;
             faceIntrMemberToChange = (PrimaryMemberFacePlaneIntersectionFeatureData)memTochange;
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
             newIntSecPlane[0] = swSelMgr.GetSelectedObject6(1, -1);
             dArray = ObjectArrayToDispatchWrapperArray(newIntSecPlane);
             stat = faceIntrMemberToChange.SetIntersectingPlanesAndFaces(dArray);
             Debug.Print("Intersecting plane successfully changed: " + stat);
             stat = feat.ModifyDefinition(MemberData, modDoc, null);
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
