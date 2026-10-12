---
title: "PreIntersect Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "PreIntersect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreIntersect.html"
---

# PreIntersect Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::PreIntersect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreIntersect2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function PreIntersect( _
   ByVal CapPlanar As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim CapPlanar As System.Boolean
Dim value As System.Object

value = instance.PreIntersect(CapPlanar)
```

### C#

```csharp
System.object PreIntersect(
   System.bool CapPlanar
)
```

### C++/CLI

```cpp
System.Object^ PreIntersect(
   System.bool CapPlanar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CapPlanar`: True to cap the flat openings of surfaces to define closed volumes, false to not

### Return Value

Array of intersect [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [FeatureManager::PreIntersect](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~PreIntersect.html).

## Examples

[Get Intersect Feature Data (VBA)](Get_Intersect_Feature_Data_Example_VB.htm)
[Get Intersect Feature Data (VB.NET)](Get_Intersect_Feature_Data_Example_VBNET.htm)
[Get Intersect Feature Data (C#)](Get_Intersect_Feature_Data_Example_CSharp.htm)

## Remarks

Before calling this method, you must select the intersecting [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html), [solids](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), or [planes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html) that make up the intersect feature.

After calling this method, call [IFeatureManager::PostIntersect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PostIntersect.html) to create the intersect feature.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
