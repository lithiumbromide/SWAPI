---
title: "GetMinMaxDisplacementForHarmonic Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxDisplacementForHarmonic"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacementForHarmonic.html"
---

# GetMinMaxDisplacementForHarmonic Method (ICWResults)

Gets the algebraic minimum and maximum displacement for the specified component and solution step of this harmonic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxDisplacementForHarmonic( _
   ByVal NComponent As System.Integer, _
   ByVal NStepNum As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NStepNum As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxDisplacementForHarmonic(NComponent, NStepNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxDisplacementForHarmonic(
   System.int NComponent,
   System.int NStepNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxDisplacementForHarmonic(
   System.int NComponent,
   System.int NStepNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Displacement component as defined in [swsDisplacementComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDisplacementComponent_e.html)
- `NStepNum`: Solution step number (use 1 for static)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if reference geometry does not exist
- `NUnits`: Linear units for displacement translation as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetMinMaxDisplacementForHarmonic](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxDisplacementForHarmonic.html).

## Remarks

This method returns the following array:

{`node_with_minimum_displacement`, `minimum_displacement`, `node_with_maximum_displacement`, `maximum_displacement`},

where the nodes are integer indexes, and the displacements are in scientific notation.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxDisplacement Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacement.html)
[ICWResults::GetMinMaxDisplacementRMS Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacementRMS.html)

## Availability

SOLIDWORKS Simulation API 2015 SP1.0
