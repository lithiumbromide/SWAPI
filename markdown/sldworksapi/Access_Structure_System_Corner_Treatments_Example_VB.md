---
title: "Access Structure System Corner Treatments Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_Structure_System_Corner_Treatments_Example_VB.htm"
---

# Access Structure System Corner Treatments Example (VBA)

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

Dim swApp As SldWorks.SldWorks

Dim modDoc As SldWorks.ModelDoc2

Dim swFeatMgr As SldWorks.FeatureManager

Dim swSelMgr As SldWorks.SelectionMgr

Dim modDocExt As SldWorks.ModelDocExtension

Dim structMemDef As SldWorks.StructureSystemMemberFeatureData

Dim profDef As SldWorks.StructureSystemMemberProfile

Dim PrimDef As SldWorks.PrimaryStructuralMemberFeatureData

Dim memPathSegDef As PrimaryMemberPathSegmentFeatureData

Dim segments(5) As Object

Dim tsegments(0) As Object

Dim csegments(1) As Object

Dim stat As Boolean

Dim memData(0) As SldWorks.StructureSystemMemberFeatureData

Dim memDataArray As Variant

Dim feat As SldWorks.Feature

Dim i As Long

Dim k As Long

Dim l As Long

Dim m As Long

Dim x As Long

Dim Y As Long

Dim swFeat As SldWorks.Feature

Dim complexCrnr As SldWorks.ComplexCornerTreatmentFeatureData

Dim strCornerName As String

Dim featArr As Variant

Dim Count As Long

Dim swStructSysFolder As SldWorks.StructureSystemFolder

Dim swCornerMgmtFolder As SldWorks.CornerManagementFolder

Dim grpArr As Variant

Dim grpCnt As Long

Dim crnrGrpFolder As SldWorks.CornerTreatmentGroupFolder

Dim crnrArr As Variant

Dim crnrCnt As Long

Dim crnrFeat As SldWorks.Feature

Dim crnrFeat2 As SldWorks.CornerTreatmentFeatureData

Dim simpleCrnr As SldWorks.SimpleCornerTreatmentFeatureData

Dim twoMbrCrnr As SldWorks.TwoMemberCornerTreatmentFeatureData

Dim member As SldWorks.CornerMember

Dim varBodyMem As Variant

Dim obj As Object

Dim objType As Long

Dim tmember As SldWorks.CornerMember

Dim crnrMbrArr As Variant

Dim crnrMbr As SldWorks.CornerMember

Dim feat1 As SldWorks.Feature

Dim status As Boolean

Dim pmember As SldWorks.CornerMember

Dim varPlanarMem As Variant

Option Explicit

Sub main()

Set swApp = Application.SldWorks

Set modDoc = swApp.ActiveDoc

Set modDocExt = modDoc.Extension

Set swSelMgr = modDoc.SelectionManager

Set swFeatMgr = modDoc.FeatureManager

'Create Structure System1

Debug.Print "Create Structure System1"

Debug.Print ""

