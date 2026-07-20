---
title: "Create Forming Tool Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Forming_Tool_Feature_Example_CSharp.htm"
---

# Create Forming Tool Feature Example (C#)

This example shows how to create a forming tool feature.

//
----------------------------------------------------------------------------

// Preconditions:

// 1. Open`public_documents`**\SOLIDWORKS\SOLIDWORKS
2025\samples\tutorial\sheetmetal\formtools\cover.sldprt**.

// 2. On the SOLIDWORKS toolbar, click Tools > Macro > New and create a C# macro.

// 3. Copy and paste the code below into SolidWorksMacro.cs .

// 4. Modify the two formtoolpath locations.

// 5. Run the macro.

// 6. At the pause, inspect the FeatureManager design
tree and the graphics area for the drafted rectangular emboss forming tool.

// Then select a flat face where to re-position (and
replace) the forming tool.

// 7. Press F5 finish.

//

// Postconditions:

// 1. A dimple emboss replaces the drafted rectangular
emboss.

// 2. Inspect the FeatureManager design tree, graphics
area, and the Immediate window.

//

// NOTE: Do not save the part as it may be used
elsewhere.

//
---------------------------------------------------------------------------

using System;

using System.Collections.Generic;

using System.Diagnostics;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

using System.Windows;

using System.Windows.Forms;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

namespace CreateFormingTool_CSharp

{

public
partial class SolidWorksMacro

{

private ModelDoc2 swModel;

private FeatureManager featMgr;

private bool boolstatus;

public void Main()

{

swModel = (ModelDoc2)swApp. ActiveDoc ;

// Select a flat face where to insert an emboss forming tool

boolstatus = swModel.Extension. SelectByRay (0.0553557395141979,
0.0303381093343091, 0.0266948404126879, -0.707061513640545, -0.415946801562901,
-0.57188484347632, 0.000532844353755021, 2, false, 0, 0);

featMgr = swModel.FeatureManager;

LibraryFormToolFeatureData LibFormToolFeatureData;

LibFormToolFeatureData = (LibraryFormToolFeatureData)featMgr. CreateDefinition ((int)swFeatureNameID_e.swFmFormToolInstance);

LibFormToolFeatureData. LinkToFormTool = true;

LibFormToolFeatureData. FormToolPath =
@"E:\images\2025_SP02_release64\d250219.026.F63\WinRel64\WinRel64\data\Design
Library\forming tools\embosses\drafted rectangular emboss.sldftp";

LibFormToolFeatureData. OverrideDocumentSettings (true,
true, true, true);

LibFormToolFeatureData. RotationAngle = 0.5;

Feature swFeat;

swFeat = featMgr. CreateFeature (LibFormToolFeatureData);

System.Diagnostics.Debugger.Break();// Inspect the graphics area and FeatureManager design tree; select a flat face
where to re-position (and replace) the forming tool

SelectionMgr selMgr;

selMgr = (SelectionMgr)swModel. SelectionManager ;

Face2 face2;

face2 = (Face2)selMgr. GetSelectedObject6 (1, -1);

object pickPt;

pickPt = selMgr. GetSelectionPoint2 (1, -1);

MathUtility MU;

MU = (MathUtility)swApp. GetMathUtility ();

MathPoint mathPt;

mathPt = (MathPoint)MU. CreatePoint (pickPt);

swModel. ClearSelection2 (true);

LibraryFormToolFeatureData swLibFormFeatData1;

swLibFormFeatData1 = (LibraryFormToolFeatureData)swFeat. GetDefinition ();

Debug.Print("Forming tool punch ID: " + swLibFormFeatData1. GetPunchID ());

Debug.Print("Forming tool part configuration: " + swLibFormFeatData1. FormToolConfiguration );

Debug.Print("Forming tool path: " + swLibFormFeatData1. FormToolPath );

Debug.Print("Link to Design Library part? " + swLibFormFeatData1. LinkToFormTool );

Debug.Print("Rotation angle: " + swLibFormFeatData1. RotationAngle );

swLibFormFeatData1. AccessSelections (swModel, null);

Face2 face;

face = (Face2)swLibFormFeatData1. PlacementFace ;

swLibFormFeatData1. RotationAngle = 0.7833;

swLibFormFeatData1. OverrideDocumentSettings (true, true,
true, true);

swLibFormFeatData1. FormToolConfiguration = "Default";

swLibFormFeatData1. FormToolPath =
@"E:\images\2025_SP02_release64\d250219.026.F63\WinRel64\WinRel64\data\Design
Library\forming tools\embosses\dimple.SLDFTP";

swLibFormFeatData1. LinkToFormTool = true;

Entity ent;

ent = (Entity)face;

ent. Select4 (true, null);

swLibFormFeatData1. SetPlacementFace (face2, mathPt);

swFeat. ModifyDefinition (swLibFormFeatData1, swModel,
null);

Face2 face1;

face1 = (Face2)swLibFormFeatData1. PlacementFace ;

}

// The SldWorks swApp variable is pre-assigned for you.

public SldWorks swApp;

}

}
