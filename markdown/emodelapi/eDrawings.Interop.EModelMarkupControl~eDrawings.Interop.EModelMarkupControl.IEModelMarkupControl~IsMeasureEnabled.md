---
title: "IsMeasureEnabled Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "IsMeasureEnabled"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~IsMeasureEnabled.html"
---

# IsMeasureEnabled Property (IEModelMarkupControl)

Gets whether the current document is measure-enabled.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsMeasureEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
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

See [EModelViewControl::IsMeasureEnabled](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~IsMeasureEnabled.html).

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)

## Availability

eDrawings API 2009 SP0
