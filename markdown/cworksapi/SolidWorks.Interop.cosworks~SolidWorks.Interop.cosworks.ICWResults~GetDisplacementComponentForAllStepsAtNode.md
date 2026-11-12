---
title: "GetDisplacementComponentForAllStepsAtNode Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetDisplacementComponentForAllStepsAtNode"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementComponentForAllStepsAtNode.html"
---

# GetDisplacementComponentForAllStepsAtNode Method (ICWResults)

Gets the specified displacement component at the specified node for all solutions steps.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplacementComponentForAllStepsAtNode( _
   ByVal NComponent As System.Integer, _
   ByVal NNodeNum As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NNodeNum As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetDisplacementComponentForAllStepsAtNode(NComponent, NNodeNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetDisplacementComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetDisplacementComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Displacement component as defined in [swsDisplacementComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDisplacementComponent_e.html)
- `NNodeNum`: Node number
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `NUnits`: Linear units as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of displacement component values

## VBA Syntax

See [CWResults::GetDisplacementComponentForAllStepsAtNode](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetDisplacementComponentForAllStepsAtNode.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDisplacementForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementForEntities.html)
[ICWResults::GetMinMaxDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacement.html)
[ICWResults::GetTranslationalDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetTranslationalDisplacement.html)
[ICWResults::GetReactionForcesAndMoments Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetReactionForcesAndMoments.html)
[ICWResults::GetRotationalDisplacement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetRotationalDisplacement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
