---
title: "CurrentSheet Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "CurrentSheet"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~CurrentSheet.html"
---

# CurrentSheet Property (IPrintSpecification)

Gets the index of the current sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentSheet As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Integer

value = instance.CurrentSheet
```

### C#

```csharp
System.int CurrentSheet {get;}
```

### C++/CLI

```cpp
property System.int CurrentSheet {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Index of current sheet

## VBA Syntax

See [PrintSpecification::CurrentSheet](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~CurrentSheet.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
