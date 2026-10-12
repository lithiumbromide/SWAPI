---
title: "GetMinMaxStressForHarmonic2 Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxStressForHarmonic2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStressForHarmonic2.html"
---

# GetMinMaxStressForHarmonic2 Method (ICWResults)

Gets the algebraic minimum and maximum for the specified stress component and solution step of this harmonic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxStressForHarmonic2( _
   ByVal NComponent As System.Integer, _
   ByVal BByElementNumber As System.Boolean, _
   ByVal BAvgOnBoundary As System.Boolean, _
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
Dim BByElementNumber As System.Boolean
Dim BAvgOnBoundary As System.Boolean
Dim NStepNum As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxStressForHarmonic2(NComponent, BByElementNumber, BAvgOnBoundary, NStepNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxStressForHarmonic2(
   System.int NComponent,
   System.bool BByElementNumber,
   System.bool BAvgOnBoundary,
   System.int NStepNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxStressForHarmonic2(
   System.int NComponent,
   System.bool BByElementNumber,
   System.bool BAvgOnBoundary,
   System.int NStepNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Stress component as defined in [swsStressComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStressComponent_e.html)
- `BByElementNumber`: -1 or true to obtain element stress values, 0 or false to obtain nodal stress values
- `BAvgOnBoundary`: -1 or true to activate averaging of nodal stress results across common part boundaries, 0 or false to deactivate averaging; valid only if BByElementNumber = 0
- `NStepNum`: Solution step number (use 1 for static)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if reference geometry does not exist
- `NUnits`: Units as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array (see **Remarks**)

## Remarks

This method returns the following array:

{`node/element_with_minimum_stress`, `minimum_stress`, `node/element_with_maximum_stress`, `maximum_stress`},

where the nodes or elements are integer indexes, and the stresses are in scientific notation.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
