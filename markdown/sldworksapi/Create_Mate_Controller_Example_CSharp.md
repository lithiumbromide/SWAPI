---
title: "Create a Mate Controller Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Mate_Controller_Example_CSharp.htm"
---

# Create a Mate Controller Example (C#)

This example shows how to create a Mate Controller in an assembly.

// ======================================================================================

// Preconditions: Open an assembly document that contains a mechanical slot feature

// with a slot mate that has one of these constraints:

// - Distance Along Slot

// - Percent Along Slot

//

// Postconditions:

// 1. Mate Controller (Position 3) is added to the FeatureManager design tree.

// 2. Inspect the graphics area.

//

// =====================================================================================

using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

using System.Windows;

using System.Windows.Forms;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System.Runtime.InteropServices;

namespace SlotMate_CSharp

{

public partial class SolidWorksMacro

{

private ModelDoc2 Part;

private AssemblyDoc Assem;

private FeatureManager featMgr;

private bool boolstatus;

private object myModelView;

private object[] var;

private MateControllerFeatureData mateControllerObj;

private MateControllerFeatureData mcObj2;

private Feature mateContFeat;

private double[] position2ValArr = new double[1];

private double[] position3ValArr = new double[1];

private object var1;

private double[] position2ValArr2 = new double[1];

private double[] position3ValArr2 = new double[1];

public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)

{

int ArraySize;

ArraySize = Objects.GetUpperBound(0);

DispatchWrapper[] d = new DispatchWrapper[ArraySize + 1];

int ArrayIndex;

for (ArrayIndex = 0; ArrayIndex <= ArraySize; ArrayIndex++)

d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);

return d;

}

public void Main()

{

Part = (ModelDoc2)swApp.ActiveDoc;

Assem = (AssemblyDoc)Part;

myModelView = Part.ActiveView;

Part.ClearSelection2(true);

boolstatus = Assem.**IsSupportedMatesAvailable**;

var = (object[])Assem.**CollectAllSupportiveMates**();

featMgr = Part.FeatureManager;

mateControllerObj = (MateControllerFeatureData)featMgr.**CreateDefinition**((int)swFeatureNameID_e.swFmMateController);

DispatchWrapper[] dArray;

dArray = ObjectArrayToDispatchWrapperArray(var);

mateControllerObj.**Initialize**(dArray);

mateControllerObj.**AddNewPosition**("Position1");

mateControllerObj.**AddNewPosition**("Position2");

mateControllerObj.**AddNewPosition**("Position3");

position2ValArr[0] = 0.0375;

mateControllerObj.**SetValues**("Position2", position2ValArr);

position3ValArr[0] = 0.0625;

mateControllerObj.**SetValues**("Position3", position3ValArr);

mateContFeat = featMgr.**CreateFeature**(mateControllerObj);

mcObj2 = (MateControllerFeatureData)mateContFeat.**GetDefinition**();

var1 = mcObj2.**Mates**;

position2ValArr2[0] = 0.015;

mcObj2.**SetValues**("Position2", position2ValArr2);

position3ValArr2[0] = 0.085;

mcObj2.**SetValues**("Position3", position3ValArr2);

mateContFeat.**ModifyDefinition**(mcObj2, Part, null);

}

// The SldWorks swApp variable is pre-assigned for you.

public SldWorks swApp;

}

}
