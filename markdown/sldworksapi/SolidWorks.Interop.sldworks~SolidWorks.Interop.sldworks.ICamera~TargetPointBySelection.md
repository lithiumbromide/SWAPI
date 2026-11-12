---
title: "TargetPointBySelection Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "TargetPointBySelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointBySelection.html"
---

# TargetPointBySelection Property (ICamera)

Gets or sets whether you can set the target point.

## Syntax

### Visual Basic (Declaration)

```vb
Property TargetPointBySelection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Boolean

instance.TargetPointBySelection = value

value = instance.TargetPointBySelection
```

### C#

```csharp
System.bool TargetPointBySelection {get; set;}
```

### C++/CLI

```cpp
property System.bool TargetPointBySelection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if you can set the target point, false if not

## VBA Syntax

See [Camera::TargetPointBySelection](ms-its:sldworksapivb6.chm::/sldworks~Camera~TargetPointBySelection.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::TargetPointPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointPosition.html)
[ICamera::GetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetTargetPointEntity.html)
[ICamera::SetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetTargetPointEntity.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
