---
title: "GetStrainForEntities3 Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStrainForEntities3"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainForEntities3.html"
---

# GetStrainForEntities3 Method (ICWResults)

Gets the specified strain component for the specified entities at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStrainForEntities3( _
   ByVal BValueByNode As System.Boolean, _
   ByVal NComponent As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NShellFace As System.Integer, _
   ByVal NPlyNumber As System.Integer, _
   ByVal BInPlyDirection As System.Boolean, _
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
Dim NShellFace As System.Integer
Dim NPlyNumber As System.Integer
Dim BInPlyDirection As System.Boolean
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetStrainForEntities3(BValueByNode, NComponent, NStepNumber, DispPlane, ArraySelectedEntities, NShellFace, NPlyNumber, BInPlyDirection, ErrorCode)
```

### C#

```csharp
System.object GetStrainForEntities3(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   System.int NShellFace,
   System.int NPlyNumber,
   System.bool BInPlyDirection,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStrainForEntities3(
   System.bool BValueByNode,
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   System.int NShellFace,
   System.int NPlyNumber,
   System.bool BInPlyDirection,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BValueByNode`: True to get the strain value by node, false to get the strain value by element
- `NComponent`: Strain component as defined in [swsStrainComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrainComponent_e.html)
- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if NComponent is not a directional component
- `ArraySelectedEntities`: Array of geometric entities
- `NShellFace`: Option as defined in [swsShellFace_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShellFace_e.html)
- `NPlyNumber`: Ply number to show the strain; available only when the model uses composite shells
- `BInPlyDirection`: 1 to display the results in ply direction on the surface of the ply, 0 to display the results in the transverse direction to the ply direction on the surface of the ply
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of {node/element #, strain value} pairs

## VBA Syntax

See [CWResults::GetStrainForEntities3](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStrainForEntities3.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
