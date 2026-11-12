---
title: "GetStressForEntities2 Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStressForEntities2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressForEntities2.html"
---

# GetStressForEntities2 Method (ICWResults)

Obsolete. Superseded by [ICWResults::GetStressForEntities3](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults~GetStressForEntities3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStressForEntities2( _
   ByVal BValueByNode As System.Boolean, _
   ByVal NComponent As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim BValueByNode As System.Boolean
Dim NComponent As System.Integer
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim ArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetStressForEntities2(BValueByNode, NComponent, NStepNumber, DispPlane, ArraySelectedEntities, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetStressForEntities2(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStressForEntities2(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BValueByNode`: True to get the stress value by node, false to get the stress value by element
- `NComponent`: Stress as defined in [swsStressComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStressComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for steady state)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArraySelectedEntities`: Array of geometric entities
- `NUnits`: Unit as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of stress results (each node or element followed by the stress value)

## VBA Syntax

See [CWResults::GetStressForEntities2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStressForEntities2.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxStress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStress.html)
[ICWResults::GetStress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStress.html)
[ICWResults::GetStressComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressComponentForAllStepsAtNode.html)

## Availability

SOLIDWORKS Simulation API 2009 SP5.0
