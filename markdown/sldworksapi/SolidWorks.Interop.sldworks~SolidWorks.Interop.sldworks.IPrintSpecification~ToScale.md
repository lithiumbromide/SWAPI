---
title: "ToScale Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "ToScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ToScale.html"
---

# ToScale Property (IPrintSpecification)

Gets or sets the custom "to" scale factor for the current drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Double

instance.ToScale = value

value = instance.ToScale
```

### C#

```csharp
System.double ToScale {get; set;}
```

### C++/CLI

```cpp
property System.double ToScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

"To" scale factor in the From:To scale

## VBA Syntax

See [PrintSpecification::ToScale](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~ToScale.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## Remarks

This property is valid only if [IPrintSpecification::ScaleMethod](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ScaleMethod.html) is set to [swPrintSelectionScaleFactor_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrintSelectionScaleFactor_e.html).swPrintSelection.

For details about applying a scale factor to the current drawing sheet, see the **Print Specification** Help topic in the SOLIDWORKS Help.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)
[IPrintSpecification::FromScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~FromScale.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
