---
title: "FromScale Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "FromScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~FromScale.html"
---

# FromScale Property (IPrintSpecification)

Gets or sets the custom "from" scale factor for the current drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property FromScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Double

instance.FromScale = value

value = instance.FromScale
```

### C#

```csharp
System.double FromScale {get; set;}
```

### C++/CLI

```cpp
property System.double FromScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

"From" scale factor in the From:To scale

## VBA Syntax

See [PrintSpecification::FromScale](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~FromScale.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## Remarks

This property is valid only if [IPrintSpecification::ScaleMethod](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ScaleMethod.html) is set to [swPrintSelectionScaleFactor_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrintSelectionScaleFactor_e.html).swPrintSelection.

For details about applying a scale factor to the current drawing sheet, see the **Print Specification** Help topic in the SOLIDWORKS Help.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)
[IPrintSpecification::ToScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ToScale.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
