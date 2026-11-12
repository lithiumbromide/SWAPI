---
title: "Access Structure System Corner Treatments Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_Structure_System_Corner_Treatments_Example_VBNET.htm"
---

# Access Structure System Corner Treatments Example (VB.NET)

This example shows how to access structure system corner treatments.

'==========================================================================================

'Preconditions:

'1. Open `public_documents`**\samples\tutorial\weldments\weldment_box.sldprt**.

'2. Open an Immediate window.

'3. Press F5.

'

'Postconditions:

'1. Creates **Structure System1**.

'2. Configures its weldment profile to have **<GB><round-rods><ROUND BAR 23>**.

'3. Creates **Corner Management1** containing:

' - **Two member Corner Group1**

' - **Simple Corner Group1**

' - **Complex Corner Group1**

'4. Press F5 to inspect the corner treatments.

'5. Inspect the Immediate window.

'6. Inspect the structure system and its corner management folder in the FeatureManager design tree.

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

Dim segments(5) As Object

Dim tsegments(0) As Object

Dim csegments(1) As Object

Dim stat As Boolean

Dim memData(0) As StructureSystemMemberFeatureData

Dim memDataArray As Object

Dim feat As Feature

Dim i As Integer

Dim k As Integer

Dim l As Integer

Dim m As Integer

Dim x As Integer

Dim Y As Integer

Dim swFeat As Feature

Dim complexCrnr As ComplexCornerTreatmentFeatureData

Dim strCornerName As String

Dim featArr As Object

Dim Count As Integer

Dim swStructSysFolder As StructureSystemFolder

Dim swCornerMgmtFolder As CornerManagementFolder

Dim grpArr As Object

Dim grpCnt As Integer

Dim crnrGrpFolder As CornerTreatmentGroupFolder

Dim crnrArr As Object

Dim crnrCnt As Integer

Dim crnrFeat As Feature

Dim crnrFeat2 As CornerTreatmentFeatureData

Dim simpleCrnr As SimpleCornerTreatmentFeatureData

Dim twoMbrCrnr As TwoMemberCornerTreatmentFeatureData

Dim member As CornerMember

Dim varBodyMem As Object

Dim obj As Object

Dim objType As Integer

Dim tmember As CornerMember

Dim crnrMbrArr As Object

Dim crnrMbr As CornerMember

Dim feat1 As Feature

Dim status As Boolean

Dim pmember As CornerMember

Dim varPlanarMem As Object

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

modDoc = swApp.ActiveDoc

modDocExt = modDoc.Extension

swSelMgr = modDoc.SelectionManager

swFeatMgr = modDoc.FeatureManager

'Create Structure System1

Debug.Print("Create Structure System1")

Debug.Print("")

