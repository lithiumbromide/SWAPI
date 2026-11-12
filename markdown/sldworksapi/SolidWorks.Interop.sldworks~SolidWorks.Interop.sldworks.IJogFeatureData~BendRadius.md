---
title: "BendRadius Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "BendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~BendRadius.html"
---

# BendRadius Property (IJogFeatureData)

Gets or sets the bend radius for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Double

instance.BendRadius = value

value = instance.BendRadius
```

### C#

```csharp
System.double BendRadius {get; set;}
```

### C++/CLI

```cpp
property System.double BendRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [JogFeatureData::BendRadius](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~BendRadius.html).

## Examples

See [IJogFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJogFeatureData.html) examples.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::UseDefaultBendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~UseDefaultBendRadius.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.0
