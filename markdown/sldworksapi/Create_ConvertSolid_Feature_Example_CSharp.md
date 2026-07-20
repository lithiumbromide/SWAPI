---
title: "Create ConvertSolid Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_ConvertSolid_Feature_Example_CSharp.htm"
---

# Create ConvertSolid Feature Example (C#)

This example shows how to convert a solid body to sheet metal.

//
------------------------------------------------------------------

// Preconditions:

// 1. Open public_documents \SOLIDWORKS\SOLIDWORKS
2025\samples\tutorial\api\sweepcutextrude.sldprt.

// 2. Ensure that the Sheet Metal tab is visible on the Command
Manager toolbar.

// 3. On the SOLIDWORKS toolbar, click Tools > Macro > New and create a C# macro.

// 4. Copy and paste the code below into SolidWorksMacro.cs .

// 5. Open an Immediate window.

//

// Postconditions:

// 1. Creates Convert-Solid1 and Sheet-Metal1.

// 2. Inspect the FeatureManager design tree and the Immediate
window.

//

// NOTE: Because the model may be used elsewhere, do not save
changes to it.

// -------------------------------------------------------------

using System;

using System.Collections.Generic;

using System.Diagnostics;

using System.Globalization;

using System.IO;

using System.Linq;

using System.Reflection;

using System.Runtime.CompilerServices;

using System.Security;

using System.Text;

using System.Threading.Tasks;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System.Runtime.InteropServices;

namespace ConvertToSheetMetal_CSharp

{

partial
class SolidWorksMacro

{

public void Main()

{

ModelDoc2 swModel;

Feature swFeat;

FeatureManager FeatMgr;

ConvertSolidFeatureData swConvertSolidFeatData;

ConvertSolidFeatureData FeatData;

bool boolstatus;

CustomBendAllowance cba;

Face2 face;

object faceId;

object bendEdges;

swModel = (ModelDoc2)swApp. ActiveDoc ;

FeatMgr = swModel. FeatureManager ;

boolstatus = swModel.Extension. SelectByID2 ("", "FACE",
0.0004130570195002, 0.02357994168921, 0.02568415695742, true, 0, null, 0);

boolstatus = swModel.Extension. SelectByID2 ("", "EDGE", -0.00190522473838,
0.02387533864419, 0.04979931166838, true, 1, null, 0);

boolstatus = swModel.Extension. SelectByID2 ("", "EDGE", 0.02911271681069,
0.02376277320678, 0.02892436699148, true, 1, null, 0);

boolstatus = swModel.Extension. SelectByID2 ("", "EDGE",
-0.004838857104858, 0.02387396382323, -0.0001997542986487, true, 1, null, 0);

// Create a feature data object

swConvertSolidFeatData =
(ConvertSolidFeatureData)FeatMgr. CreateDefinition ((int)swFeatureNameID_e.swFmSolidToSheetMetal);

cba =
(CustomBendAllowance)swConvertSolidFeatData. GetCustomBendAllowance ();

cba. Type = (int)swBendAllowanceTypes_e.swBendAllowanceKFactor;

cba. KFactor = 0.08;

// Initialize the feature data object with custom bend allowance

swConvertSolidFeatData. Initialize (true, false, cba);

// Create the feature

swFeat = FeatMgr. CreateFeature (swConvertSolidFeatData);

FeatData = (ConvertSolidFeatureData)swFeat. GetDefinition ();

cba =
(CustomBendAllowance)swConvertSolidFeatData. GetCustomBendAllowance ();

Debug.Print("Type of custom bend allowance as defined in
swBendAllowanceTypes_e: " + cba. Type );

Debug.Print("K factor: " + cba. KFactor );

Debug.Print("SheetMetal thickness : " + FeatData. SheetThickness );

Debug.Print("Bend Radius : "
+ FeatData. BendRadius );

Debug.Print("Reverse thickness : " + FeatData. ReverseThickness );

Debug.Print("Keep body : " + FeatData. KeepBody );

Debug.Print("Overlap type : " + FeatData. CornerDefaults );

Debug.Print("Rip gaps : " + FeatData. RipGap );

Debug.Print("Rip overlap ratio : " + FeatData. RipOverlapRatio );

Debug.Print("Auto relief type : " + FeatData. ReliefType );

Debug.Print("Auto relief ratio : " + FeatData. ReliefRatio );

bendEdges = FeatData. BendEdges ;

Debug.Print("Number of bend edges: " + FeatData. GetBendEdgesCount ());

FeatData. AccessSelections (swModel, null);

face = (Face2)FeatData. GetFixedFace ();

faceId = face. GetFaceId ();

Debug.Print("Fixed face ID: " + faceId);

// Modify initial values

FeatData. SheetThickness = 0.014;

FeatData. BendRadius = 0.0006;

// Modify the feature definition

swFeat. ModifyDefinition (FeatData, swModel, null);

Debug.Print("----------------------------After Setting
Values-------------------------------");

Debug.Print("SheetMetal thickness : " + FeatData. SheetThickness );

Debug.Print("Bend Radius : "
+ FeatData. BendRadius );

Debug.Print("Reverse thickness : " + FeatData. ReverseThickness );

Debug.Print("Keep body : " + FeatData. KeepBody );

Debug.Print("Overlap type : " + FeatData. CornerDefaults );

Debug.Print("Rip gaps : " + FeatData. RipGap );

Debug.Print("Rip overlap ratio : " + FeatData. RipOverlapRatio );

Debug.Print("Auto relief type : " + FeatData. ReliefType );

Debug.Print("Auto relief ratio : " + FeatData. ReliefRatio );

}

public SldWorks swApp;

}

}
