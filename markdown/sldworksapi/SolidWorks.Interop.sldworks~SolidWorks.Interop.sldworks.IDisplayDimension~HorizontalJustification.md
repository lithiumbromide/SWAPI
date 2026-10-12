---
title: "HorizontalJustification Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "HorizontalJustification"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~HorizontalJustification.html"
---

# HorizontalJustification Property (IDisplayDimension)

Gets or sets the dimension text's horizontal justification.

## Syntax

### Visual Basic (Declaration)

```vb
Property HorizontalJustification As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

instance.HorizontalJustification = value

value = instance.HorizontalJustification
```

### C#

```csharp
System.int HorizontalJustification {get; set;}
```

### C++/CLI

```cpp
property System.int HorizontalJustification {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Horizontal justification as defined in [swTextJustification_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextJustification_e.html)

## VBA Syntax

See [DisplayDimension::HorizontalJustification](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~HorizontalJustification.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::VerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~VerticalJustification.html)
[IDisplayDimension::AddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayText.html)
[IDisplayDimension::IAddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
