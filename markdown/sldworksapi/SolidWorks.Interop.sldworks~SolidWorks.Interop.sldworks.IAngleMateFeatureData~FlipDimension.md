---
title: "FlipDimension Property (IAngleMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAngleMateFeatureData"
member: "FlipDimension"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~FlipDimension.html"
---

# FlipDimension Property (IAngleMateFeatureData)

Gets or sets whether to move entities to opposite sides of the dimension in this angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipDimension As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAngleMateFeatureData
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

See [AngleMateFeatureData::FlipDimension](ms-its:sldworksapivb6.chm::/sldworks~AngleMateFeatureData~FlipDimension.html).

## Examples

See the [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html) examples.

## See Also

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html)
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
