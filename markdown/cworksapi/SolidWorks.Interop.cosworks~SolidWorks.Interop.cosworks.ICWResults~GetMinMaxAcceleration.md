---
title: "GetMinMaxAcceleration Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxAcceleration"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxAcceleration.html"
---

# GetMinMaxAcceleration Method (ICWResults)

Gets the algebraic minimum and maximum for the specified acceleration component and solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxAcceleration( _
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

value = instance.GetMinMaxAcceleration(NComponent, NStepNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxAcceleration(
   System.int NComponent,
   System.int NStepNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxAcceleration(
   System.int NComponent,
   System.int NStepNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Component of acceleration as defined in [swsAccelerationComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAccelerationComponent_e.html)
- `NStepNum`: Solution step number (use 1 for steady state)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `NUnits`: Units of acceleration as defined by [swsAccelerationUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAccelerationUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetMinMaxAcceleration](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxAcceleration.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## Remarks

This method returns the following array:

{`node_with_minimum_acceleration`, `minimum_acceleration`, `node_with_maximum_acceleration`, `maximum_acceleration`},

where the nodes are integer indexes, and the accelerations are in scientific notation.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetAccelerationComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetAccelerationComponentForAllStepsAtNode.html)
[ICWResults::GetAccelerationForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetAccelerationForEntities.html)
[ICWResults::GetEnvelopeAccelerationForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetEnvelopeAccelerationForEntities.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
