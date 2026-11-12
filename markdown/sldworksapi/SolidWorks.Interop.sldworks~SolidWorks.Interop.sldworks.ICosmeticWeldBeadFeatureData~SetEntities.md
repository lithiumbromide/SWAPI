---
title: "SetEntities Method (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "SetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntities.html"
---

# SetEntities Method (ICosmeticWeldBeadFeatureData)

Obsolete. Superseded by [ICosmeticWeldBeadFeatureData::SetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.html) and [ICosmeticWeldBeadFeatureData::SetEntitiesWeldTo.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldTo.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEntities( _
   ByVal Entities As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim Entities As System.Object

instance.SetEntities(Entities)
```

### C#

```csharp
void SetEntities(
   System.object Entities
)
```

### C++/CLI

```cpp
void SetEntities(
   System.Object^ Entities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entities`: Array of [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)s and [IEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)s

## VBA Syntax

See [CosmeticWeldBeadFeatureData::SetEntities](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~SetEntities.html).

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntities.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
