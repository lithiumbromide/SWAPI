---
title: "SheetCount Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "SheetCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~SheetCount.html"
---

# SheetCount Property (IPrintSpecification)

Gets the number of sheets in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SheetCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Integer

value = instance.SheetCount
```

### C#

```csharp
System.int SheetCount {get;}
```

### C++/CLI

```cpp
property System.int SheetCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of sheets

## VBA Syntax

See [PrintSpecification::SheetCount](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~SheetCount.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
