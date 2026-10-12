---
title: "ISetLoops Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "ISetLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetLoops.html"
---

# ISetLoops Method (IChamferFeatureData2)

Sets the loops to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetLoops( _
   ByVal Count As System.Integer, _
   ByRef LoopList As Loop _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Count As System.Integer
Dim LoopList As Loop

instance.ISetLoops(Count, LoopList)
```

### C#

```csharp
void ISetLoops(
   System.int Count,
   ref Loop LoopList
)
```

### C++/CLI

```cpp
void ISetLoops(
   System.int Count,
   Loop^% LoopList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of loops
- `LoopList`: - in-process, unmanaged C++: Pointer to an array of [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::IGetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetLoops.html)
[IChamferFeatureData2::Loops Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Loops.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
