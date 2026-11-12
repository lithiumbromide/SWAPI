---
title: "ResolutionControl Property (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "ResolutionControl"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ResolutionControl.html"
---

# ResolutionControl Property (IFillSurfaceFeatureData)

Gets and sets the quality of the resolution of the fill-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResolutionControl As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim value As System.Integer

instance.ResolutionControl = value

value = instance.ResolutionControl
```

### C#

```csharp
System.int ResolutionControl {get; set;}
```

### C++/CLI

```cpp
property System.int ResolutionControl {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Valid values: 1, 2, and 3 (see **Remarks**)

## VBA Syntax

See [FillSurfaceFeatureData::ResolutionControl](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~ResolutionControl.html).

## Examples

[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)

## Remarks

Adjusting the quality of the resolution is only available for patches that are not optimized. See [IFillSurfaceFeatureData::OptimizeSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~OptimizeSurface.html) for details.

Specifying a higher value:

- Increases the number of patches defining the surface
- Improves the quality of the surface profile
- Increases processing time
- Increases the size of the file

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
