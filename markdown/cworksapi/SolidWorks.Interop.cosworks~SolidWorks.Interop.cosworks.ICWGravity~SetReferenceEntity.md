---
title: "SetReferenceEntity Method (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "SetReferenceEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~SetReferenceEntity.html"
---

# SetReferenceEntity Method (ICWGravity)

Sets the direction reference for gravity.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferenceEntity( _
   ByVal RefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
Dim RefEntity As System.Object

instance.SetReferenceEntity(RefEntity)
```

### C#

```csharp
void SetReferenceEntity(
   System.object RefEntity
)
```

### C++/CLI

```cpp
void SetReferenceEntity(
   System.Object^ RefEntity
)
```

### Parameters

- `RefEntity`: Face, edge, or plane

## VBA Syntax

See [CWGravity::SetReferenceEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGravity~SetReferenceEntity.html).

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)
[ICWGravity::ReverseDirectionAlongPlaneDir1 Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionAlongPlaneDir1.html)
[ICWGravity::ReverseDirectionAlongPlaneDir2 Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionAlongPlaneDir2.html)
[ICWGravity::ReverseDirectionNormalToPlane Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionNormalToPlane.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
