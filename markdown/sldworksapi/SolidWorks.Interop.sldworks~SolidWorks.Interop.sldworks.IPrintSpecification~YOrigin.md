---
title: "YOrigin Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "YOrigin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~YOrigin.html"
---

# YOrigin Property (IPrintSpecification)

Gets or sets the Y-coordinate of the print window origin.

## Syntax

### Visual Basic (Declaration)

```vb
Property YOrigin As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Double

instance.YOrigin = value

value = instance.YOrigin
```

### C#

```csharp
System.double YOrigin {get; set;}
```

### C++/CLI

```cpp
property System.double YOrigin {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Y-coordinate of the print window origin

## VBA Syntax

See [PrintSpecification::YOrigin](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~YOrigin.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
