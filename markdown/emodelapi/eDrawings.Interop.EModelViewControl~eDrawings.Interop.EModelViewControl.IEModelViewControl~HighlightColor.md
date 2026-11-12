---
title: "HighlightColor Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "HighlightColor"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~HighlightColor.html"
---

# HighlightColor Property (IEModelViewControl)

Gets or sets the color used when an entity is selected.

## Syntax

### Visual Basic (Declaration)

```vb
Property HighlightColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

instance.HighlightColor = value

value = instance.HighlightColor
```

### C#

```csharp
System.int HighlightColor {get; set;}
```

### C++/CLI

```cpp
property System.int HighlightColor {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

COLORREF value (see **Remarks**)

## VBA Syntax

See [EModelViewControl::HighlightColor](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~HighlightColor.html).

## Examples

```vb
EModelViewControl::HighlightColor(16711680) //Set color to red
See IEModelViewControl examples.
```

## Remarks

A COLORREF is a 32-bit integer value that specifies the red, blue, and green components of a 24-bit color.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2007 SP0
