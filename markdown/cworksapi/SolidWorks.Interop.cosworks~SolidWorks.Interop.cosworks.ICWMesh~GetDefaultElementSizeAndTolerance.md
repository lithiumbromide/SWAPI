---
title: "GetDefaultElementSizeAndTolerance Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "GetDefaultElementSizeAndTolerance"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetDefaultElementSizeAndTolerance.html"
---

# GetDefaultElementSizeAndTolerance Method (ICWMesh)

Gets the default element size and tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetDefaultElementSizeAndTolerance( _
   ByVal NUnits As System.Integer, _
   ByRef DElementSize As System.Double, _
   ByRef DTolerance As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim NUnits As System.Integer
Dim DElementSize As System.Double
Dim DTolerance As System.Double

instance.GetDefaultElementSizeAndTolerance(NUnits, DElementSize, DTolerance)
```

### C#

```csharp
void GetDefaultElementSizeAndTolerance(
   System.int NUnits,
   out System.double DElementSize,
   out System.double DTolerance
)
```

### C++/CLI

```cpp
void GetDefaultElementSizeAndTolerance(
   System.int NUnits,
   [Out] System.double DElementSize,
   [Out] System.double DTolerance
)
```

### Parameters

- `NUnits`: Mesh linear units as defined [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `DElementSize`: Average global element size
- `DTolerance`: Tolerance (if the distance between any two nodes is less than this distance, then the nodes are merged)

## VBA Syntax

See [CWMesh::GetDefaultElementSizeAndTolerance](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~GetDefaultElementSizeAndTolerance.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)
[ICWMesh::GetElementDataFromEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementDataFromEntity.html)
[ICWMesh::GetElementLocation Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElementLocation.html)
[ICWMesh::GetElements Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~GetElements.html)
[ICWMesh::ElementCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementCount.html)
[ICWMesh::ElementSize Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~ElementSize.html)
[ICWMesh::MinElementsInCircle Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MinElementsInCircle.html)
[ICWMesh::MaxAspectRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~MaxAspectRatio.html)
[ICWMesh::NumberOfLoops Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~NumberOfLoops.html)
[ICWMesh::AutomaticLooping Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~AutomaticLooping.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
