---
title: "VerticalJustification Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "VerticalJustification"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~VerticalJustification.html"
---

# VerticalJustification Property (IDisplayDimension)

Gets the dimension text's vertical justification.

## Syntax

### Visual Basic (Declaration)

```vb
Property VerticalJustification As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

instance.VerticalJustification = value

value = instance.VerticalJustification
```

### C#

```csharp
System.int VerticalJustification {get; set;}
```

### C++/CLI

```cpp
property System.int VerticalJustification {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Vertical justification as defined in [swVerticalJustification_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swVerticalJustification_e.html)

## VBA Syntax

See [DisplayDimension::VerticalJustification](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~VerticalJustification.html).

## Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::HorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~HorizontalJustification.html)
[IDisplayDimension::AddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayText.html)
[IDisplayDimension::IAddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
