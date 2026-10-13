---
title: "BothDirections Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "BothDirections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~BothDirections.html"
---

# BothDirections Property (IExtrudeFeatureData2)

Gets or sets whether the extrusion is in both directions.

## Syntax

### Visual Basic (Declaration)

```vb
Property BothDirections As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean

instance.BothDirections = value

value = instance.BothDirections
```

### C#

```csharp
System.bool BothDirections {get; set;}
```

### C++/CLI

```cpp
property System.bool BothDirections {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if extrusion is in both directions, false if not

## VBA Syntax

See [ExtrudeFeatureData2::BothDirections](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~BothDirections.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
