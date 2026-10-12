---
title: "GetStrainForEntities2 Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStrainForEntities2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainForEntities2.html"
---

# GetStrainForEntities2 Method (ICWResults)

Obsolete. Superseded by [ICWResults::GetStrainForEntities3](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults~GetStrainForEntities3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStrainForEntities2( _
   ByVal BValueByNode As System.Boolean, _
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
Dim BValueByNode As System.Boolean
Dim NComponent As System.Integer
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim ArraySelectedEntities As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetStrainForEntities2(BValueByNode, NComponent, NStepNumber, DispPlane, ArraySelectedEntities, ErrorCode)
```

### C#

```csharp
System.object GetStrainForEntities2(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStrainForEntities2(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BValueByNode`: True to get the strain value by node, false to get the strain value by element
- `NComponent`: Strain as defined in [swsStrainComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrainComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Reference geometry
- `ArraySelectedEntities`: Array of geometric entities
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of strain results (each node or element followed by the strain value)

## VBA Syntax

See [CWResults::GetStrainForEntities2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStrainForEntities2.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxStrain Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStrain.html)
[ICWResults::GetStrainComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainComponentForAllStepsAtNode.html)
[ICWResults::GetStrain Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrain.html)

## Availability

SOLIDWORKS Simulation API 2009 SP5.0
