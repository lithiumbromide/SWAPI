---
title: "OffsetDirections Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "OffsetDirections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OffsetDirections.html"
---

# OffsetDirections Property (IBaseFlangeFeatureData)

Gets or sets the number of offset directions for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetDirections As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Integer

instance.OffsetDirections = value

value = instance.OffsetDirections
```

### C#

```csharp
System.int OffsetDirections {get; set;}
```

### C++/CLI

```cpp
property System.int OffsetDirections {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of offset directions

## VBA Syntax

See [BaseFlangeFeatureData::OffsetDirections](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~OffsetDirections.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
