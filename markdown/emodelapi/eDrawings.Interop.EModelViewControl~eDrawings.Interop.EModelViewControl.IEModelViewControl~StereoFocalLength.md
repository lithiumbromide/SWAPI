---
title: "StereoFocalLength Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "StereoFocalLength"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoFocalLength.html"
---

# StereoFocalLength Property (IEModelViewControl)

Gets or sets the distance between camera position and the stereo focal plane in terms of the camera eye distance.

## Syntax

### Visual Basic (Declaration)

```vb
Property StereoFocalLength As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Single

instance.StereoFocalLength = value

value = instance.StereoFocalLength
```

### C#

```csharp
System.float StereoFocalLength {get; set;}
```

### C++/CLI

```cpp
property System.float StereoFocalLength {
   System.float get();
   void set (    System.float value);
}
```

### Property Value

Distance between camera position and the stereo focal plane in terms of the camera eye distance; default stereo distance = 0

## VBA Syntax

See [EModelViewControl::StereoFocalLength](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~StereoFocalLength.html).

## Remarks

A stereo distance of 0 corresponds to the stereo focal plane being set at the camera target.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::StereoEnabled Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoEnabled.html)
[IEModelViewControl::StereoSeparation Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoSeparation.html)
[IEModelViewControl::CameraNearClip Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CameraNearClip.html)
[IEModelViewControl::CameraProjection Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CameraProjection.html)

## Availability

eDrawings API 2014 SP1
