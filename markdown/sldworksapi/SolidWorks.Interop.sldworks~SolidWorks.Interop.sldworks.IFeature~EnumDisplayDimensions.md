---
title: "EnumDisplayDimensions Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "EnumDisplayDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~EnumDisplayDimensions.html"
---

# EnumDisplayDimensions Method (IFeature)

This method returns a [display dimensions enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDisplayDimensions.html) for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumDisplayDimensions() As EnumDisplayDimensions
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As EnumDisplayDimensions

value = instance.EnumDisplayDimensions()
```

### C#

```csharp
EnumDisplayDimensions EnumDisplayDimensions()
```

### C++/CLI

```cpp
EnumDisplayDimensions^ EnumDisplayDimensions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to a [display dimensions enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDisplayDimensions.html) for this feature

## VBA Syntax

See [Feature::EnumDisplayDimensions](ms-its:sldworksapivb6.chm::/sldworks~Feature~EnumDisplayDimensions.html).

## Remarks

Before you can get a feature's display dimensions, use [IModelDoc2::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html) and swDisplayFeatureDimension to display them.

All dimensions on this feature and its sub-features are returned in the enumeration. In the user-interface, this is equivalent to double-clicking a feature in the FeatureManager design tree to display all of the feature and sub-feature dimensions.

If you call this method from a sub-feature (for example, the sketch of a boss-extrude), then the returned dimensions contain only the dimensions found in the sketch.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetFirstDisplayDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstDisplayDimension.html)
[IFeature::GetNextDisplayDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextDisplayDimension.html)
[IFeature::GetDisplayDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDisplayDimension.html)
