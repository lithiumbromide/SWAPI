---
title: "LoopPatchType Property (IShutOffSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShutOffSurfaceFeatureData"
member: "LoopPatchType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.html"
---

# LoopPatchType Property (IShutOffSurfaceFeatureData)

Gets and sets the type of patch for the specified loop for this shut-off surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property LoopPatchType( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IShutOffSurfaceFeatureData
Dim Index As System.Integer
Dim value As System.Integer

instance.LoopPatchType(Index) = value

value = instance.LoopPatchType(Index)
```

### C#

```csharp
System.int LoopPatchType(
   System.int Index
) {get; set;}
```

### C++/CLI

```cpp
property System.int LoopPatchType {
   System.int get(System.int Index);
   void set (System.int Index, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the loop for which to set the type of patch

### Property Value

Type of patch as defined in [swShutOffSurfacePatchType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swShutOffSurfacePatchType_e.html)

## VBA Syntax

See [ShutOffSurfaceFeatureData::LoopPatchType](ms-its:sldworksapivb6.chm::/sldworks~ShutOffSurfaceFeatureData~LoopPatchType.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html)
[IShutOffSurfaceFeatureData::SetAllPatchTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.html)
[IShutOffSurfaceFeatureData::Knit Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Knit.html)
[IShutOffSurfaceFeatureData::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopCount.html)
[IShutOffSurfaceFeatureData::GetLoopEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetLoopEdgeCount.html)
[IShutOffSurfaceFeatureData::IGetLoopEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~IGetLoopEdges.html)
[IShutOffSurfaceFeatureData::LoopEdges Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopEdges.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
