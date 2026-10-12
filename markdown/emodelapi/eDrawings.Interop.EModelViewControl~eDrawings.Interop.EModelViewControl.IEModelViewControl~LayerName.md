---
title: "LayerName Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "LayerName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~LayerName.html"
---

# LayerName Property (IEModelViewControl)

Gets the name of the specified layer in this eDrawings document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LayerName( _
   ByVal LayerIndex As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim LayerIndex As System.Integer
Dim value As System.String

value = instance.LayerName(LayerIndex)
```

### C#

```csharp
System.string LayerName(
   System.int LayerIndex
) {get;}
```

### C++/CLI

```cpp
property System.String^ LayerName {
   System.String^ get(System.int LayerIndex);
}
```

### Parameters

- `LayerIndex`: Number of the layer whose name to get (see Remarks)

### Property Value

Name of specified layer

## VBA Syntax

See [EModelViewControl::LayerName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~LayerName.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

Before calling this property, call [IEModelViewControl::LayerCount](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~LayerCount.html) to get the total number of layers in this eDrawings document.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ShowLayer Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowLayer.html)

## Availability

eDrawings API 2007 SP0
