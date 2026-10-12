---
title: "GetStrainForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStrainForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainForEntities.html"
---

# GetStrainForEntities Method (ICWResults)

Obsolete. Superseded by [ICWResults::GetStrainForEntities2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults~GetStrainForEntities2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStrainForEntities( _
   ByVal NComponent As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim ArraySelectedEntities As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetStrainForEntities(NComponent, NStepNumber, DispPlane, ArraySelectedEntities, ErrorCode)
```

### C#

```csharp
System.object GetStrainForEntities(
   System.int NComponent,
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStrainForEntities(
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Strain as defined in [swsStrainComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrainComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Reference geometry
- `ArraySelectedEntities`: Array of geometric entities
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of strain results

## VBA Syntax

See [CWResults::GetStrainForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStrainForEntities.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxStrain Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStrain.html)
[ICWResults::GetStrain Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrain.html)
[ICWResults::GetStrainComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainComponentForAllStepsAtNode.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
