---
title: "XOrigin Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "XOrigin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~XOrigin.html"
---

# XOrigin Property (IPrintSpecification)

Gets or sets the X-coordinate of the print window origin.

## Syntax

### Visual Basic (Declaration)

```vb
Property XOrigin As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Double

instance.XOrigin = value

value = instance.XOrigin
```

### C#

```csharp
System.double XOrigin {get; set;}
```

### C++/CLI

```cpp
property System.double XOrigin {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

X-coordinate of the print window origin

## VBA Syntax

See [PrintSpecification::XOrigin](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~XOrigin.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)
[IPrintSpecification::YOrigin Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~YOrigin.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
