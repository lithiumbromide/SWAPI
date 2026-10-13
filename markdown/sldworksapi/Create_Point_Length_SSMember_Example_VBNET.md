---
title: "Create Point Length Structure System Member Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Point_Length_SSMember_Example_VBNET.htm"
---

# Create Point Length Structure System Member Example (VB.NET)

This example shows how to create a structure system member that originates at a point and extends to a specified end condition.

```vb
  '==========================================================================================
 'Preconditions:
 '1. Ensure the specified part template exists.
 '2. Open an Immediate window.
 '3. Press F5.
 '
 'Postconditions:
 ' 1. Creates  Sketch1, Sketch2, and Sketch3 in a new part.
 ' 2. Configures the start/end extensions and the member profile.
 ' 3. Configures the length end condition for the structure members.
 ' 4. Selects three sketch points.
 ' 5. Specifies the length.
 ' 6. Creates a  Structure System1 with three structure system point length members.
 ' 7. Inspect the structure system in the graphics area.
 ' 8. Press F5 to edit the structure system.
 ' 9. Gets one structure system member.
 '10. Changes the length and member extensions in directions 1 and 2.
 '11. Modifies the structure system.
 '12. Inspect the changes in the graphics area.
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
       Dim memPointLengthDef  As   PrimaryMemberPointLengthFeatureData
       Dim startPoints(2)  As   Object
       Dim stat  As  Boolean
       Dim memData(0)  As   StructureSystemMemberFeatureData
       Dim memDataArray()  As   Object
       Dim systemFeature  As   Feature
       Dim structSysModDef  As   StructureSystemFolder
       Dim outProfiles()  As   Object
       Dim MemberData  As   StructureSystemMemberFeatureData
       Dim memberArray()  As   Object
       Dim profileGrpFeat  As   Feature
       Dim profileGrp  As   ProfileGroupFolder
       Dim memTochange  As   StructureSystemMemberFeatureData
       Dim pointLengthMember  As   PrimaryMemberPointLengthFeatureData
       Dim memberFeat  As   Feature
       Dim I  As   Integer
       Dim j  As   Integer

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

           modDoc.SketchManager.InsertSketch(True)
           stat = modDocExt.SelectByID2("Front Plane",  "PLANE", -0.0378286223842605, 0.0426130572878663, -0.00898903374939048,  False, 0,  Nothing, 0)
           modDoc.ClearSelection2(True)
            Dim skPoint  As  SketchPoint
           skPoint = modDoc.SketchManager.CreatePoint(-0.040799, 0.008094, 0#)
           modDoc.ClearSelection2(True)
           modDoc.SketchManager.InsertSketch(True)
           stat = modDocExt.SelectByID2("Top Plane",  "PLANE", 0, 0, 0,   False, 0,   Nothing, 0)
           modDoc.SketchManager.InsertSketch(True)
           skPoint = modDoc.SketchManager.CreatePoint(-0.023183, 0.004864, 0#)
           modDoc.ClearSelection2(True)
           modDoc.SketchManager.InsertSketch(True)
           stat = modDocExt.SelectByID2("Right Plane",  "PLANE", 0, 0, 0,   False, 0,   Nothing, 0)
           modDoc.SketchManager.InsertSketch(True)
           skPoint = modDoc.SketchManager.CreatePoint(-0.020877, 0.010539, 0#)
           modDoc.ClearSelection2(True)
           modDoc.SketchManager.InsertSketch(True)

           modDoc.ClearSelection2(True)
           modDoc.ShowNamedView2("*Trimetric", 8)
           modDoc.ViewZoomtofit2

            'Configure a structure system point length member
           structMemDef = modDocExt.CreateStructureSystemMemberData(2)

            Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " & structMemDef.StructureSystemMemberType)

           structMemDef.StartEndExtendD1 = 1.0#
            Debug.Print("Extend length in direction 1: " & structMemDef.StartEndExtendD1)
           structMemDef.StartEndExtendD2 = 2.0#
            Debug.Print("Extend length in direction 2: " & structMemDef.StartEndExtendD2)

           profDef = structMemDef.MemberProfile

           profDef.ProfileStandard =   "ansi inch"
           profDef.ProfileType =   "c channel"
           profDef.ProfileSize =   "3 x 5"

           PrimDef = structMemDef
            Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " & PrimDef.PrimaryMemberType)

           memPointLengthDef = PrimDef

           memPointLengthDef.EndCondition = 0

            'Set three points that define three structure system point length members
           stat = modDocExt.SelectByID2("Point1@Sketch3",   "EXTSKETCHPOINT", -0.020877, 0.010539, 0,  False, 0,  Nothing, 0)
           stat = modDocExt.SelectByID2("Point1@Sketch1",   "EXTSKETCHPOINT", -0.040799, 0.008094, 0,  True, 0,  Nothing, 0)
           stat = modDocExt.SelectByID2("Point1@Sketch2",   "EXTSKETCHPOINT", -0.023183, 0.004864, 0,  True, 0,  Nothing, 0)

           startPoints(0) = swSelMgr.GetSelectedObject6(1, 0)
           startPoints(1) = swSelMgr.GetSelectedObject6(2, 0)
           startPoints(2) = swSelMgr.GetSelectedObject6(3, 0)

            Dim dArray()  As  DispatchWrapper
           dArray = ObjectArrayToDispatchWrapperArray(startPoints)

           stat = memPointLengthDef.SetPoints(dArray)
            Debug.Print("Start points set successfully: " & stat)

            'Set the length for each member
           memPointLengthDef.Length = 5
           memPointLengthDef.ReverseDirection =   False

           memData(0) = structMemDef

           memDataArray = memData

           systemFeature = modDocExt.CreateStructureSystem(memDataArray,  Nothing)

           modDoc.ViewZoomtofit2

            Stop

           structSysModDef = systemFeature.GetSpecificFeature2
            Debug.Print("Number of structure system profile groups: " & structSysModDef.GetProfileGroupFoldersCount)

           outProfiles = structSysModDef.GetProfileGroupFolders()

            If (outProfiles.Length > 0)   Then
               For I = 0  To UBound(outProfiles)
                  profileGrpFeat = outProfiles(I)
                  profileGrp = profileGrpFeat.GetSpecificFeature2
                   If  Not profileGrp  Is   Nothing   Then
                        Debug.Print("Number of members inside profile group " & profileGrp.GetStructureSystemMemberCount)
                      memberArray = profileGrp.GetStructureSystemMembers()
                       If (memberArray.Length > 0)  Then
                            For j = 0  To UBound(memberArray)
                              MemberData = memberArray(j)  'Get one structure system member to change
                              Exit   For
                            Next
                        End  If
                   End  If
               Next
            End  If

            'Changing one member only
           memTochange = MemberData

            Debug.Print("Change member length and extensions in directions 1 and 2 for one member only")
           memTochange.StartEndExtendD1 = 0.1
           memTochange.StartEndExtendD2 = 0.1

           pointLengthMember = MemberData
           pointLengthMember.Length = 1

            'Save edits
           memberFeat = memTochange.GetFeature()
           stat = memberFeat.ModifyDefinition(MemberData, modDoc,  Nothing)

       End  Sub

       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
