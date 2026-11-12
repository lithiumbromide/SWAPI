---
title: "Create Secondary Structure System Members Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Secondary_SSMembers_Example_VBNET.htm"
---

# Create Secondary Structure System Members Example (VB.NET)

This example shows how to create two secondary structure system members: one between primary member pair end points and the other on a support plane between a primary member pair.

```vb
  '==========================================================================================
 'Preconditions:
 '1. Ensure the specified part template exists.
 '2. Open an Immediate window.
 '3. Press F5.
 '
 'Postconditions:
 ' 1. Creates Sketch1 containing two sketch segments.
 ' 2. Configures the start/end extensions and the member profile.
 ' 3. Selects the two sketch segments.
 ' 4. Creates primary Structure System1 with two primary path segment members (Member1 and Member2).
 ' 5. Inspect the structure system in the graphics area.
 ' 6. Press F5 to add a secondary support plane member.
 '     Creates secondary Structure System2 (Member3).
 ' 7. Press F5 to edit the support plane member.
 ' 8. Press F5 to add a secondary between points member.
 '     Creates secondary Structure System3 (Member4).
 ' 9. Press F5 to edit the between points member.
```

'10. Press F5 to add a secondary structure system up to member.

'11. When the macro stops, multi-select a **Member1** vertex

' in the graphics area and **Member2** in the FeatureManager Design tree.

'12. Press F5 to create the secondary **Structure System4** (**Member5**).

'13. Inspect the Immediate window.

```vb
  '========================================================================
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim modDoc As ModelDoc2
     Dim swFeatMgr As FeatureManager
     Dim swSelMgr As SelectionMgr
     Dim modDocExt As ModelDocExtension
     Dim structMemDef As StructureSystemMemberFeatureData
     Dim profDef As StructureSystemMemberProfile
     Dim PrimDef As PrimaryStructuralMemberFeatureData
     Dim memPathSegDef As PrimaryMemberPathSegmentFeatureData
     Dim memBetweenPointsSecDef As SecondaryMemberBetweenPointsFeatureData
     Dim secMemDatTochange As SecondaryMemberBetweenPointsFeatureData
     Dim memSupportPlaneSecDef As SecondaryMemberSupportPlaneFeatureData
     Dim segments(2) As Object
     Dim stat As Boolean
     Dim memData(0) As StructureSystemMemberFeatureData
     Dim memDataArray() As Object
     Dim structSys As Feature
     Dim baseSecondarySystem As StructureSystemFolder
     Dim structSysDef As StructureSystemFolder
     Dim structSysSecDef As StructureSystemFolder
     Dim feat As Feature
     Dim structSysModDef As StructureSystemFolder
     Dim outProfiles() As Object
     Dim MemberData As StructureSystemMemberFeatureData
     Dim memberArray() As Object
     Dim profileGrpFeat As Feature
     Dim profileGrp As ProfileGroupFolder
     Dim memTochange As StructureSystemMemberFeatureData
     Dim I As Integer
     Dim j As Integer
```

Dim secDef As SecondaryStructuralMemberFeatureData

Dim UpToMemDef As SecondaryMemberUpToMembersFeatureData

Dim point As Object

Dim Members(0) As Object

