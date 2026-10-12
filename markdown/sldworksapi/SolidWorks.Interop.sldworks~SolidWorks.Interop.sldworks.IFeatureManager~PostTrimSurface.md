---
title: "PostTrimSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "PostTrimSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostTrimSurface.html"
---

# PostTrimSurface Method (IFeatureManager)

Sets whether to sew the resulting trimmed surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Function PostTrimSurface( _
   ByVal BSewSurfaceIn As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BSewSurfaceIn As System.Boolean
Dim value As Feature

value = instance.PostTrimSurface(BSewSurfaceIn)
```

### C#

```csharp
Feature PostTrimSurface(
   System.bool BSewSurfaceIn
)
```

### C++/CLI

```cpp
Feature^ PostTrimSurface(
   System.bool BSewSurfaceIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BSewSurfaceIn`: True to sew the resulting trimmed surfaces, false to not

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::PostTrimSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~PostTrimSurface.html).

## Examples

[Create Trimmed Surface Feature (C#)](Create_Trimmed_Surface_Feature_Example_CSharp.htm)
[Create Trimmed Surface Feature (VB.NET)](Create_Trimmed_Surface_Feature_Example_VBNET.htm)
[Create Trimmed Surface Feature (VBA)](Create_Trimmed_Surface_Feature_Example_VB.htm)
[Create Solid Body Surface Trim Feature (C#)](Create_Solid_Body_Surface_Trim_Feature_Example_CSharp.htm)
[Create Solid Body Surface Trim Feature (VB.NET)](Create_Solid_Body_Surface_Trim_Feature_Example_VBNET.htm)
[Create Solid Body Surface Trim Feature (VBA)](Create_Solid_Body_Surface_Trim_Feature_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IFeatureManager::PreTrimSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreTrimSurface.html).
2. Select the trimming surfaces or trim tool.
3. Optionally, call [IFeatureManager::SolidForTrim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SolidForTrim.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
