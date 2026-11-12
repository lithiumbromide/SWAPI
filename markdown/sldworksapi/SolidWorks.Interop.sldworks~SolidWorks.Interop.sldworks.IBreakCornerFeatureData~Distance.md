---
title: "Distance Property (IBreakCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBreakCornerFeatureData"
member: "Distance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~Distance.html"
---

# Distance Property (IBreakCornerFeatureData)

Gets or sets the chamfer length or fillet radius, depending on the break corner type.

## Syntax

### Visual Basic (Declaration)

```vb
Property Distance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakCornerFeatureData
Dim value As System.Double

instance.Distance = value

value = instance.Distance
```

### C#

```csharp
System.double Distance {get; set;}
```

### C++/CLI

```cpp
property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Chamfer length or fillet radius

## VBA Syntax

See [BreakCornerFeatureData::Distance](ms-its:sldworksapivb6.chm::/sldworks~BreakCornerFeatureData~Distance.html).

## See Also

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.html)
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
