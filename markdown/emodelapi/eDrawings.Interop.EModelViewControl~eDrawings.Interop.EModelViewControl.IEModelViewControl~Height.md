---
title: "Height Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "Height"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Height.html"
---

# Height Property (IEModelViewControl)

Gets the height of the control.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Height As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

value = instance.Height
```

### C#

```csharp
System.int Height {get;}
```

### C++/CLI

```cpp
property System.int Height {
   System.int get();
}
```

### Property Value

Height of the control

## VBA Syntax

See [EModelViewControl::Height](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~Height.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

Depending on the programming environment, height and [width](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Width.html) may be displayed in either Twips or Pixels. See MSDN for more information on Twips.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
