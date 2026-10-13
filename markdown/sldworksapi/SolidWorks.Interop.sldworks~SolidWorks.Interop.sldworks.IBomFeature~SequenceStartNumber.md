---
title: "SequenceStartNumber Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "SequenceStartNumber"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SequenceStartNumber.html"
---

# SequenceStartNumber Property (IBomFeature)

Gets or sets the number with which to start the numbering for this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Property SequenceStartNumber As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Integer

instance.SequenceStartNumber = value

value = instance.SequenceStartNumber
```

### C#

```csharp
System.int SequenceStartNumber {get; set;}
```

### C++/CLI

```cpp
property System.int SequenceStartNumber {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number with which to start the numbering

## VBA Syntax

See [BomFeature::SequenceStartNumber](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~SequenceStartNumber.html).

## Examples

See [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) examples.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
