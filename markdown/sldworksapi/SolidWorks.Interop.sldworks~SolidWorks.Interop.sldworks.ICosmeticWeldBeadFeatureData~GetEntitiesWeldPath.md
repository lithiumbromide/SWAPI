---
title: "GetEntitiesWeldPath Method (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "GetEntitiesWeldPath"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldPath.html"
---

# GetEntitiesWeldPath Method (ICosmeticWeldBeadFeatureData)

Gets the entities for this cosmetic weld bead, which was created using a weld path.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesWeldPath() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Object

value = instance.GetEntitiesWeldPath()
```

### C#

```csharp
System.object GetEntitiesWeldPath()
```

### C++/CLI

```cpp
System.Object^ GetEntitiesWeldPath();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of entities of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) or [sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html) or a combination of edges and sketches

## VBA Syntax

See [CosmeticWeldBeadFeatureData::GetEntitiesWeldPath](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~GetEntitiesWeldPath.html).

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::SetEntitiesWeldPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldPath.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
