---
title: "Create Face Plane Intersection Structure System Member (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Face_Plane_Intersection_SSMember_Example_VBNET.htm"
---

# Create Face Plane Intersection Structure System Member (VB.NET)

This example shows how to create a structure system member along the intersection of a face and a plane.

```vb
  '==========================================================================================
 'Preconditions:
  '1. Ensure the specified part template exists.
 '2. Open an Immediate window.
 '3. Press F5.
 '
 'Postconditions:
 ' 1. Creates  Boss-Extrude1 and Plane1 in a new part.
 ' 2. Selects a parameter face on the extrusion.
 ' 3. Selects  Plane1.
 ' 4. Creates a face plane intersection member along the intersection of the selected face and plane.
 ' 5. Creates a  Structure System1.
 ' 6. Inspect the member on Plane1 in the graphics area.
 ' 7. Press F5 to edit the structure system.
 ' 8. Gets all of the structure system members in all of the profile group folders.
 ' 9. Changes the member extension lengths in directions 1 and 2.
 '10. Selects the  Right Plane to intersect the parameter face.
 '11. Modifies the structure system.
 '12. Inspect the member move to the Right Plane in the graphics area.
  '========================================================================
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Diagnostics
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
       Dim facePlaneIntrSecDef  As   PrimaryMemberFacePlaneIntersectionFeatureData
       Dim faces(0)  As  Object
       Dim stat  As  Boolean
       Dim IntSecPlane(0)  As   Object
       Dim memData(0)  As   StructureSystemMemberFeatureData
       Dim memDataArray()  As   Object
       Dim structSys  As   Feature
       Dim structSysModDef  As   StructureSystemFolder
       Dim outProfiles()  As   Object
       Dim MemberData  As   StructureSystemMemberFeatureData
       Dim memberArray()  As   Object
       Dim profileGrpFeat  As   Feature
       Dim profileGrp  As   ProfileGroupFolder
       Dim memTochange  As   StructureSystemMemberFeatureData
       Dim faceIntrMemberToChange  As   PrimaryMemberFacePlaneIntersectionFeatureData
       Dim newIntSecPlane(0)  As   Object
       Dim feat  As  Feature
       Dim I  As Integer
       Dim j  As Integer

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
            Dim swPart  As  PartDoc
           swPart = modDoc
           modDoc = swApp.ActiveDoc

          modDocExt = modDoc.Extension
           swSelMgr = modDoc.SelectionManager

           stat = modDocExt.SelectByID2("Right Plane",  "PLANE", 0, 0, 0,   False, 0,   Nothing, 0)
           modDoc.SketchManager.InsertSketch(True)
           modDoc.ClearSelection2(True)
           stat = modDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity,   swUserPreferenceOption_e.swDetailingNoOptionSpecified,   False)
           stat = modDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType,   swUserPreferenceOption_e.swDetailingNoOptionSpecified,   True)
            Dim vSkLines()  As   Object
           vSkLines = modDoc.SketchManager.CreateCornerRectangle(-0.0168788132580097, 0.0116544186781496, 0, 0.0139317188796271, -0.00736773594595662, 0)

           modDoc.ShowNamedView2("*Trimetric", 8)
           modDoc.ViewZoomtofit2()
            Dim myFeature  As   Feature
           myFeature = modDoc.FeatureManager.FeatureExtrusion2(False,  False,  False, 0, 0, 0.2, 0.2,   False,   False,   False,   False, 0.0174532925199433, 0.0174532925199433,  False,  False,  False,  False,  True,  True,  True, 0, 0,  False)
           swSelMgr.EnableContourSelection =   False
           stat = modDocExt.SelectByRay(0.199999999999932, 0.00280649656951937, 0.000880259028576802, -0.400036026779314, -0.515038074910018, -0.758094294050287, 0.00111139990390966, 2,  False, 0, 0)
            Dim myRefPlane  As   RefPlane
           myRefPlane = modDoc.FeatureManager.InsertRefPlane(4, 0, 0, 0, 0, 0)
           modDoc.ClearSelection2(True)

            'Configure a structure system face plane intersection member
           structMemDef = modDocExt.CreateStructureSystemMemberData(3)
          Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " & structMemDef.StructureSystemMemberType)

           structMemDef.StartEndExtendD1 = 0.4
            Debug.Print("Extend length in direction 1: " & structMemDef.StartEndExtendD1)
           structMemDef.StartEndExtendD2 = 0.15
            Debug.Print("Extend length in direction 2: " & structMemDef.StartEndExtendD2)

           profDef = structMemDef.MemberProfile

           profDef.ProfileStandard =   "ansi inch"
           profDef.ProfileType =   "c channel"
           profDef.ProfileSize =   "3 x 5"

           PrimDef = structMemDef
            Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " & PrimDef.PrimaryMemberType)

           facePlaneIntrSecDef = PrimDef

           facePlaneIntrSecDef.MergeTangentMembers =   False

            'Select parameter face and intersecting plane
           stat = modDocExt.SelectByRay(-0.00017443058891331, 0.0116544186780629, -0.000426704146832435, -0.400036026779314, -0.515038074910018, -0.758094294050287, 0.000189520697225961, 2,  False, 0, 0)
           faces(0) = swSelMgr.GetSelectedObject6(1, -1)
           stat = modDocExt.SelectByID2("Plane1",   "PLANE", 0, 0, 0,   False, 0,   Nothing, 0)
           IntSecPlane(0) = swSelMgr.GetSelectedObject6(1, -1)

            Dim dArray()  As  DispatchWrapper
            Dim eArray()  As  DispatchWrapper
            Dim fArray()  As  DispatchWrapper

           dArray = ObjectArrayToDispatchWrapperArray(faces)

           stat = facePlaneIntrSecDef.SetParameterFaces(dArray)
            Debug.Print("Member's parameter face set successfully: " & stat)

           eArray = ObjectArrayToDispatchWrapperArray(IntSecPlane)

           stat = facePlaneIntrSecDef.SetIntersectingPlanesAndFaces(eArray)
            Debug.Print("Member's intersecting plane set successfully: " & stat)

           memData(0) = structMemDef

           fArray = ObjectArrayToDispatchWrapperArray(memData)

            'Create Structure System1 in the FeatureManager design tree
           structSys = modDocExt.CreateStructureSystem(fArray,  Nothing)

           modDoc.ViewZoomtofit2()

            Stop

            Debug.Print("")
            Debug.Print("Edit Structure System1...")

           structSysModDef = structSys.GetSpecificFeature2()
            Debug.Print("Number of structure system profile groups: " & structSysModDef.GetProfileGroupFoldersCount)

           outProfiles = structSysModDef.GetProfileGroupFolders()

            If (outProfiles.Length > 0)   Then
               For I = 0  To UBound(outProfiles)
                  profileGrpFeat = outProfiles(I)
                  profileGrp = profileGrpFeat.GetSpecificFeature2
                   If  Not profileGrp  Is   Nothing   Then
                        Debug.Print("Number of members inside group: " & profileGrp.GetStructureSystemMemberCount)
                      memberArray = profileGrp.GetStructureSystemMembers()
                       If (memberArray.Length > 0)  Then
                            For j = 0  To UBound(memberArray)
                              MemberData = memberArray(j)
                                Exit   For
                            Next
                        End  If
                   End  If
               Next
            End  If

           memTochange = MemberData
          feat = memTochange.GetFeature()

            Debug.Print("Change member extensions in directions 1 and 2...")
           memTochange.StartEndExtendD1 = 0.1
           memTochange.StartEndExtendD2 = 0.2

           faceIntrMemberToChange = memTochange

           modDoc.ClearSelection2(True)

           stat = modDocExt.SelectByID2("Right Plane",  "PLANE", 0, 0, 0,   True, 0,   Nothing, 0)
           newIntSecPlane(0) = swSelMgr.GetSelectedObject6(1, -1)
           dArray = ObjectArrayToDispatchWrapperArray(newIntSecPlane)
           stat = faceIntrMemberToChange.SetIntersectingPlanesAndFaces(dArray)
            Debug.Print("Intersecting plane successfully changed: " & stat)

           stat = feat.ModifyDefinition(MemberData, modDoc,  Nothing)

       End  Sub

       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
