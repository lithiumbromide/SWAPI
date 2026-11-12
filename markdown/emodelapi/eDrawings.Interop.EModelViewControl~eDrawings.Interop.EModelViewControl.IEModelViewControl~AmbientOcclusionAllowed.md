---
title: "AmbientOcclusionAllowed Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "AmbientOcclusionAllowed"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~AmbientOcclusionAllowed.html"
---

# AmbientOcclusionAllowed Property (IEModelViewControl)

Gets whether ambient occlusion is permitted.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AmbientOcclusionAllowed As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

value = instance.AmbientOcclusionAllowed
```

### C#

```csharp
System.bool AmbientOcclusionAllowed {get;}
```

### C++/CLI

```cpp
property System.bool AmbientOcclusionAllowed {
   System.bool get();
}
```

### Property Value

True if ambient occlusion is permitted, false if not

## VBA Syntax

See [EModelViewControl::AmbientOcclusionAllowed](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~AmbientOcclusionAllowed.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::AmbientOcclusionEnabled Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~AmbientOcclusionEnabled.html)

## Availability

eDrawings 2019 SP0
