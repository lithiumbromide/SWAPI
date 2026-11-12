---
title: "PaperColor Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "PaperColor"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~PaperColor.html"
---

# PaperColor Property (IEModelViewControl)

Gets or sets the color of the paper (sheet) for an eDrawings document of a drawing only.

## Syntax

### Visual Basic (Declaration)

```vb
Property PaperColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

instance.PaperColor = value

value = instance.PaperColor
```

### C#

```csharp
System.int PaperColor {get; set;}
```

### C++/CLI

```cpp
property System.int PaperColor {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

COLORREF value (see Remarks)

## VBA Syntax

See [EModelViewControl::PaperColor](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~PaperColor.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

[IEModelViewControl::PaperColorOverride](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~PaperColorOverride.html) must be true for this method to have an effect.

A COLORREF is a 32-bit integer value that specifies the red, blue, and green components of a 24-bit color.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2007 SP0
