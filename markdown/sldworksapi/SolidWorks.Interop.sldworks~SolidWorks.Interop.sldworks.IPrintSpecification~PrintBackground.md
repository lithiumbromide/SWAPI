---
title: "PrintBackground Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "PrintBackground"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintBackground.html"
---

# PrintBackground Property (IPrintSpecification)

Gets or sets whether to print the background.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrintBackground As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Boolean

instance.PrintBackground = value

value = instance.PrintBackground
```

### C#

```csharp
System.bool PrintBackground {get; set;}
```

### C++/CLI

```cpp
property System.bool PrintBackground {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to print the background, false to not

## VBA Syntax

See [PrintSpecification::PrintBackground](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~PrintBackground.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
