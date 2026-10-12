---
title: "SetEntitiesWeldTo Method (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "SetEntitiesWeldTo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldTo.html"
---

# SetEntitiesWeldTo Method (ICosmeticWeldBeadFeatureData)

Sets the weld-to entities for this cosmetic weld bead, which was created using weld geometry.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEntitiesWeldTo( _
   ByVal Entities As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim Entities As System.Object

instance.SetEntitiesWeldTo(Entities)
```

### C#

```csharp
void SetEntitiesWeldTo(
   System.object Entities
)
```

### C++/CLI

```cpp
void SetEntitiesWeldTo(
   System.Object^ Entities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entities`: Array of weld-to entities of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::SetEntitiesWeldTo](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~SetEntitiesWeldTo.html).

## Remarks

The weld-to entities must be the same type of entities; e.g., all faces or all edges.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldTo.html)
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldFrom.html)
[ICosmeticWeldBeadFeatureData::SetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
