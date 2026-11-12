---
title: "ConvertToHighQuality Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "ConvertToHighQuality"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ConvertToHighQuality.html"
---

# ConvertToHighQuality Property (IPrintSpecification)

Gets or sets whether to convert draft quality drawing views to high quality.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConvertToHighQuality As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Boolean

instance.ConvertToHighQuality = value

value = instance.ConvertToHighQuality
```

### C#

```csharp
System.bool ConvertToHighQuality {get; set;}
```

### C++/CLI

```cpp
property System.bool ConvertToHighQuality {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to convert to high quality, false to not

## VBA Syntax

See [PrintSpecification::ConvertToHighQuality](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~ConvertToHighQuality.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
