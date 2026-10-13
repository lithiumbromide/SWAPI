---
title: "ScaleMethod Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "ScaleMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ScaleMethod.html"
---

# ScaleMethod Property (IPrintSpecification)

Gets or sets the page selection option for printing.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Integer

instance.ScaleMethod = value

value = instance.ScaleMethod
```

### C#

```csharp
System.int ScaleMethod {get; set;}
```

### C++/CLI

```cpp
property System.int ScaleMethod {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Page selection option as defined in [swPrintSelectionScaleFactor_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrintSelectionScaleFactor_e.html)

## VBA Syntax

See [PrintSpecification::ScaleMethod](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~ScaleMethod.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## Remarks

For details about applying a scale factor to the current drawing sheet, see the **Print Specification** Help topic in the SOLIDWORKS Help.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
