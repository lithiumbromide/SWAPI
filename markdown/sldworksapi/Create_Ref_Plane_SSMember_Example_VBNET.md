---
title: "Create Reference Plane Structure System Member Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ref_Plane_SSMember_Example_VBNET.htm"
---

# Create Reference Plane Structure System Member Example (VB.NET)

This example shows how to create a structure system member along the intersection of two or more planes.

```vb
  '==========================================================================================
 'Preconditions:
 '1. Ensure the specified part template exists.
 '2. Open an Immediate window.
 '3. Press F5.
 '
 'Postconditions:
 ' 1. Creates five reference planes:
 '       - Plane1 parallel to Right Plane
 '       - Plane2 and Plane3 parallel to and flanking Top Plane
 '       - Plane4 and Plane5 parallel to and flanking Front Plane
 ' 2. Configures the member profile.
 ' 3. Selects the start/end reference planes that define the lengths of the members: Plane1 and Right Plane.
 ' 4. Selects the axis reference planes that define the direction of the members: Plane2 and Plane3.
 ' 5. Selects the location reference planes that define the positions of the members: Plane4 and Plane5.
 ' 6. Creates a Structure System1 with nine structure system reference plane members.
 ' 7. Inspect the structure system in the graphics area.
 ' 8. Press F5 to edit the structure system.
 ' 9. Gets Member1.
 '10. Changes its extensions in directions 1 and 2.
 '11. Modifies the structure system.
 '12. Inspect the changes in the graphics area.
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
       Dim memRefPlaneDef  As   PrimaryMemberRefPlaneFeatureData
       Dim startEndPlanes(1)  As   Object
       Dim horzPlanes(2)  As   Object
       Dim vertPlanes(2)  As   Object
       Dim stat  As  Boolean
       Dim memData(0)  As   StructureSystemMemberFeatureData
       Dim memDataArray()  As   Object
       Dim structSysFeat  As   Feature
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

           swSelMgr = modDoc.SelectionManager
           modDocExt = modDoc.Extension

           stat = modDocExt.SelectByID2("Right Plane",  "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)

            Dim myRefPlane  As   Object
           myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.381, 0, 0, 0, 0)
           modDoc.ClearSelection2(True)
           stat = modDocExt.SelectByID2("Top Plane",  "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)
           myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.1778, 0, 0, 0, 0)
           modDoc.ClearSelection2(True)
           stat = modDocExt.SelectByID2("Plane1",   "PLANE", 0, 0, 0,   False, 0,   Nothing, 0)
           modDoc.ClearSelection2(True)
           stat = modDocExt.SelectByID2("Top Plane",  "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)
           myRefPlane = modDoc.FeatureManager.InsertRefPlane(264, 0.1778, 0, 0, 0, 0)
           modDoc.ClearSelection2(True)
           stat = modDocExt.SelectByID2("Plane2",   "PLANE", 0, 0, 0,   False, 0,   Nothing, 0)
           modDoc.ClearSelection2(True)
           stat = modDocExt.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)
           myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.1778, 0, 0, 0, 0)
           modDoc.ClearSelection2(True)
           stat = modDocExt.SelectByID2("Plane3",   "PLANE", 0, 0, 0,   False, 0,   Nothing, 0)
           modDoc.ClearSelection2(True)
           stat = modDocExt.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)
           myRefPlane = modDoc.FeatureManager.InsertRefPlane(264, 0.1778, 0, 0, 0, 0)
           modDoc.ClearSelection2(True)
           stat = modDocExt.SelectByID2("Plane4",   "PLANE", 0, 0, 0,   False, 0,   Nothing, 0)
           modDoc.ClearSelection2(True)

           stat = modDocExt.SelectByID2("Right Plane",  "PLANE", 0, 0, 0,   False, 0,   Nothing, 0)
           stat = modDocExt.SelectByID2("Plane1",   "PLANE", 0.0729275826275853, 0.103693179609365, 0.188906126602433,   True, 0,   Nothing, 0)
           stat = modDocExt.SelectByID2("Plane2",   "PLANE", -0.035035924945646, 0.0882769827595098, 0.154770056203461,   True, 0,   Nothing, 0)
           stat = modDocExt.SelectByID2("Top Plane",  "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)
           stat = modDocExt.SelectByID2("Plane3",   "PLANE", -0.0359335022268397, 0.0486897858681345, 0.154489603864079,  True, 0,  Nothing, 0)
           stat = modDocExt.SelectByID2("Plane4",   "PLANE", -0.0353613843872154, 0.122848840931965, 0.120060929442332,   True, 0,   Nothing, 0)
           stat = modDocExt.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)
           stat = modDocExt.SelectByID2("Plane5",   "PLANE", -0.0313617150023902, 0.123208535607716, 0.0798165581882131,   True, 0,   Nothing, 0)

            'Create structure system reference plane member
           structMemDef = modDocExt.CreateStructureSystemMemberData(1)
            Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " & structMemDef.StructureSystemMemberType)

            Debug.Print("Extend length in direction 1 (m): " & structMemDef.StartEndExtendD1)
            Debug.Print("Extend length in direction 2 (m): " & structMemDef.StartEndExtendD2)

           profDef = structMemDef.MemberProfile

           profDef.ProfileStandard =   "ansi inch"
           profDef.ProfileType =   "c channel"
           profDef.ProfileSize =   "3 x 5"

           PrimDef = structMemDef
            Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " & PrimDef.PrimaryMemberType)

           memRefPlaneDef = PrimDef

            'Define the member lengths
           startEndPlanes(0) = swSelMgr.GetSelectedObject6(1, 0)
           startEndPlanes(1) = swSelMgr.GetSelectedObject6(2, 0)

            Dim dArray()  As  DispatchWrapper
           dArray = ObjectArrayToDispatchWrapperArray(startEndPlanes)

           stat = memRefPlaneDef.SetStartAndEndReferences(dArray)
            Debug.Print("Reference planes set successfully: " & stat)

           horzPlanes(0) = swSelMgr.GetSelectedObject6(3, 0)
           horzPlanes(1) = swSelMgr.GetSelectedObject6(4, 0)
           horzPlanes(2) = swSelMgr.GetSelectedObject6(5, 0)

            Dim eArray()  As  DispatchWrapper
           eArray = ObjectArrayToDispatchWrapperArray(horzPlanes)

           stat = memRefPlaneDef.SetReferenceAxes(eArray)
            Debug.Print("Reference axis planes set successfully: " & stat)

           vertPlanes(0) = swSelMgr.GetSelectedObject6(6, 0)
           vertPlanes(1) = swSelMgr.GetSelectedObject6(7, 0)
           vertPlanes(2) = swSelMgr.GetSelectedObject6(8, 0)

            Dim fArray()  As  DispatchWrapper
           fArray = ObjectArrayToDispatchWrapperArray(vertPlanes)

           stat = memRefPlaneDef.SetReferenceLocations(fArray)
            Debug.Print("Reference location planes set successfully: " & stat)

           memData(0) = structMemDef

          memDataArray = memData

           structSysFeat = modDocExt.CreateStructureSystem(memDataArray,  Nothing)

           modDoc.ShowNamedView2("*Trimetric", 8)
           modDoc.ViewZoomtofit2()

            Stop

           structSysModDef = structSysFeat.GetSpecificFeature2
            Debug.Print("Number of profile group folders: " & structSysModDef.GetProfileGroupFoldersCount)

           outProfiles = structSysModDef.GetProfileGroupFolders()

            If (outProfiles.Length > 0)   Then
               For I = 0  To UBound(outProfiles)
                  profileGrpFeat = outProfiles(I)
                  profileGrp = profileGrpFeat.GetSpecificFeature2
                   If  Not profileGrp  Is   Nothing   Then
                        Debug.Print("Number of members in profile group folder: " & profileGrp.GetStructureSystemMemberCount)
                      memberArray = profileGrp.GetStructureSystemMembers()
                       If (memberArray.Length > 0)  Then
                            For j = 0  To UBound(memberArray)
                              MemberData = memberArray(j)   'Get first member only
                                Exit   For
                            Next
                        End  If
                   End  If
               Next
            End  If

           memTochange = MemberData

           feat = memTochange.GetFeature()

            'Change the extensions in directions 1 and 2 for Member1
           memTochange.StartEndExtendD1 = 0.5
           memTochange.StartEndExtendD2 = 0.2

           modDoc.ClearSelection2(True)

            Debug.Print("Member extensions set successfully: " & stat)

            'Save edits
           stat = feat.ModifyDefinition(MemberData, modDoc,  Nothing)

       End  Sub

       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
