---
title: "Scale2 Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "Scale2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Scale2.html"
---

# Scale2 Property (IDisplayDimension)

Gets or sets the scale value that is applied to the dimension value of this non-associative distance dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Double

instance.Scale2 = value

value = instance.Scale2
```

### C#

```csharp
System.double Scale2 {get; set;}
```

### C++/CLI

```cpp
property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Scale applied to the dimension value

## VBA Syntax

See [DisplayDimension::Scale2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~Scale2.html).

## Remarks

This scale value applies only to non-associative distance dimensions, such as those created using [IDrawingDoc::CreateLinearDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateLinearDim4.html) or [IDrawingDoc::CreateDiamDim4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateDiamDim4.html). For these dimensions, SOLIDWORKS multiplies the actual dimension measurement by this scale value to get the dimension value that is displayed on the screen. For any other types of dimensions (such as associative dimensions or angular measurement dimensions), setting the scale factor has no effect and getting the scale factor will always return 1.

The scale value must be greater than 0. This has no effect in the OLE interface, and returns S_false in the COM interface.

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
