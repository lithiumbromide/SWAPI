---
title: "GetPatternedTransformsCount Method (ICThread)"
project: "SOLIDWORKS API Help"
interface: "ICThread"
member: "GetPatternedTransformsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetPatternedTransformsCount.html"
---

# GetPatternedTransformsCount Method (ICThread)

Gets the number of instances of this cosmetic thread that are patterns of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternedTransformsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICThread
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

See [CThread::GetPatternedTransformsCount](ms-its:sldworksapivb6.chm::/sldworks~CThread~GetPatternedTransformsCount.html).

## Examples

[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

## Remarks

The value returned by this method does not include this cosmetic thread, which is the seed feature and not an instance of the pattern. Therefore, if this cosmetic thread is not used in any pattern feature, then this method returns 0.

Use this method before using [ICThread::IGetPatternedTransforms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~IGetPatternedTransforms.html) to determine the size of the array to pass to that method.

## See Also

[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.html)
[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.html)
[ICThread::PatternedTransforms Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~PatternedTransforms.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
