---
title: "Create Path Segment Structure System Member Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Path_Segment_SSMember_Example_VBNET.htm"
---

# Create Path Segment Structure System Member Example (VB.NET)

This example shows how to create structure system path segment members that are split along a reference plane.

```vb
  '==========================================================================================
 'Preconditions:
 '1. Ensure the specified part template exists.
 '2. Open an Immediate window.
 '3. Press F5.
 '
 'Postconditions:
 ' 1. Creates Sketch1 containing two sketch segments.
 ' 2. Creates Plane1.
 ' 3. Configures the start/end extensions and the member profile.
 ' 4. Selects two sketch segments and Plane1.
 ' 5. Configures structure system to split members using Plane1.
 ' 6. Creates a Structure System1 with four split members: Member1_1, Member1_2, Member2_1, and Member2_2.
 ' 7. Inspect the structure system in the graphics area.
 ' 8. Press F5 to edit the structure system.
 ' 9. Changes the start/end extensions for Member1_1 and Member1_2.
 '10. Modifies the structure system.
 '11. Inspect the changes in the graphics area.
  '========================================================================
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial   Class   SolidWorksMacro

       Dim modDoc  As  ModelDoc2
       Dim swFeatMgr  As   FeatureManager
       Dim swSelMgr  As  SelectionMgr
       Dim modDocExt  As   ModelDocExtension
       Dim structMemDef  As   StructureSystemMemberFeatureData
       Dim profDef  As   StructureSystemMemberProfile
       Dim PrimDef  As   PrimaryStructuralMemberFeatureData
       Dim memPathSegDef  As   PrimaryMemberPathSegmentFeatureData
       Dim segments(1)  As   Object
       Dim stat  As  Boolean
       Dim memData(0)  As   StructureSystemMemberFeatureData
       Dim memDataArray()  As   Object
       Dim structSys  As   Feature
       Dim feat  As  Feature
       Dim structSysModDef  As   StructureSystemFolder
       Dim outProfiles()  As   Object
       Dim MemberData  As   StructureSystemMemberFeatureData
       Dim memberArray()  As   Object
       Dim profileGrpFeat  As   Feature
       Dim profileGrp  As   ProfileGroupFolder
       Dim memTochange  As   StructureSystemMemberFeatureData
       Dim I  As  Integer
       Dim j  As  Integer

       Function ObjectArrayToDispatchWrapperArray(ByVal Objects  As  Object())  As   DispatchWrapper()
            Dim ArraySize  As   Integer
           ArraySize = Objects.GetUpperBound(0)
            Dim d(ArraySize)  As   DispatchWrapper
            Dim ArrayIndex  As   Integer
            For ArrayIndex = 0  To ArraySize
              d(ArrayIndex) =   New   DispatchWrapper(Objects(ArrayIndex))
            Next
            Return d
       End  Function

       Sub main()

            Dim swSheetWidth  As   Double
           swSheetWidth = 0
            Dim swSheetHeight  As   Double
           swSheetHeight = 0
           modDoc = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Part.PRTDOT", 0, swSheetWidth, swSheetHeight)
           modDoc = swApp.ActiveDoc

           modDocExt = modDoc.Extension
           swSelMgr = modDoc.SelectionManager

           modDoc.SketchManager.InsertSketch(True)
           stat = modDocExt.SelectByID2("Front Plane",  "PLANE", -0.0550812963393624, 0.0228249965575248, 0.0135586835718293,  False, 0,  Nothing, 0)
           modDoc.ClearSelection2(True)
            Dim skSegment  As   Object
           skSegment = modDoc.SketchManager.CreateLine(-0.036101, -0.017052, 0#, 0.03111, 0.018383, 0#)
           skSegment = modDoc.SketchManager.CreateLine(0.055067, -0.015222, 0#, -0.01281, -0.055483, 0#)

          modDoc.SketchManager.InsertSketch(True)
           modDoc.ClearSelection2(True)

           stat = modDocExt.SelectByID2("Right Plane",  "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)
            Dim myRefPlane  As   RefPlane
           myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.02, 0, 0, 0, 0)
           modDoc.ClearSelection2(True)

           stat = modDocExt.SelectByID2("Line1@Sketch1",   "EXTSKETCHSEGMENT", -0.0123094293114227, -0.00450860223252535, 0,  True, 0,   Nothing, 0)
           stat = modDocExt.SelectByID2("Line2@Sketch1",   "EXTSKETCHSEGMENT", 1.11728134432853, -0.0376344266391984, 0,  True, 0,  Nothing, 0)
           stat = modDocExt.SelectByID2("Plane1",   "PLANE", 0.0199883401957978, 0.0202450835544425, -0.0243017856732353,   True, 0,   Nothing, 0)

           structMemDef = modDocExt.CreateStructureSystemMemberData(0)

            Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " & structMemDef.StructureSystemMemberType)

           structMemDef.StartEndExtendD1 = 0.1
            Debug.Print("Extend length in direction 1 (m): " & structMemDef.StartEndExtendD1)
           structMemDef.StartEndExtendD2 = 0.2
            Debug.Print("Extend length in direction 2 (m): " & structMemDef.StartEndExtendD2)

           profDef = structMemDef.MemberProfile

           profDef.ProfileStandard =   "ansi inch"
           profDef.ProfileType =   "c channel"
           profDef.ProfileSize =   "3 x 5"

           PrimDef = structMemDef
            Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " & PrimDef.PrimaryMemberType)

           memPathSegDef = PrimDef
           memPathSegDef.MergeTangentMembers =   True
            Debug.Print("Merge tangent members? " & memPathSegDef.MergeTangentMembers)

           segments(0) = swSelMgr.GetSelectedObject6(1, 0)
           segments(1) = swSelMgr.GetSelectedObject6(2, 0)

            Dim dArray()  As  DispatchWrapper
           dArray = ObjectArrayToDispatchWrapperArray(segments)

           stat = memPathSegDef.SetPathSegments(dArray)
            Debug.Print("Path segments set successfully: " & stat)

            Dim planes(0)  As   Object
           planes(0) = swSelMgr.GetSelectedObject6(3, 0)
           structMemDef.IsSplit =   True
            Dim structSplitMember  As   StructureSystemSplitMember
           structSplitMember = structMemDef.GetSplitMember
           structSplitMember.MemberType =   swStructureSplitMemberType_e.swStructureSplitMember_Reference

            Dim eArray()  As  DispatchWrapper
           eArray = ObjectArrayToDispatchWrapperArray(planes)

           stat = structSplitMember.SetSplitReferences(eArray)

           memData(0) = structMemDef

            Dim fArray()  As  DispatchWrapper
           fArray = ObjectArrayToDispatchWrapperArray(memData)

           structSys = modDocExt.CreateStructureSystem(fArray,  Nothing)

           modDoc.ViewZoomtofit

            Stop

            'Edit the structure system
           structSysModDef = structSys.GetSpecificFeature2
            Debug.Print("Number of profile group folders: " & structSysModDef.GetProfileGroupFoldersCount)

           outProfiles = structSysModDef.GetProfileGroupFolders()

            If (outProfiles.Length > 0)   Then
               For I = 0  To UBound(outProfiles)
                  profileGrpFeat = outProfiles(I)
                  profileGrp = profileGrpFeat.GetSpecificFeature2
                   If  Not profileGrp  Is   Nothing   Then
                        Debug.Print("Number of members inside profile group folder: " & profileGrp.GetStructureSystemMemberCount)
                      memberArray = profileGrp.GetStructureSystemMembers()
                       If (memberArray.Length > 0)  Then
                            For j = 0  To UBound(memberArray)
                              MemberData = memberArray(j)  'Get Member1 only
                                Exit   For
                            Next
                        End  If
                   End  If
               Next
            End  If

           memTochange = MemberData

            'Change the start/end extensions for Member1
            Debug.Print("Change member extensions in directions 1 and 2 for one member only")
           feat = memTochange.GetFeature()
           memTochange.StartEndExtendD1 = 0.5
           memTochange.StartEndExtendD2 = 0.2

            'Save edits
           stat = feat.ModifyDefinition(MemberData, modDoc,  Nothing)

       End  Sub

       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
