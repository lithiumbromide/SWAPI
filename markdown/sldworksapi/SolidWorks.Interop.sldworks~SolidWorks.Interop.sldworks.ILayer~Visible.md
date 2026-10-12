---
title: "Visible Property (ILayer)"
project: "SOLIDWORKS API Help"
interface: "ILayer"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Visible.html"
---

# Visible Property (ILayer)

Gets or sets the visibility of this layer.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILayer
Dim value As System.Boolean

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.bool Visible {get; set;}
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the layer is visible, false if the layer is not visible (see **Remarks**)

## VBA Syntax

See [Layer::Visible](ms-its:sldworksapivb6.chm::/sldworks~Layer~Visible.html).

## Examples

[Determine if Layer is Visible (VBA)](Determine_if_Layer_is_Visible_Example_VB.htm)
[Get Layers (C#)](Get_Layers_Example_CSharp.htm)
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## Remarks

After setting this property to the opposite state, call [ILayer::Printable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Printable.html) to check its state, because setting ILayer::Visible might change the state of ILayer::Printable.

To ensure that ILayer::Visible and ILayer::Printable are set to the desired states, perform the following steps in this order:

1. Set ILayer::Visible.
2. Get the state of ILayer::Printable.
3. Set ILayer::Printable if necessary.

## See Also

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.html)
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.html)

## Availability

SOLIDWORKS 99 SP6, datecode 1999355
