---
title: "Foreshortened Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "Foreshortened"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Foreshortened.html"
---

# Foreshortened Property (IDisplayDimension)

Gets or sets whether a linear dimension is foreshortened in a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Property Foreshortened As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.Foreshortened = value

value = instance.Foreshortened
```

### C#

```csharp
System.bool Foreshortened {get; set;}
```

### C++/CLI

```cpp
property System.bool Foreshortened {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the linear dimension is foreshortened, false if not

## VBA Syntax

See [DisplayDimension::Foreshortened](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~Foreshortened.html).

## Examples

[Get Whether Linear Dimension Is Foreshortened (C#)](Get_Whether_Linear_Dimension_Is_Foreshortened_Example_CSharp.htm)
[Get Whether Linear Dimension Is Foreshortened (VB.NET)](Get_Whether_Linear_Dimension_Is_Foreshortened_Example_VBNET.htm)
[Get Whether Linear Dimension Is Foreshortened (VBA)](Get_Whether_Linear_Dimension_Is_Foreshortened_Example_VB.htm)

## Remarks

This property is only valid for linear dimensions and only when the detailing standard is ANSI.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::DisplayAsLinear Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsLinear.html)
[IModelDoc2::AddDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