stat = modDocExt.SelectByID2("Line4@3DSketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line1@Sketch2", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line3@3DSketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line6@3DSketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line3@Sketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

stat = modDocExt.SelectByID2("Line4@Sketch1", "EXTSKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

Set structMemDef = modDocExt.**CreateStructureSystemMemberData**(0)

Debug.Print "Type of structure system member as defined by swStructureSystemMemberType_e: " & structMemDef.**StructureSystemMemberType**

Set profDef = structMemDef.**MemberProfile**

profDef.**ProfileStandard** = "GB"

profDef.**ProfileType** = "round-rods"

profDef.**ProfileSize** = "ROUND BAR 23"

Set PrimDef = structMemDef

Debug.Print "Structure system primary member creation type as defined by swStructureSystemMemberCreationType_e: " & PrimDef.**PrimaryMemberType**

Set memPathSegDef = PrimDef

Set segments(0) = swSelMgr.GetSelectedObject6(1, 0)

Set segments(1) = swSelMgr.GetSelectedObject6(2, 0)

Set segments(2) = swSelMgr.GetSelectedObject6(3, 0)

Set segments(3) = swSelMgr.GetSelectedObject6(4, 0)

Set segments(4) = swSelMgr.GetSelectedObject6(5, 0)

Set segments(5) = swSelMgr.GetSelectedObject6(6, 0)

stat = memPathSegDef.**SetPathSegments**(segments)

Debug.Print "Path segments set successfully: " & stat

Set memData(0) = structMemDef

memDataArray = memData

modDocExt.**CreateStructureSystem** memDataArray, Nothing

modDoc.ViewZoomtofit

Stop

'Inspect corner treatments

featArr = swFeatMgr.**GetCornerManagementFolders**()

Count = UBound(featArr)

For i = 0 To Count

Set swFeat = featArr(i)

Debug.Print swFeat.Name

Set swCornerMgmtFolder = swFeat.GetSpecificFeature2

Set swFeat = swCornerMgmtFolder.**GetFeature**

Set swFeat = swCornerMgmtFolder.**GetStructureSystemFolder**

Debug.Print swFeat.Name

Set swStructSysFolder = swFeat.GetSpecificFeature2

Debug.Print "Number of profile groups: " & swStructSysFolder.**GetProfileGroupFoldersCount**

grpCnt = swCornerMgmtFolder.**GetTreatmentGroupFolderCount**

Debug.Print "Number of corner treatment groups: " & grpCnt

grpArr = swCornerMgmtFolder.**GetTreatmentGroupFolders**()

For k = 0 To grpCnt - 1

Set crnrGrpFolder = grpArr(k)

Set swFeat = crnrGrpFolder.**GetFeature**

Debug.Print ""

Debug.Print swFeat.Name

Debug.Print "Corner group folder type as defined by swCornerType_e: " & crnrGrpFolder.**Type**

crnrCnt = crnrGrpFolder.**GetCornerTreatmentCount**

Debug.Print "Number of corner treatments: " & crnrCnt

crnrArr = crnrGrpFolder.**GetCornerTreatments**

For x = 0 To crnrCnt - 1

Set crnrFeat = crnrArr(x)

Debug.Print crnrFeat.Name

Set crnrFeat2 = crnrFeat.**GetDefinition**

Debug.Print "Corner type as defined by swCornerType_e: " & crnrFeat2.**CornerType**

Debug.Print "Ignore corner treatment? " & crnrFeat2.**IgnoreCornerTreatment**

Debug.Print "Allow extension? " & crnrFeat2.**AllowExtension**

Debug.Print ""

crnrFeat2.**AccessSelections** modDoc, Nothing

strCornerName = crnrFeat.Name

If crnrFeat2.**CornerType** = 0 Then 'Simple corner treatment

Debug.Print "Simple corner treatment"

Set simpleCrnr = crnrFeat2

Debug.Print "Corner treatment trim type as defined by swCornerTreatmentTrimType_e: " & simpleCrnr.**CornerTreatmentTrimType**

Debug.Print "Planar trim option as defined by swCornerTreatmentPlanarTrimOptions_e: " & simpleCrnr.**PlanarTrimOption**

Debug.Print "Planar trim tool type as defined by swCornerTreatmentPlanarTrimToolType_e: " & simpleCrnr.**PlanarTrimToolType**

Debug.Print "Weld trim gap: " & simpleCrnr.**WeldTrimGap**

ElseIf crnrFeat2.**CornerType** = 1 Then 'Two member corner treatment

Debug.Print "Two member corner treatment"

Set twoMbrCrnr = crnrFeat2

Debug.Print "Corner treatment trim type as defined by swCornerTreatmentTrimType_e: " & twoMbrCrnr.**CornerTreatmentTrimType**

Debug.Print "Planar trim option as defined by swCornerTreatmentPlanarTrimOptions_e: " & twoMbrCrnr.**PlanarTrimOption**

Debug.Print "Weld trim gap: " & twoMbrCrnr.**WeldTrimGap**

'Change some settings

twoMbrCrnr.**CornerTreatmentTrimType** = 1 'Body trim

twoMbrCrnr.**WeldTrimGap** = 0.001

crnrMbrArr = twoMbrCrnr.**GetCornerGroupMembers**

Debug.Print "Corner members:"

For Y = 0 To 1

Set crnrMbr = crnrMbrArr(Y)

Debug.Print "Trim order: " & crnrMbr.**TrimOrder**

Set feat1 = crnrMbr.**GetUnderlyingMemberFeature**()

Debug.Print "Member feature: " & feat1.Name

Next Y

twoMbrCrnr.**SwapMembers** 'Make other member the trim tool

ElseIf crnrFeat2.**CornerType** = 2 Then 'Complex corner treatment

Debug.Print "Complex corner treatment"

Set complexCrnr = crnrFeat2

Debug.Print "Planar trim tool type as defined by swCornerTreatmentPlanarTrimToolType_e: " & complexCrnr.**PlanarTrimToolType**

Debug.Print "Planar trim option as defined by swCornerTreatmentPlanarTrimOptions_e: " & complexCrnr.**PlanarTrimOption**

varBodyMem = complexCrnr.**GetBodyTrimMembers**

If Not IsEmpty(varBodyMem) Then

For l = 0 To UBound(varBodyMem)

Set member = varBodyMem(l)

Debug.Print "Body trim member: " & member.**GetUnderlyingMemberFeature**().Name

Debug.Print "Body trim order: " & member.**TrimOrder**

Debug.Print "Body weld gap: " & member.**WeldGap**

Next l

End If

**complexCrnr.SetTrimToolMember** (varBodyMem(0))

Set obj = complexCrnr.**GetTrimToolMember**(objType)

If objType = swTrimToolMemberObjectType_swCornerMember Then

Set tmember = obj

ElseIf objType = swTrimToolMemberObjectType_swCornerTreatmentFeature Then

Set feat = obj

Debug.Print "Trim tool: " & feat.Name

End If

If Not tmember Is Nothing Then

Debug.Print "Trim tool member: " & tmember.**GetUnderlyingMemberFeature**().Name

Debug.Print "Trim tool member trim order: " & tmember.**TrimOrder**

Debug.Print "Trim tool member weld gap: " & tmember.**WeldGap**

End If

varPlanarMem = complexCrnr.**GetPlanarTrimMembers**

If Not IsEmpty(varPlanarMem) Then

For m = 0 To UBound(varPlanarMem)

Set pmember = varPlanarMem(m)

Debug.Print "Planar trim member: " & pmember.**GetUnderlyingMemberFeature**().Name

Debug.Print "Planar trim member trim order: " & pmember.**TrimOrder**

Debug.Print "Planar trim member weld gap: " & pmember.**WeldGap**

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

Set feat = crnrFeat2.**GetFeature**()

status = feat.**ModifyDefinition**(crnrFeat2, modDoc, Nothing)

If status = False Then

crnrFeat2.**ReleaseSelectionAccess**

End If

Next x

Next k

Next i

End Sub
