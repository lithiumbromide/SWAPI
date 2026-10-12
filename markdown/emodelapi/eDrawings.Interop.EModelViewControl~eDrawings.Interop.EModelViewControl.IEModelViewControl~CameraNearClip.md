---
title: "CameraNearClip Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "CameraNearClip"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CameraNearClip.html"
---

# CameraNearClip Property (IEModelViewControl)

Gets or sets the distance of the camera near clip plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property CameraNearClip As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Single

instance.CameraNearClip = value

value = instance.CameraNearClip
```

### C#

```csharp
System.float CameraNearClip {get; set;}
```

### C++/CLI

```cpp
property System.float CameraNearClip {
   System.float get();
   void set (    System.float value);
}
```

### Property Value

Value from 0.0 at the camera to 1.0 at the target

## VBA Syntax

See [EModelViewControl::CameraNearClip](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~CameraNearClip.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::CameraProjection Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CameraProjection.html)
[IEModelViewControl::ViewCamera Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ViewCamera.html)
[IEModelViewControl::StereoFocalLength Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoFocalLength.html)

## Availability

eDrawings API 2014 SP1
