---
title: "ChamferTextStyle Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ChamferTextStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ChamferTextStyle.html"
---

# ChamferTextStyle Property (IDisplayDimension)

Gets or sets the text style for chamfer dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Property ChamferTextStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

instance.ChamferTextStyle = value

value = instance.ChamferTextStyle
```

### C#

```csharp
System.int ChamferTextStyle {get; set;}
```

### C++/CLI

```cpp
property System.int ChamferTextStyle {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text style for chamfer dimensions only as defined by [swDetailingChamferDimLeaderTextStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetailingChamferDimLeaderTextStyle_e.html)

## VBA Syntax

See [DisplayDimension::ChamferTextStyle](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ChamferTextStyle.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
