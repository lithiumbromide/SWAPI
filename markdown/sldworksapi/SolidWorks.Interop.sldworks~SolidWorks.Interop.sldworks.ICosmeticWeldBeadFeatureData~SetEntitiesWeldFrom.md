---
title: "SetEntitiesWeldFrom Method (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "SetEntitiesWeldFrom"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.html"
---

# SetEntitiesWeldFrom Method (ICosmeticWeldBeadFeatureData)

Sets the weld-from entities for this cosmetic weld bead, which was created using weld geometry.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEntitiesWeldFrom( _
   ByVal Entities As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim Entities As System.Object

instance.SetEntitiesWeldFrom(Entities)
```

### C#

```csharp
void SetEntitiesWeldFrom(
   System.object Entities
)
```

### C++/CLI

```cpp
void SetEntitiesWeldFrom(
   System.Object^ Entities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entities`: Array of weld-from entities of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::SetEntitiesWeldFrom](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.html).

## Remarks

The weld-from entities must be the same type of entities; e.g., all faces or all edges.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldFrom Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldFrom.html)
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldTo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldTo.html)
[ICosmeticWeldBeadFeatureData::SetEntitiesWeldTo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldTo.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
