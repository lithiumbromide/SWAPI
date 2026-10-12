---
title: "PreserveZAxis Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "PreserveZAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PreserveZAxis.html"
---

# PreserveZAxis Property (IMirrorComponentFeatureData)

Gets or sets whether to preserve the orientation of the Z-axis in the opposite-hand versions.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreserveZAxis As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean

instance.PreserveZAxis = value

value = instance.PreserveZAxis
```

### C#

```csharp
System.bool PreserveZAxis {get; set;}
```

### C++/CLI

```cpp
property System.bool PreserveZAxis {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to preserve the orientation of the Z-axis, false to not

## VBA Syntax

See [MirrorComponentFeatureData::PreserveZAxis](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~PreserveZAxis.html).

## Examples

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html) example.

## Remarks

This property is valid only if [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.html) is false.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
