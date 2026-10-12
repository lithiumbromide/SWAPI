---
title: "GetPatternedTransformsCount Method (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "GetPatternedTransformsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~GetPatternedTransformsCount.html"
---

# GetPatternedTransformsCount Method (ICosmeticThreadFeatureData)

Gets the number of instances of this cosmetic thread that are patterns of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternedTransformsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.Integer

value = instance.GetPatternedTransformsCount()
```

### C#

```csharp
System.int GetPatternedTransformsCount()
```

### C++/CLI

```cpp
System.int GetPatternedTransformsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of instances of this cosmetic thread that are patterns of this feature

## VBA Syntax

See [CosmeticThreadFeatureData::GetPatternedTransformsCount](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~GetPatternedTransformsCount.html).

## Examples

[Get Cosmetic Threads Features in a Part (VBA)](Get_Cosmetic_Threads_in_a_Part_Document_Example_VB.htm)

## Remarks

The value returned by this method does not include this cosmetic thread, which is the seed feature and not an instance of the pattern. Therefore, if this cosmetic thread is not used in any pattern feature, then this method returns 0.

Use this method before using [ICosmeticThreadFeatureData::IGetPatternedTransforms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData~IGetPatternedTransforms.html) to determine the size of the array to pass to that method.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)
[ICosmeticThreadFeatureData::PatternedTransforms Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~PatternedTransforms.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
