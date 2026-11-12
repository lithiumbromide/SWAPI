---
title: "GetMinMaxVelocity Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxVelocity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxVelocity.html"
---

# GetMinMaxVelocity Method (ICWResults)

Gets the algebraic minimum and maximum for the specified velocity component and solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxVelocity( _
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

value = instance.GetMinMaxVelocity(NComponent, NStepNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxVelocity(
   System.int NComponent,
   System.int NStepNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxVelocity(
   System.int NComponent,
   System.int NStepNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Velocity component as defined in [swsVelocityComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsVelocityComponent_e.html)
- `NStepNum`: Solution step number (use 1 for steady state)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if reference geometry does not exist
- `NUnits`: Units of velocity as defined in [swsVelocityUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsVelocityUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetMinMaxVelocity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxVelocity.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## Remarks

This method returns the following array:

{`node_with_minimum_velocity`, `minimum_velocity`, `node_with_maximum_velocity`, `maximum_velocity`},

where the nodes are integer indexes, and the velocities are in scientific notation.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetEnvelopeVelocityForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetEnvelopeVelocityForEntities.html)
[ICWResults::GetVelocityComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetVelocityComponentForAllStepsAtNode.html)
[ICWResults::GetVelocityForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetVelocityForEntities.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
