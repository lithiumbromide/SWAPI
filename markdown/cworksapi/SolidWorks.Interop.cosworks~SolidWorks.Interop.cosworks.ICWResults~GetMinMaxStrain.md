---
title: "GetMinMaxStrain Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxStrain"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStrain.html"
---

# GetMinMaxStrain Method (ICWResults)

Gets the algebraic minimum and maximum for the specified strain component, element, and solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxStrain( _
   ByVal NComponent As System.Integer, _
   ByVal NElementNumber As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NElementNumber As System.Integer
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxStrain(NComponent, NElementNumber, NStepNumber, DispPlane, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxStrain(
   System.int NComponent,
   System.int NElementNumber,
   System.int NStepNumber,
   System.object DispPlane,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxStrain(
   System.int NComponent,
   System.int NElementNumber,
   System.int NStepNumber,
   System.Object^ DispPlane,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Strain component as defined in [swsStrainComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrainComponent_e.html)
- `NElementNumber`: Element number
- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if reference geometry does not exist
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetMinMaxStrain](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxStrain.html).

## Remarks

This method returns the following array:

{`node_with_minimum_strain`, `minimum_strain`, `node_with_maximum_strain`, `maximum_strain`},

where the nodes are integer indexes, and the strains are in scientific notation.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetStrainComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainComponentForAllStepsAtNode.html)
[ICWResults::GetStrainForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainForEntities.html)
[ICWResults::GetStrain Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrain.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
