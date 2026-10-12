---
title: "LoopCount Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "LoopCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~LoopCount.html"
---

# LoopCount Property (IChamferFeatureData2)

Gets the number of loops to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LoopCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Integer

value = instance.LoopCount
```

### C#

```csharp
System.int LoopCount {get;}
```

### C++/CLI

```cpp
property System.int LoopCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of loops

## VBA Syntax

See [ChamferFeatureData2::LoopCount](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~LoopCount.html).

## Remarks

Call this property before calling [IChamferFeatureData2::IGetLoops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~IGetLoops.html).

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::ISetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetLoops.html)
[IChamferFeatureData2::Loops Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Loops.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
