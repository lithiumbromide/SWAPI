---
title: "LowerInspection Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "LowerInspection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~LowerInspection.html"
---

# LowerInspection Property (IDisplayDimension)

Gets or sets whether a display dimension below the dimension line is displayed as an inspection dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property LowerInspection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.LowerInspection = value

value = instance.LowerInspection
```

### C#

```csharp
System.bool LowerInspection {get; set;}
```

### C++/CLI

```cpp
property System.bool LowerInspection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the display dimension below the dimension is displayed as an inspection dimension, false if not

## VBA Syntax

See [DisplayDimension::LowerInspection](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~LowerInspection.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

## Remarks

An inspection dimension is contained within an oval.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLowerText.html)
[IDisplayDimension::SetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLowerText.html)
[IDisplayDimension::Inspection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Inspection.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
