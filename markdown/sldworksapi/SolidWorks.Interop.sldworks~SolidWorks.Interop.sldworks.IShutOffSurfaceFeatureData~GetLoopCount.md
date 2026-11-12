---
title: "GetLoopCount Method (IShutOffSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShutOffSurfaceFeatureData"
member: "GetLoopCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopCount.html"
---

# GetLoopCount Method (IShutOffSurfaceFeatureData)

Gets the number of closed loops for all of the patches.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLoopCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IShutOffSurfaceFeatureData
Dim value As System.Integer

value = instance.GetLoopCount()
```

### C#

```csharp
System.int GetLoopCount()
```

### C++/CLI

```cpp
System.int GetLoopCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of loops for the patches

## VBA Syntax

See [ShutOffSurfaceFeatureData::GetLoopCount](ms-its:sldworksapivb6.chm::/sldworks~ShutOffSurfaceFeatureData~GetLoopCount.html).

## Examples

See [IShutOffSurfaceFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShutOffSurfaceFeatureData.html) examples.

## Remarks

Call this method before calling [IShutOffSurfaceFeatureData::IGetEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShutOffSurfaceFeatureData~IGetEdges.html) to get the size of the array for that method.

## See Also

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html)
[IShutOffSurfaceFeatureData::GetLoopEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopEdgeCount.html)
[IShutOffSurfaceFeatureData::IGetLoopEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetLoopEdges.html)
[IShutOffSurfaceFeatureData::LoopEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopEdges.html)
[IShutOffSurfaceFeatureData::LoopPatchType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.html)
[IShutOffSurfaceFeatureData::SetAllPatchTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
