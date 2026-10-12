---
title: "DimensionPositionType Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "DimensionPositionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~DimensionPositionType.html"
---

# DimensionPositionType Property (IJogFeatureData)

Gets or sets the dimension position type for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimensionPositionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Integer

instance.DimensionPositionType = value

value = instance.DimensionPositionType
```

### C#

```csharp
System.int DimensionPositionType {get; set;}
```

### C++/CLI

```cpp
property System.int DimensionPositionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Dimension position type as defined in [swJogDimensionPositionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swJogDimensionPositionType_e.html)

## VBA Syntax

See [JogFeatureData::DimensionPositionType](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~DimensionPositionType.html).

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
