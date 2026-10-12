---
title: "PreTrimSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "PreTrimSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreTrimSurface.html"
---

# PreTrimSurface Method (IFeatureManager)

Sets the trimming options before trimming a surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function PreTrimSurface( _
   ByVal BMutualTrimIn As System.Boolean, _
   ByVal BSplitSystemIn As System.Boolean, _
   ByVal BSplitLinearIn As System.Boolean, _
   ByVal BRemovePickedIn As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BMutualTrimIn As System.Boolean
Dim BSplitSystemIn As System.Boolean
Dim BSplitLinearIn As System.Boolean
Dim BRemovePickedIn As System.Boolean
Dim value As System.Boolean

value = instance.PreTrimSurface(BMutualTrimIn, BSplitSystemIn, BSplitLinearIn, BRemovePickedIn)
```

### C#

```csharp
System.bool PreTrimSurface(
   System.bool BMutualTrimIn,
   System.bool BSplitSystemIn,
   System.bool BSplitLinearIn,
   System.bool BRemovePickedIn
)
```

### C++/CLI

```cpp
System.bool PreTrimSurface(
   System.bool BMutualTrimIn,
   System.bool BSplitSystemIn,
   System.bool BSplitLinearIn,
   System.bool BRemovePickedIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BMutualTrimIn`: True to use the selected intersecting surfaces as the trimming surfaces (mutual), false to use the selected surface, plane, or sketch as the trim tool (standard)
- `BSplitSystemIn`: True to let the SOLIDWORKS Design application determine which surfaces to trim, false to trim all possible surfaces
- `BSplitLinearIn`: False to naturally extend any trims along the intersecting surfaces, true to extend any trims linearly along the intersecting surfaces
- `BRemovePickedIn`: True to remove the selected surfaces, false to keep the selected surfaces

### Return Value

True if successful, false if not

## VBA Syntax

See [FeatureManager::PreTrimSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~PreTrimSurface.html).

## Examples

[Create Trimmed Surface Feature (C#)](Create_Trimmed_Surface_Feature_Example_CSharp.htm)
[Create Trimmed Surface Feature (VB.NET)](Create_Trimmed_Surface_Feature_Example_VBNET.htm)
[Create Trimmed Surface Feature (VBA)](Create_Trimmed_Surface_Feature_Example_VB.htm)
[Create Solid Body Surface Trim Feature (C#)](Create_Solid_Body_Surface_Trim_Feature_Example_CSharp.htm)
[Create Solid Body Surface Trim Feature (VB.NET)](Create_Solid_Body_Surface_Trim_Feature_Example_VBNET.htm)
[Create Solid Body Surface Trim Feature (VBA)](Create_Solid_Body_Surface_Trim_Feature_Example_VB.htm)

## Remarks

After calling this method:

1. Select the trimming surfaces or trim tool.
2. Optionally, call [IFeatureManager::SolidForTrim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SolidForTrim.html).
3. Call [IFeatureManager::PostTrimSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostTrimSurface.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
