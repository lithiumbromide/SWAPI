---
title: "SetEntityForTargetOrientation2 Method (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "SetEntityForTargetOrientation2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForTargetOrientation2.html"
---

# SetEntityForTargetOrientation2 Method (ICWDropTestSetup)

Sets the orientation reference for the impact plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEntityForTargetOrientation2( _
   ByVal DispEntity As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim DispEntity As System.Object
Dim value As System.Boolean

value = instance.SetEntityForTargetOrientation2(DispEntity)
```

### C#

```csharp
System.bool SetEntityForTargetOrientation2(
   System.object DispEntity
)
```

### C++/CLI

```cpp
System.bool SetEntityForTargetOrientation2(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Reference plane

## Remarks

This method is valid only if [ICWDropTestSetup::TargetOrientationType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~TargetOrientationType.html) = swsDropTargetOrientationType_e.swsDropTargetOrientationType_ParallelToRefPlane.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
