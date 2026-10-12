---
title: "PreIntersect2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "PreIntersect2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreIntersect2.html"
---

# PreIntersect2 Method (IFeatureManager)

Prepares an intersect feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function PreIntersect2( _
   ByVal CapPlanar As System.Boolean, _
   ByVal RegionType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim CapPlanar As System.Boolean
Dim RegionType As System.Integer
Dim value As System.Object

value = instance.PreIntersect2(CapPlanar, RegionType)
```

### C#

```csharp
System.object PreIntersect2(
   System.bool CapPlanar,
   System.int RegionType
)
```

### C++/CLI

```cpp
System.Object^ PreIntersect2(
   System.bool CapPlanar,
   System.int RegionType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CapPlanar`: True to cap the flat openings of surfaces to define closed volumes, false to not
- `RegionType`: Type of regions to create:

  - 0 = Intersecting regions
  - 1 = Internal regions
  - 2 = Intersecting and internal regions

### Return Value

Array of intersecting [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [FeatureManager::PreIntersect2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~PreIntersect2.html).

## Examples

[Create Intersect Feature (C#)](Create_Intersect_Feature_Example_CSharp.htm)
[Create Intersect Feature (VB.NET)](Create_Intersect_Feature_Example_VBNET.htm)
[Create Intersect Feature (VBA)](Create_Intersect_Feature_Example_VB.htm)

## Remarks

Before calling this method, you must select the intersecting [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html), [solids](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), or [planes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html) that make up the intersect feature.

After calling this method, call [IFeatureManager::PostIntersect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PostIntersect.html) to create the intersect feature.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
