---
title: "IGetPatternedTransforms Method (ICThread)"
project: "SOLIDWORKS API Help"
interface: "ICThread"
member: "IGetPatternedTransforms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~IGetPatternedTransforms.html"
---

# IGetPatternedTransforms Method (ICThread)

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
Dim instance As ICThread
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

Call [ICThreadFeatureData::GetPatternedTransformsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~GetPatternedTransformsCount.html) before calling this method to determine the size of the output array.

The value returned by this method does not include this cosmetic thread, which is the seed feature and not an pattern instance. Therefore, if this cosmetic thread is not used in a pattern feature, then ICThreadFeatureData::GetPatternedTransformsCount returns 0 and this method returns an empty array.

## See Also

[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.html)
[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.html)
[ICThread::PatternedTransforms Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~PatternedTransforms.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
