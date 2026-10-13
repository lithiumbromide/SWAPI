---
title: "BackgroundColor Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "BackgroundColor"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColor.html"
---

# BackgroundColor Property (IEModelViewControl)

Gets or sets the background color for all eDrawings files.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

instance.BackgroundColor = value

value = instance.BackgroundColor
```

### C#

```csharp
System.int BackgroundColor {get; set;}
```

### C++/CLI

```cpp
property System.int BackgroundColor {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

COLORREF value (see Remarks)

## VBA Syntax

See [EModelViewControl::BackgroundColor](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~BackgroundColor.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

[IEModelViewControl::BackgroundColorOverride](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColorOverride.html) must be set to true for this method to have an effect.

A COLORREF is a 32-bit integer value that specifies the red, blue, and green components of a 24-bit color.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::BackgroundColorGradient Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColorGradient.html)
[IEModelViewControl::BackgroundImagePath Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundImagePath.html)

## Availability

eDrawings API 2006 SP01
