---
title: "BackgroundColorGradient Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "BackgroundColorGradient"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColorGradient.html"
---

# BackgroundColorGradient Property (IEModelViewControl)

Specifies whether to apply a gradient background using the document's background color.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundColorGradient As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

instance.BackgroundColorGradient = value

value = instance.BackgroundColorGradient
```

### C#

```csharp
System.bool BackgroundColorGradient {get; set;}
```

### C++/CLI

```cpp
property System.bool BackgroundColorGradient {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to apply a gradient background, false to not

## VBA Syntax

See [EModelViewControl::BackgroundColorGradient](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~BackgroundColorGradient.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

[IEModelViewControl::BackgroundColorOverride](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColorOverride.html) must be set to true for this method to have an effect.

If IEModelViewControl::BackgroundColorOverride and this method are true, then the color displayed is the color set by [IEModelViewControl::BackgroundColor](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColor.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2007 SP0
