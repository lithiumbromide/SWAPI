---
title: "Get Type of Instant3D Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Type_of_Instant3D_Feature_Example_CSharp.htm"
---

# Get Type of Instant3D Feature Example (C#)

This example shows how to get the types and persistent IDs of underlying features of Instant3D features.

//-----------------------------------------------------
// Preconditions:
// 1. Verify that the specified part exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part and traverses the FeatureManager
// design tree.
// 2. Gets the types of features, including the types
// of underlying features and persistent IDs
// of Instant3D features.
// 3. Examine the Immediate window.
//-----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace Instant3DFeatureCSharp.csproj
{

partial class SolidWorksMacro
{

public void Main()
{
ModelDoc2 swModel = default(ModelDoc2);
Feature swFeature = default(Feature);
string fileName = null;
int errors = 0;
int warnings = 0;

fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block.sldprt";
swModel = (ModelDoc2)swApp.**OpenDoc6**(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

swFeature = (Feature)swModel.**FirstFeature**();

SelectFeat(swFeature);

}

public bool SelectFeat(Feature featureTemp)
{
while ((featureTemp != null))
{
string featureName = null;
featureName = featureTemp.**GetTypeName2**();

Debug.Print(featureName);

// Instant3D features are ICE features
if (featureName == "ICE")
{
Debug.Print(" Type: " + featureTemp.**GetTypeName**());
Debug.Print(" ID: " + featureTemp.**GetID**());
}

featureTemp = (Feature)featureTemp.**GetNextFeature**();
}
return true;
}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>

public SldWorks swApp;

}
}
