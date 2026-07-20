---
title: "Create Forming Tool Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Forming_Tool_Feature_Example_VBNET.htm"
---

# Create Forming Tool Feature Example (VB.NET)

This example shows how to create a forming tool feature.

'----------------------------------------------------------------------------

' Preconditions:

' 1. Open public_documents \SOLIDWORKS\SOLIDWORKS
2025\samples\tutorial\sheetmetal\formtools\cover.sldprt.

'2. On the SOLIDWORKS toolbar, click Tools > Macro > New and create a VB.NET macro.

'3. Copy and paste the code below into SolidWorksMacro.vb .

' 4. Modify the two formtoolpath locations.

' 5. Run the macro.

' 6. At the pause, inspect the FeatureManager design
tree and the graphics area for the drafted rectangular emboss forming tool.

' Then select a flat face where to re-position (and
replace) the forming tool.

' 7. Press F5 finish.

'

' Postconditions:

' 1. A dimple emboss replaces the drafted rectangular
emboss.

' 2. Inspect the FeatureManager design tree, graphics
area, and the Immediate window.

'

' NOTE: Do not save the part as it may be used
elsewhere.

'
---------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System.Runtime.InteropServices

Imports System

Partial Class SolidWorksMacro

Dim
swModel As ModelDoc2

Dim
featMgr As FeatureManager

Dim
boolstatus As Boolean

Sub main()

swModel = swApp.ActiveDoc

'Select
a flat face where to insert an emboss forming tool

boolstatus = swModel.Extension. SelectByRay (0.0553557395141979,
0.0303381093343091, 0.0266948404126879, -0.707061513640545,
-0.415946801562901, -0.57188484347632, 0.000532844353755021, 2, False, 0, 0)

featMgr = swModel. FeatureManager

Dim LibFormToolFeatureData As LibraryFormToolFeatureData

LibFormToolFeatureData = featMgr. CreateDefinition (swFeatureNameID_e.swFmFormToolInstance)

LibFormToolFeatureData. LinkToFormTool = True

LibFormToolFeatureData. FormToolPath =
"E:\images\2025_SP02_release64\d250219.026.F63\WinRel64\WinRel64\data\Design
Library\forming tools\embosses\drafted rectangular emboss.sldftp"

Call LibFormToolFeatureData. OverrideDocumentSettings (True,
True, True, True)

LibFormToolFeatureData. RotationAngle = 0.5

Dim swFeat As Feature

swFeat = featMgr. CreateFeature (LibFormToolFeatureData)

Stop' Inspect the graphics area and FeatureManager design tree; select a flat
face where to re-position (and replace) the forming tool

Dim selMgr As SelectionMgr

selMgr = swModel. SelectionManager

Dim face2 As Face2

face2 = selMgr. GetSelectedObject6 (1, -1)

Dim pickPt As Object

pickPt = selMgr. GetSelectionPoint2 (1, -1)

Dim MU As MathUtility

MU = swApp. GetMathUtility ()

Dim mathPt As MathPoint

mathPt = MU. CreatePoint (pickPt)

swModel. ClearSelection2 (True)

Dim swLibFormFeatData1 As LibraryFormToolFeatureData

swLibFormFeatData1 = swFeat. GetDefinition ()

Debug.Print(swLibFormFeatData1. GetPunchID ())

Debug.Print(swLibFormFeatData1. FormToolConfiguration )

Debug.Print(swLibFormFeatData1. FormToolPath )

Debug.Print(swLibFormFeatData1. LinkToFormTool )

Debug.Print(swLibFormFeatData1. RotationAngle )

Debug.Print(swLibFormFeatData1. AccessSelections (swModel,
Nothing))

Dim face As Face2

face = swLibFormFeatData1. PlacementFace

swLibFormFeatData1. RotationAngle = 0.7833

Call swLibFormFeatData1. OverrideDocumentSettings (True,
True, True, True)

swLibFormFeatData1. FormToolConfiguration = "Default"

swLibFormFeatData1. FormToolPath =
"E:\images\2025_SP02_release64\d250219.026.F63\WinRel64\WinRel64\data\Design
Library\forming tools\embosses\dimple.SLDFTP"

swLibFormFeatData1. LinkToFormTool = True

Dim ent As Entity

ent = face

Call ent. Select4 (True, Nothing)

Call swLibFormFeatData1. SetPlacementFace (face2,
mathPt)

Debug.Print(swFeat. ModifyDefinition (swLibFormFeatData1,
swModel, Nothing))

Dim face1 As Face2

face1 = swLibFormFeatData1. PlacementFace

End Sub

'''
<summary>

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public
swApp As SldWorks

End Class
