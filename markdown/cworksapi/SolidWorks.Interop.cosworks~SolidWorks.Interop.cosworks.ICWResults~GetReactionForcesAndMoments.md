---
title: "GetReactionForcesAndMoments Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetReactionForcesAndMoments"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetReactionForcesAndMoments.html"
---

# GetReactionForcesAndMoments Method (ICWResults)

Obsolete. Superseded by [ICWResults::GetReactionForcesAndMomentsWithSelections](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetReactionForcesAndMomentsWithSelections.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReactionForcesAndMoments( _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetReactionForcesAndMoments(NStepNumber, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetReactionForcesAndMoments(
   System.int NStepNumber,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetReactionForcesAndMoments(
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Reference geometry
- `NUnits`: Unit as defined in [swsForceUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsForceUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of reaction forces and moments for the entire model (see **Remarks**)

## VBA Syntax

See [CWResults::GetReactionForcesAndMoments](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetReactionForcesAndMoments.html).

## Remarks

This method is valid only for static, nonlinear, drop test, and dynamic studies.

This method returns the reaction forces and moments at each node of the entire model:

{

`node_1`,

`node_1_xcoord_reaction_force,`

`node_1_ycoord_reaction_force,`

`node_1_zcoord_reaction_force,`

`node_1_resultant_reaction_force,`

`node_1_xcoord_reaction_moment,`

`node_1_ycoord_reaction_moment,`

`node_1_zcoord_reaction_moment,`

`node_1_resultant_reaction_moment,`

`...`

`node_n,`

`node_n_xcoord_reaction_force,`

`node_n_ycoord_reaction_force,`

`node_n_zcoord_reaction_force,`

`node_n_resultant_reaction_force,`

`node_n_xcoord_reaction_moment,`

`node_n_ycoord_reaction_moment,`

`node_n_zcoord_reaction_moment,`

`node_n_resultant_reaction_moment`

},

where the nodes are integers, and the reaction forces and moments are in decimal or scientific notation.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDisplacementComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementComponentForAllStepsAtNode.html)
[ICWResults::GetDisplacementForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementForEntities.html)
[ICWResults::GetMinMaxDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacement.html)
[ICWResults::GetRotationalDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetRotationalDisplacement.html)
[ICWResults::GetTranslationalDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetTranslationalDisplacement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