```vb
     Function ObjectArrayToDispatchWrapperArray(ByVal Objects As Object()) As DispatchWrapper()
         Dim ArraySize As Integer
         ArraySize = Objects.GetUpperBound(0)
         Dim d(ArraySize) As DispatchWrapper
         Dim ArrayIndex As Integer
         For ArrayIndex = 0 To ArraySize
             d(ArrayIndex) = New DispatchWrapper(Objects(ArrayIndex))
         Next
         Return d
     End Function

     Sub main()

         Dim swSheetWidth As Double
         swSheetWidth = 0
         Dim swSheetHeight As Double
         swSheetHeight = 0
         modDoc = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2023\templates\Part.PRTDOT", 0, swSheetWidth, swSheetHeight)

         modDocExt = modDoc.Extension

         modDoc.SketchManager.InsertSketch(True)
         stat = modDocExt.SelectByID2("Front Plane", "PLANE", -0.077188654347454, 0.054268560279924, 0.00386214196026222, False, 0, Nothing, 0)
         modDoc.ClearSelection2(True)

         Dim skSegment As Object
         skSegment = modDoc.SketchManager.CreateLine(-0.168061, 0.084736, 0#, -0.168061, -0.077684, 0#)
         skSegment = modDoc.SketchManager.CreateLine(0.075216, 0.107771, 0#, 0.075216, -0.006699, 0#)
         modDoc.ClearSelection2(True)

         stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
         Dim myRefPlane As RefPlane
         myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.03, 0, 0, 0, 0)
         modDoc.ClearSelection2(True)
         stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
         modDoc.ClearSelection2(True)
         modDoc.SketchManager.InsertSketch(True)

         stat = modDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.168061313304597, 0.0544142573846353, 0, False, 0, Nothing, 0)
         stat = modDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 0.0752162521083513, 0.0532390034454423, 0, True, 0, Nothing, 0)

         'Create primary structure system path segment members
         structMemDef = modDocExt.CreateStructureSystemMemberData(0)
         Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " & structMemDef.StructureSystemMemberType)

         structMemDef.StartEndExtendD1 = 1.0#
         structMemDef.StartEndExtendD2 = 2.0#

         profDef = structMemDef.MemberProfile

         profDef.ProfileStandard = "ansi inch"
         profDef.ProfileType = "c channel"
         profDef.ProfileSize = "3 x 5"

         PrimDef = structMemDef
         Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " & PrimDef.PrimaryMemberType)

         memPathSegDef = PrimDef
         memPathSegDef.MergeTangentMembers = True

         swSelMgr = modDoc.SelectionManager

         Dim segments(1) As Object
         segments(0) = swSelMgr.GetSelectedObject6(1, 0)
         segments(1) = swSelMgr.GetSelectedObject6(2, 0)

         Dim dArray() As DispatchWrapper
         dArray = ObjectArrayToDispatchWrapperArray(segments)

         stat = memPathSegDef.SetPathSegments(dArray)
         Debug.Print("Path segments successfully set: " & stat)

         Dim PrimMemData(0) As StructureSystemMemberFeatureData
         PrimMemData(0) = structMemDef

         Dim PrimMemDatArray() As Object
         PrimMemDatArray = PrimMemData

         Dim structSysFeat As Feature
         structSysFeat = modDocExt.CreateStructureSystem(PrimMemDatArray, Nothing)

         modDoc.ViewZoomtofit

         Stop

         structSysDef = structSysFeat.GetSpecificFeature2
         Debug.Print("Number of profile group folders: " & structSysDef.GetProfileGroupFoldersCount)

         Dim outProfiles() As Object
         outProfiles = structSysDef.GetProfileGroupFolders()

         Dim memberArray() As Object

         If (outProfiles.Length > 0) Then
             For I = 0 To UBound(outProfiles)
                 profileGrpFeat = outProfiles(I)
                 profileGrp = profileGrpFeat.GetSpecificFeature2
                 If Not profileGrp Is Nothing Then
                     Debug.Print("Number of members in profile group: " & profileGrp.GetStructureSystemMemberCount)
                     memberArray = profileGrp.GetStructureSystemMembers()
                     If (memberArray.Length > 0) Then
                         Exit For
                     End If
                 End If
             Next
         End If

         'Create secondary structure system support plane member
         Dim structSecMemDef As StructureSystemMemberFeatureData
         structSecMemDef = modDocExt.CreateStructureSystemMemberData(4) 'Secondary Support Plane

         Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " & structMemDef.StructureSystemMemberType)

         structSecMemDef.StartEndExtendD1 = 0.5
         structSecMemDef.StartEndExtendD2 = 0.5

         Dim secProfDef As StructureSystemMemberProfile
         secProfDef = structSecMemDef.MemberProfile

         secProfDef.ProfileStandard = "ansi inch"
         secProfDef.ProfileType = "c channel"
         secProfDef.ProfileSize = "3 x 5"

         Dim SecDef As SecondaryStructuralMemberFeatureData
         SecDef = structSecMemDef
         Debug.Print("Structure system secondary member creation type as defined by swStructureSystemMemberCreationType_e: " & SecDef.SecondaryMemberType)

         memSupportPlaneSecDef = SecDef

         Dim eArray() As DispatchWrapper
         eArray = ObjectArrayToDispatchWrapperArray(memberArray)

         stat = memSupportPlaneSecDef.SetMemberPairs(eArray)
         Debug.Print("Member pairs set successfully: " & stat)

         stat = modDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
         Dim Planes(0) As Object
         Planes(0) = swSelMgr.GetSelectedObject6(1, 0)

         Dim fArray() As DispatchWrapper
         fArray = ObjectArrayToDispatchWrapperArray(Planes)

         stat = memSupportPlaneSecDef.SetIntersectingPlanesAndFaces(fArray)
         Debug.Print("Intersecting plane set successfully: " & stat)

         Dim secMemData(0) As StructureSystemMemberFeatureData
         secMemData(0) = structSecMemDef

         Dim secMemDatArray() As Object
         secMemDatArray = secMemData

         Dim structSysFeat2 As Feature
         structSysFeat2 = modDocExt.CreateStructureSystem(Nothing, secMemDatArray)

         modDoc.ViewZoomtofit

         Stop

         'Edit secondary support plane member by changing start/end extensions
         baseSecondarySystem = structSysFeat2.GetSpecificFeature2
         Debug.Print("Number of profile group folders: " & baseSecondarySystem.GetProfileGroupFoldersCount)

         outProfiles = baseSecondarySystem.GetProfileGroupFolders()

         Dim secMemberData As Object
         Dim SecMemberArray() As Object
         Dim secProfileGrpFeat As Feature
         Dim secProfileGrp As ProfileGroupFolder
         If (outProfiles.Length > 0) Then
             For I = 0 To UBound(outProfiles)
                 secProfileGrpFeat = outProfiles(I)
                 secProfileGrp = secProfileGrpFeat.GetSpecificFeature2
                 If Not secProfileGrp Is Nothing Then
                     Debug.Print("Number of members in profile group: " & secProfileGrp.GetStructureSystemMemberCount)
                     SecMemberArray = secProfileGrp.GetStructureSystemMembers()
                     If (SecMemberArray.Length > 0) Then
                         For j = 0 To UBound(SecMemberArray)
                             secMemberData = SecMemberArray(j)
                             Exit For
                         Next
                     End If
                 End If
             Next
         End If

         Dim memTochange As StructureSystemMemberFeatureData
         memTochange = secMemberData
         Dim SecMemFeat As Feature
         SecMemFeat = memTochange.GetFeature()
         memTochange.StartEndExtendD1 = 0.2
         memTochange.StartEndExtendD2 = 0.1

         stat = SecMemFeat.ModifyDefinition(secMemberData, modDoc, Nothing)

         Stop

         'Create secondary between points member
         structSecMemDef = modDocExt.CreateStructureSystemMemberData(5)
         Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " & structMemDef.StructureSystemMemberType)

         secProfDef = structSecMemDef.MemberProfile

         secProfDef.ProfileStandard = "ansi inch"
         secProfDef.ProfileType = "c channel"
         secProfDef.ProfileSize = "3 x 5"

         SecDef = structSecMemDef
         Debug.Print("Structure system secondary member creation type as defined by swStructureSystemMemberCreationType_e: " & SecDef.SecondaryMemberType)

         memBetweenPointsSecDef = SecDef

         stat = memBetweenPointsSecDef.SetMemberPairs(eArray)
         Debug.Print("Member pairs successfully set: " & stat)

         memBetweenPointsSecDef.SecondaryMemberOffsetType = 0
         memBetweenPointsSecDef.DistanceMember1 = 0.5
         memBetweenPointsSecDef.DistanceMember2 = 0.4
         memBetweenPointsSecDef.RevDirectionDistanceMember1 = False
         memBetweenPointsSecDef.RevDirectionDistanceMember2 = False

         secMemData(0) = structSecMemDef

         secMemDatArray = secMemData

         structSysFeat2 = modDocExt.CreateStructureSystem(Nothing, secMemDatArray)

         Stop

         'Edit between points member by changing start/end extensions and offset type
         structSysSecDef = structSysFeat2.GetSpecificFeature2
         Debug.Print("Number of profile group folders: " & structSysSecDef.GetProfileGroupFoldersCount)

         Dim outSecProfiles() As Object
         outSecProfiles = structSysSecDef.GetProfileGroupFolders()

         If (outSecProfiles.Length > 0) Then
             For I = 0 To UBound(outSecProfiles)
                 secProfileGrpFeat = outSecProfiles(I)
                 secProfileGrp = secProfileGrpFeat.GetSpecificFeature2
                 If Not secProfileGrp Is Nothing Then
                     Debug.Print("Number of members in profile group: " & secProfileGrp.GetStructureSystemMemberCount)
                     SecMemberArray = secProfileGrp.GetStructureSystemMembers()
                     If (SecMemberArray.Length > 0) Then
                         For j = 0 To UBound(SecMemberArray)
                             secMemberData = SecMemberArray(j)
                         Next
                     End If
                 End If
             Next
         End If

         memTochange = secMemberData

         SecMemFeat = memTochange.GetFeature()
         memTochange.StartEndExtendD1 = 0.2
         memTochange.StartEndExtendD2 = 0.1

         secMemDatTochange = memTochange
         secMemDatTochange.SecondaryMemberOffsetType = 1
         secMemDatTochange.LengthRatioMember1 = 0.1
         secMemDatTochange.LengthRatioMember2 = 0.2
         stat = SecMemFeat.ModifyDefinition(secMemberData, modDoc, Nothing)
```

