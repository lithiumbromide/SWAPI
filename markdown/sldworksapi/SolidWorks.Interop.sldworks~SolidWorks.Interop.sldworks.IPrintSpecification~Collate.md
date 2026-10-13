---
title: "Collate Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "Collate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~Collate.html"
---

# Collate Property (IPrintSpecification)

Gets or sets whether to collate the pages in multiple copies of this document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Collate As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Boolean

instance.Collate = value

value = instance.Collate
```

### C#

```csharp
System.bool Collate {get; set;}
```

### C++/CLI

```cpp
property System.bool Collate {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to collate pages in multiple copies, false to not

## VBA Syntax

See [PrintSpecification::Collate](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~Collate.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
