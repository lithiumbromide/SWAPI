---
title: "InkMarkupName Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "InkMarkupName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~InkMarkupName.html"
---

# InkMarkupName Property (IEModelViewControl)

Gets the name of the specified SOLIDWORKS ink markup.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property InkMarkupName( _
   ByVal InkMarkupIndex As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim InkMarkupIndex As System.Integer
Dim value As System.String

value = instance.InkMarkupName(InkMarkupIndex)
```

### C#

```csharp
System.string InkMarkupName(
   System.int InkMarkupIndex
) {get;}
```

### C++/CLI

```cpp
property System.String^ InkMarkupName {
   System.String^ get(System.int InkMarkupIndex);
}
```

### Parameters

- `InkMarkupIndex`: Index of SOLIDWORKS ink markup whose name to retrieve

### Property Value

Name of SOLIDWORKS ink markup

## VBA Syntax

See [EModelViewControl::InkMarkupName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~InkMarkupName.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ActivateInkMarkup Method ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ActivateInkMarkup.html)
[IEModelViewControl::InkMarkupCount Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~InkMarkupCount.html)
[IEModelViewControl::ShowInkMarkup Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowInkMarkup.html)

## Availability

eDrawings 2020 SP0
