---
title: "FlipDimension Property (IDistanceMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDistanceMateFeatureData"
member: "FlipDimension"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~FlipDimension.html"
---

# FlipDimension Property (IDistanceMateFeatureData)

Gets or sets whether to move entities to opposite sides of the dimension of this distance mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipDimension As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDistanceMateFeatureData
Dim value As System.Boolean

instance.FlipDimension = value

value = instance.FlipDimension
```

### C#

```csharp
System.bool FlipDimension {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipDimension {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the dimension, false to not

## VBA Syntax

See [DistanceMateFeatureData::FlipDimension](ms-its:sldworksapivb6.chm::/sldworks~DistanceMateFeatureData~FlipDimension.html).

## Examples

See the [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html) examples.

## See Also

[IDistanceMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html)
[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
