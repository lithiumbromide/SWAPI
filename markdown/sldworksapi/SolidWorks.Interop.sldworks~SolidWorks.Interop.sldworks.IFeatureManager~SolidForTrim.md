---
title: "SolidForTrim Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "SolidForTrim"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SolidForTrim.html"
---

# SolidForTrim Property (IFeatureManager)

Gets or sets whether a [surface trim feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html) is a solid body or a surface body.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolidForTrim As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.SolidForTrim = value

value = instance.SolidForTrim
```

### C#

```csharp
System.bool SolidForTrim {get; set;}
```

### C++/CLI

```cpp
property System.bool SolidForTrim {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if a solid body, false if a surface body (see **Remarks**)

## VBA Syntax

See [FeatureManager::SolidForTrim](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~SolidForTrim.html).

## Examples

[Create Solid Body Surface Trim Feature (C#)](Create_Solid_Body_Surface_Trim_Feature_Example_CSharp.htm)
[Create Solid Body Surface Trim Feature (VB.NET)](Create_Solid_Body_Surface_Trim_Feature_Example_VBNET.htm)
[Create Solid Body Surface Trim Feature (VBA)](Create_Solid_Body_Surface_Trim_Feature_Example_VB.htm)

## Remarks

This property is only available when creating a surface trim feature. Call this property:

- after calling [IFeatureManager::PreTrimSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreTrimSurface.html)
- before calling [IFeatureManager::PostTrimSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostTrimSurface.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
