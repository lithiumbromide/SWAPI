---
title: "InkMarkupCount Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "InkMarkupCount"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~InkMarkupCount.html"
---

# InkMarkupCount Property (IEModelViewControl)

Gets the number of SOLIDWORKS ink markups.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property InkMarkupCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

value = instance.InkMarkupCount
```

### C#

```csharp
System.int InkMarkupCount {get;}
```

### C++/CLI

```cpp
property System.int InkMarkupCount {
   System.int get();
}
```

### Property Value

Number of SOLIDWORKS ink markups

## VBA Syntax

See [EModelViewControl::InkMarkupCount](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~InkMarkupCount.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::InkMarkupName Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~InkMarkupName.html)
[IEModelViewControl::ShowInkMarkup Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowInkMarkup.html)
[IEModelViewControl::ActivateInkMarkup Method ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ActivateInkMarkup.html)

## Availability

eDrawings 2020 SP0
