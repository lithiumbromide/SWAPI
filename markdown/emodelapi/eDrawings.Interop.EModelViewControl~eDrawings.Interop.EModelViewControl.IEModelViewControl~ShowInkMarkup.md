---
title: "ShowInkMarkup Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ShowInkMarkup"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowInkMarkup.html"
---

# ShowInkMarkup Property (IEModelViewControl)

Sets whether to display the specified SOLIDWORKS ink markup.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ShowInkMarkup( _
   ByVal InkMarkupIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim InkMarkupIndex As System.Integer

instance.ShowInkMarkup(InkMarkupIndex) = value
```

### C#

```csharp
System.bool ShowInkMarkup(
   System.int InkMarkupIndex
) {set;}
```

### C++/CLI

```cpp
property System.bool ShowInkMarkup {
   void set (System.int InkMarkupIndex, System.bool value);
}
```

### Parameters

- `InkMarkupIndex`: Index of SOLIDWORKS ink markup

### Property Value

True to display the specified ink markup, false to not

## VBA Syntax

See [EModelViewControl::ShowInkMarkup](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ShowInkMarkup.html).

## Remarks

After setting this property to true, you can call [IEModelViewControl::ActivateInkMarkup](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ActivateInkMarkup.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::InkMarkupCount Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~InkMarkupCount.html)
[IEModelViewControl::InkMarkupName Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~InkMarkupName.html)

## Availability

eDrawings 2020 SP0
