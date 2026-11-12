---
title: "Inspection Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "Inspection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Inspection.html"
---

# Inspection Property (IDisplayDimension)

Gets or sets whether a display dimension above the dimension line is displayed as an inspection dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property Inspection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.Inspection = value

value = instance.Inspection
```

### C#

```csharp
System.bool Inspection {get; set;}
```

### C++/CLI

```cpp
property System.bool Inspection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the display dimension above the dimension line is displayed as an inspection dimension, false if not

## VBA Syntax

See [DisplayDimension::Inspection](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~Inspection.html).

## Remarks

An inspection dimension is contained within an oval.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.html)
[IDisplayDimension::SetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.html)
[IDisplayDimension::LowerInspection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~LowerInspection.html)

## Availability

SOLIDWORKS 99, datecode 1999207
