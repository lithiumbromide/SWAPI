---
title: "AmbientOcclusionEnabled Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "AmbientOcclusionEnabled"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~AmbientOcclusionEnabled.html"
---

# AmbientOcclusionEnabled Property (IEModelViewControl)

Gets or sets whether ambient occlusion is enabled.

## Syntax

### Visual Basic (Declaration)

```vb
Property AmbientOcclusionEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

instance.AmbientOcclusionEnabled = value

value = instance.AmbientOcclusionEnabled
```

### C#

```csharp
System.bool AmbientOcclusionEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool AmbientOcclusionEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if ambient occlusion is enabled, false if disabled

## VBA Syntax

See [EModelViewControl::AmbientOcclusionEnabled](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~AmbientOcclusionEnabled.html).

## Remarks

This property is valid only if [IEModelViewControl::AmbientOcclusionAllowed](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~AmbientOcclusionAllowed.html) is true.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2019 SP0
