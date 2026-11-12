---
title: "Width Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "Width"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Width.html"
---

# Width Property (IEModelViewControl)

Gets the width of the control.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Width As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

value = instance.Width
```

### C#

```csharp
System.int Width {get;}
```

### C++/CLI

```cpp
property System.int Width {
   System.int get();
}
```

### Property Value

Width of the control

## VBA Syntax

See [EModelViewControl::Width](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~Width.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

Depending on the programming environment, width and [height](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Height.html) may be displayed in either Twips or Pixels. See MSDN for more information on Twips

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
