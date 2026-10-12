---
title: "SetReferenceEntity Method (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "SetReferenceEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~SetReferenceEntity.html"
---

# SetReferenceEntity Method (ICWCentriFugalForce)

Replaces the direction reference entity.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferenceEntity( _
   ByVal RefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
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

- `RefEntity`: Direction reference entity (axis, edge, or cylindrical face)

## VBA Syntax

See [CWCentriFugalForce::SetReferenceEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCentriFugalForce~SetReferenceEntity.html).

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
