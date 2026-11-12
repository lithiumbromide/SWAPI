---
title: "TargetPointPosition Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "TargetPointPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointPosition.html"
---

# TargetPointPosition Property (ICamera)

Gets or sets the position of the target point.

## Syntax

### Visual Basic (Declaration)

```vb
Property TargetPointPosition As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As MathPoint

instance.TargetPointPosition = value

value = instance.TargetPointPosition
```

### C#

```csharp
MathPoint TargetPointPosition {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ TargetPointPosition {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Position of target point

## VBA Syntax

See [Camera::TargetPointPosition](ms-its:sldworksapivb6.chm::/sldworks~Camera~TargetPointPosition.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetTargetPointEntity.html)
[ICamera::SetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetTargetPointEntity.html)
[ICamera::TargetPointBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointBySelection.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
