---
title: "ISetLoops Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ISetLoops"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetLoops.html"
---

# ISetLoops Method (ISimpleFilletFeatureData2)

Sets the loops on which to put a simple radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetLoops( _
   ByVal Count As System.Integer, _
   ByRef LoopList As Loop2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim Count As System.Integer
Dim LoopList As Loop2

instance.ISetLoops(Count, LoopList)
```

### C#

```csharp
void ISetLoops(
   System.int Count,
   ref Loop2 LoopList
)
```

### C++/CLI

```cpp
void ISetLoops(
   System.int Count,
   Loop2^% LoopList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of loops
- `LoopList`: - in-process, unmanaged C++: Pointer to an array of [loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html) of size Count
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetLoopCount.html)
[ISimpleFilletFeatureData2::IGetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetLoops.html)
[ISimpleFilletFeatureData2::Loops Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Loops.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
