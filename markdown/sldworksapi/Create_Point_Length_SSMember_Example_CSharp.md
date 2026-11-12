---
title: "Create Point Length Structure System Member Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Point_Length_SSMember_Example_CSharp.htm"
---

# Create Point Length Structure System Member Example (C#)

This example shows how to create a structure system member that originates at a point and extends to a specified end condition.

```vb
 // ==========================================================================================
 // Preconditions:
 // 1. Ensure the specified part template exists.
 // 2. Open an Immediate window.
 // 3. Press F5.
 //
 // Postconditions:
 // 1. Creates Sketch1, Sketch2, and Sketch3 in a new part.
 // 2. Configures the start/end extensions and the member profile.
 // 3. Configures the length end condition for the structure members.
 // 4. Selects three sketch points.
 // 5. Specifies the length.
 // 6. Creates a Structure System1 with three structure system point length members.
 // 7. Inspect the structure system in the graphics area.
 // 8. Press F5 to edit the structure system.
 // 9. Gets one structure system member.
 // 10. Changes the length and member extensions in directions 1 and 2.
 // 11. Modifies the structure system.
 // 12. Inspect the changes in the graphics area.
 // ========================================================================

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace PointLength_CSharp
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
            private   PrimaryMemberPointLengthFeatureData memPointLengthDef;
            private  object[] startPoints =   new   object[3];
            private  bool stat;
            private   StructureSystemMemberFeatureData[] memData =   new   StructureSystemMemberFeatureData[1];
            private  object[] memDataArray;
            private  Feature systemFeature;
            private  StructureSystemFolder structSysModDef;
            private  object[] outProfiles;
            private   StructureSystemMemberFeatureData MemberData;
            private  object[] memberArray;
            private  Feature profileGrpFeat;
            private  ProfileGroupFolder profileGrp;
            private   StructureSystemMemberFeatureData memTochange;
            private   PrimaryMemberPointLengthFeatureData pointLengthMember;
            private  Feature memberFeat;
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
               PartDoc swPart;
              swPart = (PartDoc)modDoc;
              modDoc = (ModelDoc2)swApp.ActiveDoc;
              modDocExt = modDoc.Extension;
              swSelMgr = (SelectionMgr)modDoc.SelectionManager;
              modDoc.SketchManager.InsertSketch(true);
              stat = modDocExt.SelectByID2("Front Plane",  "PLANE", -0.0378286223842605d, 0.0426130572878663d, -0.00898903374939048d,  false, 0,  null, 0);
              modDoc.ClearSelection2(true);
               SketchPoint skPoint;
              skPoint = modDoc.SketchManager.CreatePoint(-0.040799d, 0.008094d, 0d);
              modDoc.ClearSelection2(true);
              modDoc.SketchManager.InsertSketch(true);
              stat = modDocExt.SelectByID2("Top Plane",  "PLANE", 0, 0, 0,   false, 0,   null, 0);
              modDoc.SketchManager.InsertSketch(true);
              skPoint = modDoc.SketchManager.CreatePoint(-0.023183d, 0.004864d, 0d);
              modDoc.ClearSelection2(true);
              modDoc.SketchManager.InsertSketch(true);
              stat = modDocExt.SelectByID2("Right Plane",  "PLANE", 0, 0, 0,   false, 0,   null, 0);
              modDoc.SketchManager.InsertSketch(true);
              skPoint = modDoc.SketchManager.CreatePoint(-0.020877d, 0.010539d, 0d);
              modDoc.ClearSelection2(true);
              modDoc.SketchManager.InsertSketch(true);
              modDoc.ClearSelection2(true);
              modDoc.ShowNamedView2("*Trimetric", 8);
              modDoc.ViewZoomtofit2();

               // Configure a structure system point length member
              structMemDef = (StructureSystemMemberFeatureData)modDocExt.CreateStructureSystemMemberData(2);
               Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " + structMemDef.StructureSystemMemberType);
              structMemDef.StartEndExtendD1 = 1.0d;
               Debug.Print("Extend length in direction 1: " + structMemDef.StartEndExtendD1);
              structMemDef.StartEndExtendD2 = 2.0d;
               Debug.Print("Extend length in direction 2: " + structMemDef.StartEndExtendD2);
              profDef = (StructureSystemMemberProfile)structMemDef.MemberProfile;
              profDef.ProfileStandard =   "ansi inch";
              profDef.ProfileType =   "c channel";
              profDef.ProfileSize =   "3 x 5";
              PrimDef = (PrimaryStructuralMemberFeatureData)structMemDef;
               Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " + PrimDef.PrimaryMemberType);
              memPointLengthDef = (PrimaryMemberPointLengthFeatureData)PrimDef;
              memPointLengthDef.EndCondition = 0;

               // Set three points that define three structure system point length members
              stat = modDocExt.SelectByID2("Point1@Sketch3",   "EXTSKETCHPOINT", -0.020877d, 0.010539d, 0,  false, 0,  null, 0);
              stat = modDocExt.SelectByID2("Point1@Sketch1",   "EXTSKETCHPOINT", -0.040799d, 0.008094d, 0,  true, 0,  null, 0);
              stat = modDocExt.SelectByID2("Point1@Sketch2",   "EXTSKETCHPOINT", -0.023183d, 0.004864d, 0,  true, 0,  null, 0);
              startPoints[0] = swSelMgr.GetSelectedObject6(1, 0);
              startPoints[1] = swSelMgr.GetSelectedObject6(2, 0);
              startPoints[2] = swSelMgr.GetSelectedObject6(3, 0);
               DispatchWrapper[] dArray;
              dArray = ObjectArrayToDispatchWrapperArray(startPoints);
              stat = memPointLengthDef.SetPoints(dArray);
              Debug.Print("Start points set successfully: " + stat);

               // Set the length for each member
              memPointLengthDef.Length = 5;
              memPointLengthDef.ReverseDirection =   false;
              memData[0] = structMemDef;
              memDataArray = memData;
              systemFeature = modDocExt.CreateStructureSystem(memDataArray,  null);
              modDoc.ViewZoomtofit2();
               Debugger.Break();
              structSysModDef = (StructureSystemFolder)systemFeature.GetSpecificFeature2();
               Debug.Print("Number of structure system profile groups: " + structSysModDef.GetProfileGroupFoldersCount());
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
                            Debug.Print("Number of members inside profile group " + profileGrp.GetStructureSystemMemberCount());
                          memberArray = (object[])profileGrp.GetStructureSystemMembers();
                           if (memberArray.Length > 0)
                          {
                                var loopTo1 = memberArray.GetUpperBound(0);
                                for (j = 0; j <= loopTo1; j++)
                              {
                                  MemberData = (StructureSystemMemberFeatureData)memberArray[j];   // Get one structure system member to change
                                    break;
                              }
                          }
                      }
                  }
              }

               // Changing one member only
              memTochange = MemberData;
               Debug.Print("Change member length and extensions in directions 1 and 2 for one member only");
              memTochange.StartEndExtendD1 = 0.1d;
              memTochange.StartEndExtendD2 = 0.1d;
              pointLengthMember = (PrimaryMemberPointLengthFeatureData)MemberData;
              pointLengthMember.Length = 1;

               // Save edits
              memberFeat = memTochange.GetFeature();
              stat = memberFeat.ModifyDefinition(MemberData, modDoc,  null);
           }

            // The SldWorks swApp variable is pre-assigned for you.
            public  SldWorks swApp;

      }
 }
```
