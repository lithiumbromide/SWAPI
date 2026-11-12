---
title: "ArcRadius Property (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "ArcRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~ArcRadius.html"
---

# ArcRadius Property (IRevisionCloud)

Gets or sets the maximum arc radius of this revision cloud annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Property ArcRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim value As System.Double

instance.ArcRadius = value

value = instance.ArcRadius
```

### C#

```csharp
System.double ArcRadius {get; set;}
```

### C++/CLI

```cpp
property System.double ArcRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum arc radius

## VBA Syntax

See [RevisionCloud::ArcRadius](ms-its:sldworksapivb6.chm::/sldworks~RevisionCloud~ArcRadius.html).

## Examples

See [IRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html) examples.

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
