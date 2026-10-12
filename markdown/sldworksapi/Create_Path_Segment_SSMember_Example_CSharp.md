---
title: "Create Path Segment Structure System Member Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Path_Segment_SSMember_Example_CSharp.htm"
---

# Create Path Segment Structure System Member Example (C#)

This example shows how to create structure system path segment members that are split along a reference plane.

```vb
 // ==========================================================================================
 // Preconditions:
 // 1. Ensure the specified part template exists.
 // 2. Open an Immediate window.
 // 3. Press F5.
 //
 // Postconditions:
 // 1. Creates Sketch1 containing two sketch segments.
 // 2. Creates Plane1.
 // 3. Configures the start/end extensions and the member profile.
 // 4. Selects two sketch segments and Plane1.
 // 5. Configures structure system to split members using Plane1.
 // 6. Creates a Structure System1 with four split members: Member1_1, Member1_2, Member2_1, and Member2_2.
 // 7. Inspect the structure system in the graphics area.
 // 8. Press F5 to edit the structure system.
 // 9. Changes the start/end extensions for Member1_1 and Member1_2.
 // 10. Modifies the structure system.
 // 11. Inspect the changes in the graphics area.
 // ========================================================================

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace PathSegment_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
            private  ModelDoc2 modDoc;
            private  FeatureManager swFeatMgr;
            private  SelectionMgr swSelMgr;
            private  ModelDocExtension modDocExt;
            private   StructureSystemMemberFeatureData structMemDef;
            private   StructureSystemMemberProfile profDef;
            private   PrimaryStructuralMemberFeatureData PrimDef;
            private   PrimaryMemberPathSegmentFeatureData memPathSegDef;
            private  object[] segments =   new   object[2];
            private  bool stat;
            private   StructureSystemMemberFeatureData[] memData =   new   StructureSystemMemberFeatureData[1];
            private  object[] memDataArray;
            private  Feature structSys;
            private  Feature feat;
            private  StructureSystemFolder structSysModDef;
            private  object[] outProfiles;
            private   StructureSystemMemberFeatureData MemberData;
            private  object[] memberArray;
            private  Feature profileGrpFeat;
            private  ProfileGroupFolder profileGrp;
            private   StructureSystemMemberFeatureData memTochange;
            private  int I;
            private  int j;

            public  DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)
           {
               int ArraySize;
              ArraySize = Objects.GetUpperBound(0);
               var d =  new  DispatchWrapper[ArraySize + 1];
               int ArrayIndex;
               var loopTo = ArraySize;
               for (ArrayIndex = 0; ArrayIndex <= loopTo; ArrayIndex++)
                  d[ArrayIndex] =   new   DispatchWrapper(Objects[ArrayIndex]);
               return d;
           }

            public  void Main()
           {
               double swSheetWidth;
              swSheetWidth = 0d;
               double swSheetHeight;
              swSheetHeight = 0d;
              modDoc = (ModelDoc2)swApp.NewDocument(@"C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Part.PRTDOT", 0, swSheetWidth, swSheetHeight);
              modDoc = (ModelDoc2)swApp.ActiveDoc;
              modDocExt = modDoc.Extension;
              swSelMgr = (SelectionMgr)modDoc.SelectionManager;
              modDoc.SketchManager.InsertSketch(true);
              stat = modDocExt.SelectByID2("Front Plane",  "PLANE", -0.0550812963393624d, 0.0228249965575248d, 0.0135586835718293d,  false, 0,  null, 0);
              modDoc.ClearSelection2(true);
               object skSegment;
              skSegment = modDoc.SketchManager.CreateLine(-0.036101d, -0.017052d, 0d, 0.03111d, 0.018383d, 0d);
              skSegment = modDoc.SketchManager.CreateLine(0.055067d, -0.015222d, 0d, -0.01281d, -0.055483d, 0d);
              modDoc.SketchManager.InsertSketch(true);
              modDoc.ClearSelection2(true);
              stat = modDocExt.SelectByID2("Right Plane",   "PLANE", 0, 0, 0,   true, 0,   null, 0);
               RefPlane myRefPlane;
              myRefPlane = (RefPlane)modDoc.FeatureManager.InsertRefPlane(8, 0.02d, 0, 0, 0, 0);
              modDoc.ClearSelection2(true);
              stat = modDocExt.SelectByID2("Line1@Sketch1",   "EXTSKETCHSEGMENT", -0.0123094293114227d, -0.00450860223252535d, 0,  true, 0,   null, 0);
              stat = modDocExt.SelectByID2("Line2@Sketch1",   "EXTSKETCHSEGMENT", 1.11728134432853d, -0.0376344266391984d, 0,  true, 0,  null, 0);
              stat = modDocExt.SelectByID2("Plane1",   "PLANE", 0.0199883401957978d, 0.0202450835544425d, -0.0243017856732353d,   true, 0,   null, 0);
              structMemDef = (StructureSystemMemberFeatureData)modDocExt.CreateStructureSystemMemberData(0);
               Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " + structMemDef.StructureSystemMemberType);
              structMemDef.StartEndExtendD1 = 0.1d;
               Debug.Print("Extend length in direction 1 (m): " + structMemDef.StartEndExtendD1);
              structMemDef.StartEndExtendD2 = 0.2d;
               Debug.Print("Extend length in direction 2 (m): " + structMemDef.StartEndExtendD2);
              profDef = (StructureSystemMemberProfile)structMemDef.MemberProfile;
              profDef.ProfileStandard =   "ansi inch";
              profDef.ProfileType =   "c channel";
              profDef.ProfileSize =   "3 x 5";
              PrimDef = (PrimaryStructuralMemberFeatureData)structMemDef;
               Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " + PrimDef.PrimaryMemberType);
              memPathSegDef = (PrimaryMemberPathSegmentFeatureData)PrimDef;
              memPathSegDef.MergeTangentMembers =   true;
               Debug.Print("Merge tangent members? " + memPathSegDef.MergeTangentMembers);
              segments[0] = swSelMgr.GetSelectedObject6(1, 0);
              segments[1] = swSelMgr.GetSelectedObject6(2, 0);
               DispatchWrapper[] dArray;
              dArray = ObjectArrayToDispatchWrapperArray(segments);
              stat = memPathSegDef.SetPathSegments(dArray);
               Debug.Print("Path segments set successfully: " + stat);
               var planes =  new  object[1];
              planes[0] = swSelMgr.GetSelectedObject6(3, 0);
              structMemDef.IsSplit =   true;
               StructureSystemSplitMember structSplitMember;
              structSplitMember = (StructureSystemSplitMember)structMemDef.GetSplitMember();
              structSplitMember.MemberType = (int)swStructureSplitMemberType_e.swStructureSplitMember_Reference;
               DispatchWrapper[] eArray;
              eArray = ObjectArrayToDispatchWrapperArray(planes);
              stat = structSplitMember.SetSplitReferences(eArray);
              memData[0] = structMemDef;
               DispatchWrapper[] fArray;
              fArray = ObjectArrayToDispatchWrapperArray(memData);
              structSys = modDocExt.CreateStructureSystem(fArray,  null);
              modDoc.ViewZoomtofit();
               Debugger.Break();

               // Edit the structure system
              structSysModDef = (StructureSystemFolder)structSys.GetSpecificFeature2();
               Debug.Print("Number of profile group folders: " + structSysModDef.GetProfileGroupFoldersCount());
              outProfiles = (object[])structSysModDef.GetProfileGroupFolders();
               if (outProfiles.Length > 0)
              {
                   var loopTo = outProfiles.GetUpperBound(0);
                   for (I = 0; I <= loopTo; I++)
                  {
                      profileGrpFeat = (Feature)outProfiles[I];
                      profileGrp = (ProfileGroupFolder)profileGrpFeat.GetSpecificFeature2();
                       if (profileGrp  is   object)
                      {
                            Debug.Print("Number of members inside profile group folder: " + profileGrp.GetStructureSystemMemberCount());
                          memberArray = (object[])profileGrp.GetStructureSystemMembers();
                           if (memberArray.Length > 0)
                          {
                                var loopTo1 = memberArray.GetUpperBound(0);
                                for (j = 0; j <= loopTo1; j++)
                              {
                                  MemberData = (StructureSystemMemberFeatureData)memberArray[j];   // Get Member1 only
                                    break;
                              }
                          }
                      }
                  }
              }

              memTochange = MemberData;

               // Change the start/end extensions for Member1
               Debug.Print("Change member extensions in directions 1 and 2 for one member only");
              feat = memTochange.GetFeature();
              memTochange.StartEndExtendD1 = 0.5d;
              memTochange.StartEndExtendD2 = 0.2d;

               // Save edits
              stat = feat.ModifyDefinition(MemberData, modDoc,  null);
           }

            // The SldWorks swApp variable is pre-assigned for you.
            public  SldWorks swApp;

      }
 }
```
