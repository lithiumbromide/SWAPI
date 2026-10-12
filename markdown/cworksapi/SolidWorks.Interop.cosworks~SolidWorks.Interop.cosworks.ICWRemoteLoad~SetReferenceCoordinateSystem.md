---
title: "SetReferenceCoordinateSystem Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetReferenceCoordinateSystem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetReferenceCoordinateSystem.html"
---

# SetReferenceCoordinateSystem Method (ICWRemoteLoad)

Obsolete. Superseded by [ICWRemoteLoad::SetReferenceCoordinateSystem2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetReferenceCoordinateSystem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferenceCoordinateSystem( _
   ByVal BGlobal As System.Integer, _
   ByVal DispRefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim BGlobal As System.Integer
Dim DispRefEntity As System.Object

instance.SetReferenceCoordinateSystem(BGlobal, DispRefEntity)
```

### C#

```csharp
void SetReferenceCoordinateSystem(
   System.int BGlobal,
   System.object DispRefEntity
)
```

### C++/CLI

```cpp
void SetReferenceCoordinateSystem(
   System.int BGlobal,
   System.Object^ DispRefEntity
)
```

### Parameters

- `BGlobal`: 1 to use the global coordinate system, 0 to use the coordinate system specified by DispRefEntity
- `DispRefEntity`: User-defined coordinate system; valid only if BGlobal = 0

## VBA Syntax

See [CWRemoteLoad::SetReferenceCoordinateSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~SetReferenceCoordinateSystem.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
