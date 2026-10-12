---
title: "SetEntitiesWeldPath Method (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "SetEntitiesWeldPath"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldPath.html"
---

# SetEntitiesWeldPath Method (ICosmeticWeldBeadFeatureData)

Sets the entities for this cosmetic weld bead, which was created using a weld path.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEntitiesWeldPath( _
   ByVal Entities As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim Entities As System.Object

instance.SetEntitiesWeldPath(Entities)
```

### C#

```csharp
void SetEntitiesWeldPath(
   System.object Entities
)
```

### C++/CLI

```cpp
void SetEntitiesWeldPath(
   System.Object^ Entities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entities`: Array of entities of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html), or a combination of edges and sketches (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::SetEntitiesWeldPath](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~SetEntitiesWeldPath.html).

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldPath.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
