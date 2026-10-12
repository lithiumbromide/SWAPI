---
title: "MarkedForDrawing Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "MarkedForDrawing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~MarkedForDrawing.html"
---

# MarkedForDrawing Property (IDisplayDimension)

Gets or sets whether this display dimension is marked to include in a drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Property MarkedForDrawing As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.MarkedForDrawing = value

value = instance.MarkedForDrawing
```

### C#

```csharp
System.bool MarkedForDrawing {get; set;}
```

### C++/CLI

```cpp
property System.bool MarkedForDrawing {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the display dimension is marked to include in the drawing document, false if not

## VBA Syntax

See [DisplayDimension::MarkedForDrawing](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~MarkedForDrawing.html).

## Examples

[Determine if Display Dimension Marked for Drawing (VBA)](Determine_if_Display_Dimension_Marked_for_Drawing_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
