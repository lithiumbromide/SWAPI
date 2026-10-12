---
title: "GetStressComponentForAllStepsAtNode Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStressComponentForAllStepsAtNode"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressComponentForAllStepsAtNode.html"
---

# GetStressComponentForAllStepsAtNode Method (ICWResults)

Gets the specified stress component at the specified node for all solution steps.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStressComponentForAllStepsAtNode( _
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

value = instance.GetStressComponentForAllStepsAtNode(NComponent, NNodeNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetStressComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStressComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Stress component as defined in [swsStressComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStressComponent_e.html)
- `NNodeNum`: Node number
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `NUnits`: Unit as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of stress results

## VBA Syntax

See [CWResults::GetStressComponentForAllStepsAtNode](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStressComponentForAllStepsAtNode.html).

## Remarks

Sx, Sy, Sz, Txy, Tyz, Txz, P1, P2, P3, VON, and INT for all nodes or elements at the specified step number.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxStress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStress.html)
[ICWResults::GetStress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStress.html)
[ICWResults::GetStressForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressForEntities.html)
[ICWResults::GetStressTensorValuesForAllNodesOfElement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressTensorValuesForAllNodesOfElement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
