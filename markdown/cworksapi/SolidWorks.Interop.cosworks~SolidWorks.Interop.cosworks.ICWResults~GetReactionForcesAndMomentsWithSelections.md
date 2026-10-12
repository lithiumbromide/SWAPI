---
title: "GetReactionForcesAndMomentsWithSelections Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetReactionForcesAndMomentsWithSelections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetReactionForcesAndMomentsWithSelections.html"
---

# GetReactionForcesAndMomentsWithSelections Method (ICWResults)

Gets the reaction forces and moments for selections and the entire model at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReactionForcesAndMomentsWithSelections( _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal SelectedObjects As System.Object, _
   ByRef SelectionAndEntireModelReactionForcesAndMoments As System.Object, _
   ByRef EachSelectedObjectReactionForcesAndMoments As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim SelectedObjects As System.Object
Dim SelectionAndEntireModelReactionForcesAndMoments As System.Object
Dim EachSelectedObjectReactionForcesAndMoments As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetReactionForcesAndMomentsWithSelections(NStepNumber, DispPlane, NUnits, SelectedObjects, SelectionAndEntireModelReactionForcesAndMoments, EachSelectedObjectReactionForcesAndMoments, ErrorCode)
```

### C#

```csharp
System.object GetReactionForcesAndMomentsWithSelections(
   System.int NStepNumber,
   System.object DispPlane,
   System.int NUnits,
   System.object SelectedObjects,
   out System.object SelectionAndEntireModelReactionForcesAndMoments,
   out System.object EachSelectedObjectReactionForcesAndMoments,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetReactionForcesAndMomentsWithSelections(
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.int NUnits,
   System.Object^ SelectedObjects,
   [Out] System.Object^ SelectionAndEntireModelReactionForcesAndMoments,
   [Out] System.Object^ EachSelectedObjectReactionForcesAndMoments,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Plane, axis, or coodinate system relative to which to list reaction results
- `NUnits`: Unit as defined in [swsForceUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsForceUnit_e.html)
- `SelectedObjects`: Array of entities for which to get reaction results
- `SelectionAndEntireModelReactionForcesAndMoments`: Array of reaction forces and moments for the selected entities and the entire model (see **Remarks**)
- `EachSelectedObjectReactionForcesAndMoments`: Array of reaction forces and moments for each selected entity (see **Remarks**)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of reaction forces and moments (see **Remarks**)

## VBA Syntax

See [CWResults::GetReactionForcesAndMomentsWithSelections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetReactionForcesAndMomentsWithSelections.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## Remarks

This method is valid only for static, nonlinear, drop test, and dynamic studies.

SelectionAndEntireModelReactionForcesAndMoments array contains 16 elements:

{

`summation_xcoord_forces_all_selections,`

`summation_ycoord_forces_all_selections,`

`summation_zcoord_forces_all_selections,`

`resultant_force_all_selections`,

`summation_xcoord_moments_all_selections,`

`summation_ycoord_moments_all_selections,`

`summation_zcoord_moments_all_selections,`

`resultant_moment_all_selections`,

`summation_xcoord_forces_entire_model,`

`summation_ycoord_forces_entire_model,`

`summation_zcoord_forces_entire_model,`

`resultant_force_entire_model`,

`summation_xcoord_moments_entire_model,`

`summation_ycoord_moments_entire_model,`

`summation_zcoord_moments_entire_model,`

`resultant_moment_entire_model`

`}`

EachSelectedObjectReactionForcesAndMoments array contains (8 X `no_of_selections`) elements:

{

`selection_1_xcoord_reaction_force,`

`selection_1_ycoord_reaction_force,`

`selection_1_zcoord_reaction_force,`

`selection_1_resultant_reaction_force`,

`selection_1_xcoord_reaction_moment,`

`selection_1_ycoord_reaction_moment,`

`selection_1_zcoord_reaction_moment,`

`selection_1_resultant_reaction_moment,`

`...`

`selection_n_xcoord_reaction_force,`

`selection_n_ycoord_reaction_force,`

`selection_n_zcoord_reaction_force,`

`selection_n_resultant_reaction_force`,

`selection_n_xcoord_reaction_moment,`

`selection_n_ycoord_reaction_moment,`

`selection_n_zcoord_reaction_moment,`

`selection_n_resultant_reaction_moment`

`}`

This method returns the reaction forces and moments at each node of the entire model:

{

`node_1`,

`node_1_xcoord_reaction_force,`

`node_1_ycoord_reaction_force,`

`node_1_zcoord_reaction_force,`

`node_1_resultant_reaction_force`,

`node_1_xcoord_reaction_moment,`

`node_1_ycoord_reaction_moment,`

`node_1_zcoord_reaction_moment,`

`node_1_resultant_reaction_moment`,

...

`node_n`,

`node_n_xcoord_reaction_force,`

`node_n_ycoord_reaction_force,`

`node_n_zcoord_reaction_force,`

`node_n_resultant_reaction_force`,

`node_n_xcoord_reaction_moment,`

`node_n_ycoord_reaction_moment,`

`node_n_zcoord_reaction_moment,`

`node_n_resultant_reaction_moment`

}

In all of the arrays, the nodes are integers, and the reaction forces and moments are in decimal or scientific notation.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDisplacementComponentForAllStepsAtNode Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementComponentForAllStepsAtNode.html)
[ICWResults::GetDisplacementForEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementForEntities.html)
[ICWResults::GetMinMaxDisplacement Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacement.html)
[ICWResults::GetRotationalDisplacement Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetRotationalDisplacement.html)
[ICWResults::GetTranslationalDisplacement Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetTranslationalDisplacement.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
