---
title: "Create Reference Plane Structure System Member Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ref_Plane_SSMember_Example_CSharp.htm"
---

# Create Reference Plane Structure System Member Example (C#)

This example shows how to create a structure system member along the intersection of two or more planes.

```vb
 // ==========================================================================================
 // Preconditions:
 // 1. Ensure the specified part template exists.
 // 2. Open an Immediate window.
 // 3. Press F5.
 //
 // Postconditions:
 // 1. Creates five reference planes:
 //    - Plane1 parallel to Right Plane
 //    - Plane2 and Plane3 parallel to and flanking Top Plane
 //    - Plane4 and Plane5 parallel to and flanking Front Plane
 // 2. Configures the member profile.
 // 3. Selects the start/end reference planes that define the lengths of the members: Plane1 and Right Plane.
 // 4. Selects the axis reference planes that define the direction of the members: Plane2 and Plane3.
 // 5. Selects the location reference planes that define the positions of the members: Plane4 and Plane5.
 // 6. Creates a Structure System1 with nine structure system reference plane members.
 // 7. Inspect the structure system in the graphics area.
 // 8. Press F5 to edit the structure system.
 // 9. Gets Member1.
 // 10. Changes its extensions in directions 1 and 2.
 // 11. Modifies the structure system.
 // 12. Inspect the changes in the graphics area.
 // ========================================================================

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace RefPlane_CSharp
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
         private PrimaryMemberRefPlaneFeatureData memRefPlaneDef;
         private object[] startEndPlanes = new object[2];
         private object[] horzPlanes = new object[3];
         private object[] vertPlanes = new object[3];
         private bool stat;
         private StructureSystemMemberFeatureData[] memData = new StructureSystemMemberFeatureData[1];
         private object[] memDataArray;
         private Feature structSysFeat;
         private Feature feat;
         private StructureSystemFolder structSysModDef;
         private object[] outProfiles;
         private StructureSystemMemberFeatureData MemberData;
         private object[] memberArray;
         private Feature profileGrpFeat;
         private ProfileGroupFolder profileGrp;
         private StructureSystemMemberFeatureData memTochange;
         private int I;
         private int j;

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
             modDoc = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr =(SelectionMgr) modDoc.SelectionManager;
             modDocExt = modDoc.Extension;
             stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
             object myRefPlane;
             myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.381d, 0, 0, 0, 0);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
             myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.1778d, 0, 0, 0, 0);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, 0);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
             myRefPlane = modDoc.FeatureManager.InsertRefPlane(264, 0.1778d, 0, 0, 0, 0);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Plane2", "PLANE", 0, 0, 0, false, 0, null, 0);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
             myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.1778d, 0, 0, 0, 0);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Plane3", "PLANE", 0, 0, 0, false, 0, null, 0);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
             myRefPlane = modDoc.FeatureManager.InsertRefPlane(264, 0.1778d, 0, 0, 0, 0);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Plane4", "PLANE", 0, 0, 0, false, 0, null, 0);
             modDoc.ClearSelection2(true);
             stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
             stat = modDocExt.SelectByID2("Plane1", "PLANE", 0.0729275826275853d, 0.103693179609365d, 0.188906126602433d, true, 0, null, 0);
             stat = modDocExt.SelectByID2("Plane2", "PLANE", -0.035035924945646d, 0.0882769827595098d, 0.154770056203461d, true, 0, null, 0);
             stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
             stat = modDocExt.SelectByID2("Plane3", "PLANE", -0.0359335022268397d, 0.0486897858681345d, 0.154489603864079d, true, 0, null, 0);
             stat = modDocExt.SelectByID2("Plane4", "PLANE", -0.0353613843872154d, 0.122848840931965d, 0.120060929442332d, true, 0, null, 0);
             stat = modDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
             stat = modDocExt.SelectByID2("Plane5", "PLANE", -0.0313617150023902d, 0.123208535607716d, 0.0798165581882131d, true, 0, null, 0);

             // Create structure system reference plane member
             structMemDef = (StructureSystemMemberFeatureData)modDocExt.CreateStructureSystemMemberData(1);
             Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " + structMemDef.StructureSystemMemberType);
             Debug.Print("Extend length in direction 1 (m): " + structMemDef.StartEndExtendD1);
             Debug.Print("Extend length in direction 2 (m): " + structMemDef.StartEndExtendD2);
             profDef = (StructureSystemMemberProfile)structMemDef.MemberProfile;
             profDef.ProfileStandard = "ansi inch";
             profDef.ProfileType = "c channel";
             profDef.ProfileSize = "3 x 5";
             PrimDef = (PrimaryStructuralMemberFeatureData)structMemDef;
             Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " + PrimDef.PrimaryMemberType);
             memRefPlaneDef = (PrimaryMemberRefPlaneFeatureData)PrimDef;

             // Define the member lengths
             startEndPlanes[0] = swSelMgr.GetSelectedObject6(1, 0);
             startEndPlanes[1] = swSelMgr.GetSelectedObject6(2, 0);
             DispatchWrapper[] dArray;
             dArray = ObjectArrayToDispatchWrapperArray(startEndPlanes);
             stat = memRefPlaneDef.SetStartAndEndReferences(dArray);
             Debug.Print("Reference planes set successfully: " + stat);
             horzPlanes[0] = swSelMgr.GetSelectedObject6(3, 0);
             horzPlanes[1] = swSelMgr.GetSelectedObject6(4, 0);
             horzPlanes[2] = swSelMgr.GetSelectedObject6(5, 0);
             DispatchWrapper[] eArray;
             eArray = ObjectArrayToDispatchWrapperArray(horzPlanes);
             stat = memRefPlaneDef.SetReferenceAxes(eArray);
             Debug.Print("Reference axis planes set successfully: " + stat);
             vertPlanes[0] = swSelMgr.GetSelectedObject6(6, 0);
             vertPlanes[1] = swSelMgr.GetSelectedObject6(7, 0);
             vertPlanes[2] = swSelMgr.GetSelectedObject6(8, 0);
             DispatchWrapper[] fArray;
             fArray = ObjectArrayToDispatchWrapperArray(vertPlanes);
             stat = memRefPlaneDef.SetReferenceLocations(fArray);
             Debug.Print("Reference location planes set successfully: " + stat);
             memData[0] = structMemDef;
             memDataArray = memData;
             structSysFeat = modDocExt.CreateStructureSystem(memDataArray, null);
             modDoc.ShowNamedView2("*Trimetric", 8);
             modDoc.ViewZoomtofit2();
             Debugger.Break();
             structSysModDef = (StructureSystemFolder)structSysFeat.GetSpecificFeature2();
             Debug.Print("Number of profile group folders: " + structSysModDef.GetProfileGroupFoldersCount());
             outProfiles = (object[])structSysModDef.GetProfileGroupFolders();
             if (outProfiles.Length > 0)
             {
                 var loopTo = outProfiles.GetUpperBound(0);
                 for (I = 0; I <= loopTo; I++)
                 {
                     profileGrpFeat = (Feature)outProfiles[I];
                     profileGrp = (ProfileGroupFolder)profileGrpFeat.GetSpecificFeature2();
                     if (profileGrp is object)
                     {
                         Debug.Print("Number of members in profile group folder: " + profileGrp.GetStructureSystemMemberCount());
                         memberArray = (object[])profileGrp.GetStructureSystemMembers();
                         if (memberArray.Length > 0)
                         {
                             var loopTo1 = memberArray.GetUpperBound(0);
                             for (j = 0; j <= loopTo1; j++)
                             {
                                 MemberData = (StructureSystemMemberFeatureData)memberArray[j]; // Get first member only
                                 break;
                             }
                         }
                     }
                 }
             }

             memTochange = MemberData;
             feat = memTochange.GetFeature();

             // Change the extensions in directions 1 and 2 for Member1
             memTochange.StartEndExtendD1 = 0.5d;
             memTochange.StartEndExtendD2 = 0.2d;
             modDoc.ClearSelection2(true);
             Debug.Print("Member extensions set successfully: " + stat);

             // Save edits
             stat = feat.ModifyDefinition(MemberData, modDoc, null);
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