'Create secondary structure system up to member

structMemDef = modDocExt.**CreateStructureSystemMemberData**(6)

Debug.Print("Structure system member type as defined by swStructureSystemMemberType_e: " & structMemDef.**StructureSystemMemberType**)

structMemDef.**StartEndExtendD1** = 0.0

Debug.Print("Start/end direction 1: " & structMemDef.**StartEndExtendD1**)

structMemDef.**StartEndExtendD2** = 0.0

Debug.Print("Start/end direction 2: " & structMemDef.**StartEndExtendD2**)

profDef = structMemDef.**MemberProfile**

profDef.**ProfileStandard** = "ansi inch"

profDef.**ProfileType** = "pipe"

profDef.**ProfileSize** = "0.5 sch 40"

SecDef = structMemDef

Debug.Print("Secondary member type as defined by swStructureSystemMemberCreationType_e: " & SecDef.**SecondaryMemberType**)

UpToMemDef = SecDef

UpToMemDef.**MemberPointParametersType** = swSecondaryMemberUpToMembersMemberPointParameters_e.swSecondaryMemberUpToMembersMemberPointParameters_FromPoint

Stop 'Multi-Select a Member1 vertex In the graphics area And Member2 In the FeatureManager Design tree

point = swSelMgr.GetSelectedObject6(1, 0)

Members(0) = swSelMgr.GetSelectedObject6(2, 0)

UpToMemDef.**SetFromPoint**(point)

Dim gArray() As DispatchWrapper

gArray = ObjectArrayToDispatchWrapperArray(Members)

UpToMemDef.**SetFromPointMembers(**gArray)

UpToMemDef.**SecondaryMemberOffsetType** = swSecondaryMemberUpToMembersDistanceFromEndType_e.swSecondaryMemberUpToMembersDistanceFromEndType_Distance

UpToMemDef.**DistanceMember** = 0.1

UpToMemDef.**RevDirectionDistanceMember** = False

memData(0) = structMemDef

memDataArray = memData

Dim structSysFeat3 As Feature

structSysFeat3 = modDocExt.**CreateStructureSystem**(Nothing, memDataArray)

```vb
     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks
 End Class
```
