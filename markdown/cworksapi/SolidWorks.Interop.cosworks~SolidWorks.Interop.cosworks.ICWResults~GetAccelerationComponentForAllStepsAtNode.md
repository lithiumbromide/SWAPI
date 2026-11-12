---
title: "GetAccelerationComponentForAllStepsAtNode Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetAccelerationComponentForAllStepsAtNode"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetAccelerationComponentForAllStepsAtNode.html"
---

# GetAccelerationComponentForAllStepsAtNode Method (ICWResults)

Gets the acceleration for all solution steps at the specified node for the specified acceleration component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAccelerationComponentForAllStepsAtNode( _
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

value = instance.GetAccelerationComponentForAllStepsAtNode(NComponent, NNodeNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetAccelerationComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetAccelerationComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Component of acceleration as defined in [swsAccelerationComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAccelerationComponent_e.html)
- `NNodeNum`: Node number
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `NUnits`: Units of acceleration as defined by [swsAccelerationUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAccelerationUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of acceleration component values

## VBA Syntax

See [CWResults::GetAccelerationComponentForAllStepsAtNode](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetAccelerationComponentForAllStepsAtNode.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
