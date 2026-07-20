---
title: "Create ConvertSolid Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_ConvertSolid_Feature_Example_VBNET.htm"
---

# Create ConvertSolid Feature Example (VB.NET)

This example shows how to convert a solid body to sheet metal.

'------------------------------------------------------------------

'Preconditions:

' 1. Open public_documents \SOLIDWORKS\SOLIDWORKS
2025\samples\tutorial\api\sweepcutextrude.sldprt .

' 2. Ensure that the Sheet Metal tab is visible on
the Command Manager toolbar.

' 3. Open an Immediate window.

'

'Postconditions:

' 1. Creates Convert-Solid1 and Sheet-Metal1 .

' 2. Inspect the FeatureManager design tree and the
Immediate window.

'

' NOTE: Because the model may be used elsewhere, do
not save changes to it.

'-------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System.Runtime.InteropServices

Imports System

Partial Class SolidWorksMacro

Sub main()

Dim swModel As ModelDoc2

Dim swFeat As Feature

Dim FeatMgr As FeatureManager

Dim swConvertSolidFeatData As ConvertSolidFeatureData

Dim FeatData As ConvertSolidFeatureData

Dim boolstatus As Boolean

Dim cba As CustomBendAllowance

Dim face As Face2

Dim faceId As Object

Dim bendEdges As Object

swModel = swApp. ActiveDoc

FeatMgr = swModel. FeatureManager

boolstatus = swModel.Extension. SelectByID2 ("",
"FACE", 0.0004130570195002, 0.02357994168921, 0.02568415695742, True, 0,
Nothing, 0)

boolstatus = swModel.Extension. SelectByID2 ("",
"EDGE", -0.00190522473838, 0.02387533864419, 0.04979931166838, True, 1,
Nothing, 0)

boolstatus = swModel.Extension. SelectByID2 ("",
"EDGE", 0.02911271681069, 0.02376277320678, 0.02892436699148, True, 1,
Nothing, 0)

boolstatus = swModel.Extension. SelectByID2 ("",
"EDGE", -0.004838857104858, 0.02387396382323, -0.0001997542986487, True, 1,
Nothing, 0)

'Create a feature data object

swConvertSolidFeatData = FeatMgr. CreateDefinition (swFeatureNameID_e.swFmSolidToSheetMetal)

cba = swConvertSolidFeatData. GetCustomBendAllowance ()

cba. Type =
swBendAllowanceTypes_e.swBendAllowanceKFactor

cba. KFactor = 0.08

'Initialize the feature data object with
custom bend allowance

swConvertSolidFeatData. Initialize (True, False, cba)

'Create the feature

swFeat = FeatMgr. CreateFeature (swConvertSolidFeatData)

FeatData = swFeat. GetDefinition ()

cba = swConvertSolidFeatData. GetCustomBendAllowance ()

Debug.Print("Type of custom bend allowance as defined in
swBendAllowanceTypes_e: " & cba. Type )

Debug.Print("K factor: " & cba. KFactor )

Debug.Print("SheetMetal thickness : " & FeatData. SheetThickness )

Debug.Print("Bend Radius : " & FeatData. BendRadius )

Debug.Print("Reverse thickness : " & FeatData. ReverseThickness )

Debug.Print("Keep body : " & FeatData. KeepBody )

Debug.Print("Overlap type : " & FeatData. CornerDefaults )

Debug.Print("Rip gaps : " & FeatData. RipGap )

Debug.Print("Rip overlap ratio : " & FeatData. RipOverlapRatio )

Debug.Print("Auto relief type : " & FeatData. ReliefType )

Debug.Print("Auto relief ratio : " & FeatData. ReliefRatio )

bendEdges = FeatData. BendEdges

Debug.Print("Number of bend edges: " & FeatData. GetBendEdgesCount )

FeatData. AccessSelections (swModel, Nothing)

face = FeatData. GetFixedFace

faceId = face. GetFaceId ()

Debug.Print("Fixed face ID: " & faceId)

'Modify initial values

FeatData. SheetThickness = 0.014

FeatData. BendRadius = 0.0006

'Modify the feature definition

swFeat. ModifyDefinition (FeatData,
swModel, Nothing)

Debug.Print("----------------------------After Setting
Values-------------------------------")

Debug.Print("SheetMetal thickness : " & FeatData. SheetThickness )

Debug.Print("Bend Radius : " & FeatData. BendRadius )

Debug.Print("Reverse thickness : " & FeatData. ReverseThickness )

Debug.Print("Keep body : " & FeatData. KeepBody )

Debug.Print("Overlap type : " & FeatData. CornerDefaults )

Debug.Print("Rip gaps : " & FeatData. RipGap )

Debug.Print("Rip overlap ratio : " & FeatData. RipOverlapRatio )

Debug.Print("Auto relief type : " & FeatData. ReliefType )

Debug.Print("Auto relief ratio : " & FeatData. ReliefRatio )

End Sub

'''
<summary>

''' The SldWorks swApp variable is
pre-assigned for you.

''' </summary>

Public swApp As SldWorks

End Class
