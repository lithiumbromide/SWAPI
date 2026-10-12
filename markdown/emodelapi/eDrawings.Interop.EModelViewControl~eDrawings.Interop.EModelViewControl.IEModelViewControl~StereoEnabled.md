---
title: "StereoEnabled Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "StereoEnabled"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoEnabled.html"
---

# StereoEnabled Property (IEModelViewControl)

Gets or sets whether stereographic viewing is enabled.

## Syntax

### Visual Basic (Declaration)

```vb
Property StereoEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

instance.StereoEnabled = value

value = instance.StereoEnabled
```

### C#

```csharp
System.bool StereoEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool StereoEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if stereographic viewing is enabled, false if not

## VBA Syntax

See [EModelViewControl::StereoEnabled](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~StereoEnabled.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::StereoFocalLength Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoFocalLength.html)
[IEModelViewControl::StereoSeparation Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoSeparation.html)
[IEModelViewControl::ShadowsEnabled Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShadowsEnabled.html)

## Availability

eDrawings API 2014 SP0
