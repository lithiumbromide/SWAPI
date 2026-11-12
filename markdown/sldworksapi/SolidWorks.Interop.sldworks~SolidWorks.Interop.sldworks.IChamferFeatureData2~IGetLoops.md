---
title: "IGetLoops Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "IGetLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetLoops.html"
---

# IGetLoops Method (IChamferFeatureData2)

Gets the loops to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLoops( _
   ByVal Count As System.Integer _
) As Loop
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Count As System.Integer
Dim value As Loop

value = instance.IGetLoops(Count)
```

### C#

```csharp
Loop IGetLoops(
   System.int Count
)
```

### C++/CLI

```cpp
Loop^ IGetLoops(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of loops

### Return Value

- in-process, unmanaged C++: Pointer to an array of [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IChamferFeatureData2::LoopCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~LoopCount.html) before calling this method.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::ISetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetLoops.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
