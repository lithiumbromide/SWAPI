---
title: "IGetPatternedTransforms Method (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "IGetPatternedTransforms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~IGetPatternedTransforms.html"
---

# IGetPatternedTransforms Method (ICosmeticThreadFeatureData)

Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPatternedTransforms( _
   ByVal Count As System.Integer _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim Count As System.Integer
Dim value As MathTransform

value = instance.IGetPatternedTransforms(Count)
```

### C#

```csharp
MathTransform IGetPatternedTransforms(
   System.int Count
)
```

### C++/CLI

```cpp
MathTransform^ IGetPatternedTransforms(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Size of the output array (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of interface pointers to the [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) objects of the instances of this cosmetic thread

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ICosmeticThreadFeatureData::GetPatternedTransformsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData~GetPatternedTransformsCount.html) before calling this method to determine the size of the output array.

The value returned by this method does not include this cosmetic thread, which is the seed feature and not a pattern instance. Therefore, if this cosmetic thread is not used in a pattern feature, then ICosmeticThreadFeatureData::GetPatternedTransformsCount returns 0 and nothing is put into the output array.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)
[ICosmeticThreadFeatureData::PatternedTransforms Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~PatternedTransforms.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