stat = modDocExt.SelectByID2("Line4@3DSketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line1@Sketch2", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line3@3DSketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line6@3DSketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line3@Sketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line4@Sketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

structMemDef = modDocExt.**CreateStructureSystemMemberData**(0)

Debug.Print("Type of structure system member as defined by swStructureSystemMemberType_e: " & structMemDef.**StructureSystemMemberType**)

profDef = structMemDef.**MemberProfile**

profDef.**ProfileStandard** = "GB"

profDef.**ProfileType** = "round-rods"

profDef.**ProfileSize** = "ROUND BAR 23"

PrimDef = structMemDef

Debug.Print("Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " & PrimDef.**PrimaryMemberType**)

memPathSegDef = PrimDef

segments(0) = swSelMgr.GetSelectedObject6(1, 0)

segments(1) = swSelMgr.GetSelectedObject6(2, 0)

segments(2) = swSelMgr.GetSelectedObject6(3, 0)

segments(3) = swSelMgr.GetSelectedObject6(4, 0)

segments(4) = swSelMgr.GetSelectedObject6(5, 0)

segments(5) = swSelMgr.GetSelectedObject6(6, 0)

Dim dArray() As DispatchWrapper

dArray = ObjectArrayToDispatchWrapperArray(segments)

stat = memPathSegDef.**SetPathSegments**(dArray)

Debug.Print("Path segments set successfully: " & stat)

memData(0) = structMemDef

memDataArray = memData

modDocExt.**CreateStructureSystem**(memDataArray, Nothing)

modDoc.ViewZoomtofit

Stop

'Inspect corner treatments

featArr = swFeatMgr.**GetCornerManagementFolders**()

Count = UBound(featArr)

For i = 0 To Count

swFeat = featArr(i)

Debug.Print(swFeat.Name)

swCornerMgmtFolder = swFeat.GetSpecificFeature2

swFeat = swCornerMgmtFolder.**GetFeature**

swFeat = swCornerMgmtFolder.**GetStructureSystemFolder**

Debug.Print(swFeat.Name)

swStructSysFolder = swFeat.GetSpecificFeature2

Debug.Print("Number of profile groups: " & swStructSysFolder.**GetProfileGroupFoldersCount**)

grpCnt = swCornerMgmtFolder.**GetTreatmentGroupFolderCount**

Debug.Print("Number of corner treatment groups: " & grpCnt)

grpArr = swCornerMgmtFolder.**GetTreatmentGroupFolders**()

For k = 0 To grpCnt - 1

crnrGrpFolder = grpArr(k)

swFeat = crnrGrpFolder.**GetFeature**

Debug.Print("")

Debug.Print(swFeat.Name)

Debug.Print("Corner group folder type as defined by swCornerType_e: " & crnrGrpFolder.**Type**)

crnrCnt = crnrGrpFolder.**GetCornerTreatmentCount**

Debug.Print("Number of corner treatments: " & crnrCnt)

crnrArr = crnrGrpFolder.**GetCornerTreatments**

For x = 0 To crnrCnt - 1

crnrFeat = crnrArr(x)

Debug.Print(crnrFeat.Name)

crnrFeat2 = crnrFeat.**GetDefinition**

Debug.Print("Corner type as defined by swCornerType_e: " & crnrFeat2.**CornerType**)

Debug.Print("Ignore corner treatment? " & crnrFeat2.**IgnoreCornerTreatment**)

Debug.Print("Allow extension? " & crnrFeat2.**AllowExtension**)

Debug.Print("")

crnrFeat2.**AccessSelections**(modDoc, Nothing)

strCornerName = crnrFeat.Name

If crnrFeat2.CornerType = 0 Then 'Simple corner treatment

Debug.Print("Simple corner treatment")

simpleCrnr = crnrFeat2

Debug.Print("Corner treatment trim type as defined by swCornerTreatmentTrimType_e: " & simpleCrnr.**CornerTreatmentTrimType**)

Debug.Print("Planar trim option as defined by swCornerTreatmentPlanarTrimOptions_e: " & simpleCrnr.**PlanarTrimOption**)

Debug.Print("Planar trim tool type as defined by swCornerTreatmentPlanarTrimToolType_e: " & simpleCrnr.**PlanarTrimToolType**)

Debug.Print("Weld trim gap: " & simpleCrnr.**WeldTrimGap**)

ElseIf crnrFeat2.**CornerType** = 1 Then 'Two member corner treatment

Debug.Print("Two member corner treatment")

twoMbrCrnr = crnrFeat2

Debug.Print("Corner treatment trim type as defined by swCornerTreatmentTrimType_e: " & twoMbrCrnr.**CornerTreatmentTrimType**)

Debug.Print("Planar trim option as defined by swCornerTreatmentPlanarTrimOptions_e: " & twoMbrCrnr.**PlanarTrimOption**)

Debug.Print("Weld trim gap: " & twoMbrCrnr.**WeldTrimGap**)

'Change some settings

twoMbrCrnr.**CornerTreatmentTrimType** = 1 'Body trim

twoMbrCrnr.**WeldTrimGap** = 0.001

crnrMbrArr = twoMbrCrnr.**GetCornerGroupMembers**

Debug.Print("Corner members:")

For Y = 0 To 1

crnrMbr = crnrMbrArr(Y)

Debug.Print("Trim order: " & crnrMbr.**TrimOrder**)

feat1 = crnrMbr.**GetUnderlyingMemberFeature**()

Debug.Print("Member feature: " & feat1.Name)

Next Y

twoMbrCrnr.SwapMembers 'Make other member the trim tool

ElseIf crnrFeat2.**CornerType** = 2 Then 'Complex corner treatment

Debug.Print("Complex corner treatment")

complexCrnr = crnrFeat2

Debug.Print("Planar trim tool type as defined by swCornerTreatmentPlanarTrimToolType_e: " & complexCrnr.**PlanarTrimToolType**)

Debug.Print("Planar trim option as defined by swCornerTreatmentPlanarTrimOptions_e: " & complexCrnr.**PlanarTrimOption**)

varBodyMem = complexCrnr.**GetBodyTrimMembers**

If varBodyMem(0) IsNot Nothing Then

For l = 0 To UBound(varBodyMem)

member = varBodyMem(l)

Debug.Print("Body trim member: " & member.**GetUnderlyingMemberFeature**().Name)

Debug.Print("Body trim order: " & member.**TrimOrder**)

Debug.Print("Body weld gap: " & member.**WeldGap**)

Next l

End If

complexCrnr.**SetTrimToolMember**(varBodyMem(0))

obj = complexCrnr.**GetTrimToolMember**(objType)

If objType = swTrimToolMemberObjectType_e.swTrimToolMemberObjectType_swCornerMember Then

tmember = obj

ElseIf objType = swTrimToolMemberObjectType_e.swTrimToolMemberObjectType_swCornerTreatmentFeature Then

feat = obj

Debug.Print("Trim tool: " & feat.Name)

End If

If Not tmember Is Nothing Then

Debug.Print("Trim tool member: " & tmember.**GetUnderlyingMemberFeature**().Name)

Debug.Print("Trim tool member trim order: " & tmember.**TrimOrder**)

Debug.Print("Trim tool member weld gap: " & tmember.**WeldGap**)

End If

varPlanarMem = complexCrnr.**GetPlanarTrimMembers**

If varPlanarMem IsNot Nothing Then

For m = 0 To UBound(varPlanarMem)

pmember = varPlanarMem(m)

Debug.Print("Planar trim member: " & pmember.**GetUnderlyingMemberFeature**().Name)

Debug.Print("Planar trim member trim order: " & pmember.**TrimOrder**)

Debug.Print("Planar trim member weld gap: " & pmember.**WeldGap**)

Next m

End If

'Below is valid only if PlanarTrimToolType is set to

'swCornerTreatmentPlanarTrimToolType_e.swCornerTreatmentPlanarTrimTool_UserDefined

'faces = complexCrnr.**UserDefinedTrimFaces**

'If Not IsEmpty(faces) Then

'Set face = faces(0)

'Debug.Print "User defined trim face area: " & face.GetArea

'End If

End If

feat = crnrFeat2.**GetFeature**()

status = feat.**ModifyDefinition**(crnrFeat2, modDoc, Nothing)

If status = False Then

crnrFeat2.**ReleaseSelectionAccess**

End If

Next x

Next k

Next i

End Sub

''' <summary>

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public swApp As SldWorks

End Class
