---
title: "GetFaceTangentTo Method (IShutOffSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShutOffSurfaceFeatureData"
member: "GetFaceTangentTo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetFaceTangentTo.html"
---

# GetFaceTangentTo Method (IShutOffSurfaceFeatureData)

Gets the tangent face for the specified loop where to create the patch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceTangentTo( _
   ByVal Index As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IShutOffSurfaceFeatureData
Dim Index As System.Integer
Dim value As Face2

value = instance.GetFaceTangentTo(Index)
```

### C#

```csharp
Face2 GetFaceTangentTo(
   System.int Index
)
```

### C++/CLI

```cpp
Face2^ GetFaceTangentTo(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index for the loop where to create the patch

### Return Value

[Tangent face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [ShutOffSurfaceFeatureData::GetFaceTangentTo](ms-its:sldworksapivb6.chm::/sldworks~ShutOffSurfaceFeatureData~GetFaceTangentTo.html).

## Remarks

This method is only available when the type of patch is set to swPatchTypeTangent. See [IShutOffSurfaceFeatureData::LoopPatchType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.html) and [IShutOffSurfaceFeatureData::SetAllPatchTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html)
[IShutOffSurfaceFeatureData::FlipFaceTangentTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~FlipFaceTangentTo.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
