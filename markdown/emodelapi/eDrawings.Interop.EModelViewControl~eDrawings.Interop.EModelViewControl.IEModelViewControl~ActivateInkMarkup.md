---
title: "ActivateInkMarkup Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ActivateInkMarkup"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ActivateInkMarkup.html"
---

# ActivateInkMarkup Method (IEModelViewControl)

Activates the specified SOLIDWORKS ink markup.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ActivateInkMarkup( _
   ByVal InkMarkupIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim InkMarkupIndex As System.Integer

instance.ActivateInkMarkup(InkMarkupIndex)
```

### C#

```csharp
void ActivateInkMarkup(
   System.int InkMarkupIndex
)
```

### C++/CLI

```cpp
void ActivateInkMarkup(
   System.int InkMarkupIndex
)
```

### Parameters

- `InkMarkupIndex`: Index of SOLIDWORKS ink markup to activate

## VBA Syntax

See [EModelViewControl::ActivateInkMarkup](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ActivateInkMarkup.html).

## Remarks

This method is valid only if [IEModelViewControl::ShowInkMarkup](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowInkMarkup.html) is set to true.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::InkMarkupCount Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~InkMarkupCount.html)
[IEModelViewControl::InkMarkupName Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~InkMarkupName.html)

## Availability

eDrawings 2020 SP0
