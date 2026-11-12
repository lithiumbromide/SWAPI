---
title: "PatternedTransforms Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "PatternedTransforms"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~PatternedTransforms.html"
---

# PatternedTransforms Property (ICosmeticThreadFeatureData)

Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternedTransforms As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.Object

value = instance.PatternedTransforms
```

### C#

```csharp
System.object PatternedTransforms {get;}
```

### C++/CLI

```cpp
property System.Object^ PatternedTransforms {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of the transforms of the instances of this cosmetic thread

## VBA Syntax

See [CosmeticThreadFeatureData::PatternedTransforms](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~PatternedTransforms.html).

## Examples

[Get Cosmetic Threads Features in a Part (VBA)](Get_Cosmetic_Threads_in_a_Part_Document_Example_VB.htm)

## Remarks

The value returned by this property does not include this cosmetic thread, which is the seed feature and not a pattern instance. Therefore, if this cosmetic thread is not used in a pattern feature, then [ICosmeticThreadFeatureData::GetPatternedTransformsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData~GetPatternedTransformsCount.html) returns 0 and this property returns an empty array.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)
[ICosmeticThreadFeatureData::IGetPatternedTransforms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~IGetPatternedTransforms.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
