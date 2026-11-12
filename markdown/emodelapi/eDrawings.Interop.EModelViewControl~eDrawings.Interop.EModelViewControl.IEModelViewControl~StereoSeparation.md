---
title: "StereoSeparation Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "StereoSeparation"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoSeparation.html"
---

# StereoSeparation Property (IEModelViewControl)

Gets or sets the angle of separation between right and left stereo views.

## Syntax

### Visual Basic (Declaration)

```vb
Property StereoSeparation As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Single

instance.StereoSeparation = value

value = instance.StereoSeparation
```

### C#

```csharp
System.float StereoSeparation {get; set;}
```

### C++/CLI

```cpp
property System.float StereoSeparation {
   System.float get();
   void set (    System.float value);
}
```

### Property Value

Angle of separation between right and left stereo views; default angle = 3.0 degrees

## VBA Syntax

See [EModelViewControl::StereoSeparation](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~StereoSeparation.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::StereoEnabled Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoEnabled.html)
[IEModelViewControl::StereoFocalLength Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoFocalLength.html)

## Availability

eDrawings API 2014 SP1
