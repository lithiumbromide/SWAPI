---
title: "CameraProjection Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "CameraProjection"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CameraProjection.html"
---

# CameraProjection Property (IEModelViewControl)

Gets or sets the camera projection type.

## Syntax

### Visual Basic (Declaration)

```vb
Property CameraProjection As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.String

instance.CameraProjection = value

value = instance.CameraProjection
```

### C#

```csharp
System.string CameraProjection {get; set;}
```

### C++/CLI

```cpp
property System.String^ CameraProjection {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Valid string values:

- **Perspective**
- **Orthographic**

## VBA Syntax

See [EModelViewControl::CameraProjection](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~CameraProjection.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ViewCamera Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ViewCamera.html)
[IEModelViewControl::CameraNearClip Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CameraNearClip.html)
[IEModelViewControl::StereoFocalLength Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoFocalLength.html)

## Availability

eDrawings API 2014 SP1
