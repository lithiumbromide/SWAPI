---
title: "GetDisplacementAtPoints Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetDisplacementAtPoints"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDisplacementAtPoints.html"
---

# GetDisplacementAtPoints Method (ICWResults)

Gets the specified displacement component at the specified points for the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplacementAtPoints( _
   ByVal NComponent As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArrayPoints As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim ArrayPoints As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetDisplacementAtPoints(NComponent, NStepNumber, DispPlane, ArrayPoints, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetDisplacementAtPoints(
   System.int NComponent,
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArrayPoints,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetDisplacementAtPoints(
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArrayPoints,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Displacement component as defined in [swsDisplacementComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDisplacementComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArrayPoints`: Array of point coordinates
- `NUnits`: Linear units as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of displacement component values

## VBA Syntax

See [CWResults::GetDisplacementAtPoints](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetDisplacementAtPoints.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
