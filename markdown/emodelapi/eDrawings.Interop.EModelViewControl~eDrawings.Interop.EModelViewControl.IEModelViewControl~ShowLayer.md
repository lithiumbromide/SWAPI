---
title: "ShowLayer Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ShowLayer"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowLayer.html"
---

# ShowLayer Property (IEModelViewControl)

Gets or sets the layer to show.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowLayer( _
   ByVal LayerName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim LayerName As System.String
Dim value As System.Boolean

instance.ShowLayer(LayerName) = value

value = instance.ShowLayer(LayerName)
```

### C#

```csharp
System.bool ShowLayer(
   System.string LayerName
) {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowLayer {
   System.bool get(System.String^ LayerName);
   void set (System.String^ LayerName, System.bool value);
}
```

### Parameters

- `LayerName`: Name of layer to show (see Remarks)

### Property Value

True if the layer is shown, false if not

## VBA Syntax

See [EModelViewControl::ShowLayer](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ShowLayer.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

Before calling this method, call [IEModelViewControl::LayerName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~LayerName.html) to get the name of the layer to show.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::LayerCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~LayerCount.html)

## Availability

eDrawings API 2007 SP0
