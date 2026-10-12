---
title: "Change Pitch of Helix Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Pitch_of_Helix_Example_CSharp.htm"
---

# Change Pitch of Helix Example (C#)

This example shows how to change the pitch of a helix.

//-------------------------------------------------------
// Preconditions:
// 1. Open a part containing a helix feature.
// 2. Select the helix feature.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Modifies the pitch of selected helix feature.
// 2. Gets the name of helix feature, original pitch, and
// modified pitch values.
// 3. Examine the Immediate window and graphics area.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace PitchHelixFeatureDataCSharp.csproj
{

partial class SolidWorksMacro
{

public void Main()
{

ModelDoc2 swModel = default(ModelDoc2);
SelectionMgr swSelMgr = default(SelectionMgr);
Feature swFeat = default(Feature);
HelixFeatureData swHelix = default(HelixFeatureData);
bool bRet = false;

swModel = (ModelDoc2)swApp.**ActiveDoc**;
swSelMgr = (SelectionMgr)swModel.**SelectionManager**;
swFeat = (Feature)swSelMgr.**GetSelectedObject6**(1, -1);
swHelix = (HelixFeatureData)swFeat.**GetDefinition**();

Debug.Print("Feature = " + swFeat.**Name**);
Debug.Print(" Original pitch = " + swHelix.**Pitch** * 1000.0 + " mm");

// Change the pitch value
swHelix.Pitch = 1.25 * swHelix.**Pitch**;
Debug.Print(" Modified pitch = " + swHelix.**Pitch** * 1000.0 + " mm");

// Apply the change
bRet = swFeat.**ModifyDefinition**(swHelix, swModel, null);

Debug.Assert(bRet);
}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>
public SldWorks swApp;

}
}
