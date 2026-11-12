---
title: "FlipDimension Property (IProfileCenterMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProfileCenterMateFeatureData"
member: "FlipDimension"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData~FlipDimension.html"
---

# FlipDimension Property (IProfileCenterMateFeatureData)

Gets or sets whether to move entities to opposite sides of the dimension of this profile center mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipDimension As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IProfileCenterMateFeatureData
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

See [ProfileCenterMateFeatureData::FlipDimension](ms-its:sldworksapivb6.chm::/sldworks~ProfileCenterMateFeatureData~FlipDimension.html).

## Examples

See the [IProfileCenterMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.html) examples.

## See Also

[IProfileCenterMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.html)
[IProfileCenterMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
