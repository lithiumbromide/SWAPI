---
title: "PrintWhiteItemsBlack Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "PrintWhiteItemsBlack"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintWhiteItemsBlack.html"
---

# PrintWhiteItemsBlack Property (IPrintSpecification)

Gets or sets whether to print white lines and white text in black.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrintWhiteItemsBlack As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Boolean

instance.PrintWhiteItemsBlack = value

value = instance.PrintWhiteItemsBlack
```

### C#

```csharp
System.bool PrintWhiteItemsBlack {get; set;}
```

### C++/CLI

```cpp
property System.bool PrintWhiteItemsBlack {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to print white lines and white text in black

## VBA Syntax

See [PrintSpecification::PrintWhiteItemsBlack](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~PrintWhiteItemsBlack.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
