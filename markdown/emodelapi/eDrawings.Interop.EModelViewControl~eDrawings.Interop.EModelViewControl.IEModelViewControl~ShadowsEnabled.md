---
title: "ShadowsEnabled Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ShadowsEnabled"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShadowsEnabled.html"
---

# ShadowsEnabled Property (IEModelViewControl)

Gets or sets whether shadows are enabled in parts and assemblies.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShadowsEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

instance.ShadowsEnabled = value

value = instance.ShadowsEnabled
```

### C#

```csharp
System.bool ShadowsEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool ShadowsEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if shadows are enabled, false if not

## VBA Syntax

See [EModelViewControl::ShadowsEnabled](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ShadowsEnabled.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::StereoEnabled Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~StereoEnabled.html)

## Availability

eDrawings API 2014 SP0
