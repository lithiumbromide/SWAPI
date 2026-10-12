---
title: "SetReferenceCoordinateSystem2 Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetReferenceCoordinateSystem2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetReferenceCoordinateSystem2.html"
---

# SetReferenceCoordinateSystem2 Method (ICWRemoteLoad)

Sets the coordinate system used for interpreting the location and direction of the remote load, mass, or displacement.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferenceCoordinateSystem2( _
   ByVal BGlobal As System.Boolean, _
   ByVal DispRefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim BGlobal As System.Boolean
Dim DispRefEntity As System.Object

instance.SetReferenceCoordinateSystem2(BGlobal, DispRefEntity)
```

### C#

```csharp
void SetReferenceCoordinateSystem2(
   System.bool BGlobal,
   System.object DispRefEntity
)
```

### C++/CLI

```cpp
void SetReferenceCoordinateSystem2(
   System.bool BGlobal,
   System.Object^ DispRefEntity
)
```

### Parameters

- `BGlobal`: -1 or true to use the global coordinate system, 0 or false to use the coordinate system specified by DispRefEntity
- `DispRefEntity`: User-defined coordinate system; valid only if BGlobal = false

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
