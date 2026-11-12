---
title: "IsMeasureEnabled Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "IsMeasureEnabled"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~IsMeasureEnabled.html"
---

# IsMeasureEnabled Property (IEModelViewControl)

Gets whether the current document is measure-enabled.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsMeasureEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

value = instance.IsMeasureEnabled
```

### C#

```csharp
System.bool IsMeasureEnabled {get;}
```

### C++/CLI

```cpp
property System.bool IsMeasureEnabled {
   System.bool get();
}
```

### Property Value

True if the current document is measure-enabled, false if not

## VBA Syntax

See [EModelViewControl::IsMeasureEnabled](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~IsMeasureEnabled.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2009 SP0
