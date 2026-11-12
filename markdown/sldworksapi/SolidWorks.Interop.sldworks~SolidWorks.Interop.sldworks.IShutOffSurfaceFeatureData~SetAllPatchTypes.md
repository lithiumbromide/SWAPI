---
title: "SetAllPatchTypes Method (IShutOffSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShutOffSurfaceFeatureData"
member: "SetAllPatchTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.html"
---

# SetAllPatchTypes Method (IShutOffSurfaceFeatureData)

Sets the type of patch for all loops for this shut-off surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAllPatchTypes( _
   ByVal Type As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IShutOffSurfaceFeatureData
Dim Type As System.Integer

instance.SetAllPatchTypes(Type)
```

### C#

```csharp
void SetAllPatchTypes(
   System.int Type
)
```

### C++/CLI

```cpp
void SetAllPatchTypes(
   System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of patch as defined in [swShutOffSurfacePatchType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swShutOffSurfacePatchType_e.html)

## VBA Syntax

See [ShutOffSurfaceFeatureData::SetAllPatchTypes](ms-its:sldworksapivb6.chm::/sldworks~ShutOffSurfaceFeatureData~SetAllPatchTypes.html).

## See Also

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html)
[IShutOffSurfaceFeatureData::LoopPatchType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.html)
[IShutOffSurfaceFeatureData::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopCount.html)
[IShutOffSurfaceFeatureData::GetLoopEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopEdgeCount.html)
[IShutOffSurfaceFeatureData::IGetLoopEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetLoopEdges.html)
[IShutOffSurfaceFeatureData::LoopEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopEdges.html)
[IShutOffSurfaceFeatureData::Knit Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Knit.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
