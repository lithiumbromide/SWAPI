---
title: "FlipFaceTangentTo Method (IShutOffSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShutOffSurfaceFeatureData"
member: "FlipFaceTangentTo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~FlipFaceTangentTo.html"
---

# FlipFaceTangentTo Method (IShutOffSurfaceFeatureData)

Indicates to create the patch on the opposite tangent face.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FlipFaceTangentTo( _
   ByVal Index As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IShutOffSurfaceFeatureData
Dim Index As System.Integer

instance.FlipFaceTangentTo(Index)
```

### C#

```csharp
void FlipFaceTangentTo(
   System.int Index
)
```

### C++/CLI

```cpp
void FlipFaceTangentTo(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the loop to use to create the patch

## VBA Syntax

See [ShutOffSurfaceFeatureData::FlipFaceTangentTo](ms-its:sldworksapivb6.chm::/sldworks~ShutOffSurfaceFeatureData~FlipFaceTangentTo.html).

## Examples

See [IShutOffSurfaceFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShutOffSurfaceFeatureData.html) examples.

## Remarks

This method is only available when the type of patch is set to swPatchTypeTangent. See [IShutOffSurfaceFeatureData::LoopPatchType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.html) and [IShutOffSurfaceFeatureData::SetAllPatchTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.html).

## See Also

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html)
[IShutOffSurfaceFeatureData::GetFaceTangentTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetFaceTangentTo.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
