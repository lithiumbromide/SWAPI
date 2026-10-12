---
title: "LayerCount Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "LayerCount"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~LayerCount.html"
---

# LayerCount Property (IEModelViewControl)

Gets the number of layers in this eDrawings document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LayerCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

value = instance.LayerCount
```

### C#

```csharp
System.int LayerCount {get;}
```

### C++/CLI

```cpp
property System.int LayerCount {
   System.int get();
}
```

### Property Value

Number of layers

## VBA Syntax

See [EModelViewControl::LayerCount](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~LayerCount.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

Call this property before calling [IEModelViewControl::LayerName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~LayerName.html) to get the total number of the layers in this eDrawings document.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ShowLayer Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowLayer.html)

## Availability

eDrawings API 2007 SP0
