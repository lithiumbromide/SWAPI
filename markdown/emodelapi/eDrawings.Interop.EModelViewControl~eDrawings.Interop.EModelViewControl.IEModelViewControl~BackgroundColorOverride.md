---
title: "BackgroundColorOverride Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "BackgroundColorOverride"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColorOverride.html"
---

# BackgroundColorOverride Property (IEModelViewControl)

Specifies whether to override the document's background color and display the color specified by [IEModelViewControl::BackgroundColor](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColor.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundColorOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

instance.BackgroundColorOverride = value

value = instance.BackgroundColorOverride
```

### C#

```csharp
System.bool BackgroundColorOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool BackgroundColorOverride {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to override the document's background color, false to not

## VBA Syntax

See [EModelViewControl::BackgroundColorOverride](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~BackgroundColorOverride.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

If set to true, then you can also use [IEModelViewControl::BackgroundColorGradient](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColorGradient.html) to apply a gradient background.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2007 SP0
