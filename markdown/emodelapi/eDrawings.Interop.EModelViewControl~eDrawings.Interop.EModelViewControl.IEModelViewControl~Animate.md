---
title: "Animate Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "Animate"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Animate.html"
---

# Animate Method (IEModelViewControl)

Sets the state of animation.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Animate( _
   ByVal Animating As EMVAnimateAction _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim Animating As EMVAnimateAction

instance.Animate(Animating)
```

### C#

```csharp
void Animate(
   EMVAnimateAction Animating
)
```

### C++/CLI

```cpp
void Animate(
   EMVAnimateAction Animating
)
```

### Parameters

- `Animating`: Animate option as defined in [EMVAnimateAction](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVAnimateAction.html)

## VBA Syntax

See [EModelViewControl::Animate](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~Animate.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
