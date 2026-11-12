---
title: "GetStrainComponentForAllStepsAtNode Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStrainComponentForAllStepsAtNode"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainComponentForAllStepsAtNode.html"
---

# GetStrainComponentForAllStepsAtNode Method (ICWResults)

Gets the specified strain component at the specified node for all solution steps.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStrainComponentForAllStepsAtNode( _
   ByVal NComponent As System.Integer, _
   ByVal NNodeNum As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NNodeNum As System.Integer
Dim DispPlane As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetStrainComponentForAllStepsAtNode(NComponent, NNodeNum, DispPlane, ErrorCode)
```

### C#

```csharp
System.object GetStrainComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.object DispPlane,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStrainComponentForAllStepsAtNode(
   System.int NComponent,
   System.int NNodeNum,
   System.Object^ DispPlane,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Strain component as defined in [swsStrainComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrainComponent_e.html)
- `NNodeNum`: Node number
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if reference geometry does not exist
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of strain results

## VBA Syntax

See [CWResults::GetStrainComponentForAllStepsAtNode](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStrainComponentForAllStepsAtNode.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxStrain Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStrain.html)
[ICWResults::GetStrain Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrain.html)
[ICWResults::GetStrainForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainForEntities.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
