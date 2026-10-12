---
title: "PatternedTransforms Property (ICThread)"
project: "SOLIDWORKS API Help"
interface: "ICThread"
member: "PatternedTransforms"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~PatternedTransforms.html"
---

# PatternedTransforms Property (ICThread)

Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternedTransforms As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICThread
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

Array of [transforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html) for the instances of this cosmetic thread

## VBA Syntax

See [CThread::PatternedTransforms](ms-its:sldworksapivb6.chm::/sldworks~CThread~PatternedTransforms.html).

## Examples

[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

## Remarks

The value returned by this property does not include this cosmetic thread, which is the seed feature and not an pattern instance. Therefore, if this cosmetic thread is not used in a pattern feature, then [ICThreadFeatureData::GetTransformsPatternedCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~GetPatternedTransformsCount.html) returns 0 and this property returns an empty array.

## See Also

[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.html)
[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
