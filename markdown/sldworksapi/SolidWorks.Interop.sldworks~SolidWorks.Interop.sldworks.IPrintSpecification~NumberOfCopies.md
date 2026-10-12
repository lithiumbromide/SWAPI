---
title: "NumberOfCopies Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "NumberOfCopies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~NumberOfCopies.html"
---

# NumberOfCopies Property (IPrintSpecification)

Gets or sets the number of copies to print.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfCopies As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Integer

instance.NumberOfCopies = value

value = instance.NumberOfCopies
```

### C#

```csharp
System.int NumberOfCopies {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfCopies {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of copies to print

## VBA Syntax

See [PrintSpecification::NumberOfCopies](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~NumberOfCopies.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
