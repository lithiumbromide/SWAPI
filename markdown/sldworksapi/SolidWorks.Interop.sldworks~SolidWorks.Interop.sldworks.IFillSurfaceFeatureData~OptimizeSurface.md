---
title: "OptimizeSurface Property (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "OptimizeSurface"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~OptimizeSurface.html"
---

# OptimizeSurface Property (IFillSurfaceFeatureData)

Gets or sets whether or not to optimize the patch.

## Syntax

### Visual Basic (Declaration)

```vb
Property OptimizeSurface As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim value As System.Boolean

instance.OptimizeSurface = value

value = instance.OptimizeSurface
```

### C#

```csharp
System.bool OptimizeSurface {get; set;}
```

### C++/CLI

```cpp
property System.bool OptimizeSurface {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for optimized patch, false for non-optimized patch

## VBA Syntax

See [FillSurfaceFeatureData::OptimizeSurface](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~OptimizeSurface.html).

## Examples

[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)

## Remarks

You can only adjust the quality of the resolution of a patch when the patch is not optimized. See [IFillSurfaceFeatureData::ResolutionControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~ResolutionControl.html) for details.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
