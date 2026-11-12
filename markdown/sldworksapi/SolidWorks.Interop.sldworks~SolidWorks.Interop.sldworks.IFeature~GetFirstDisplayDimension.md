---
title: "GetFirstDisplayDimension Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetFirstDisplayDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstDisplayDimension.html"
---

# GetFirstDisplayDimension Method (IFeature)

Provides access to the dimensions that belong to this feature by returning the first display dimension associated with this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstDisplayDimension() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetFirstDisplayDimension()
```

### C#

```csharp
System.object GetFirstDisplayDimension()
```

### C++/CLI

```cpp
System.Object^ GetFirstDisplayDimension();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object for this feature, or Nothing or null if there are no dimensions for this feature

## VBA Syntax

See [Feature::GetFirstDisplayDimension](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetFirstDisplayDimension.html).

## Examples

[Traverse Annotations (C#)](Traverse_Annotations_Example_CSharp.htm)
[Traverse Annotations (VB.NET)](Traverse_Annotations_Example_VBNET.htm)
[Traverse Annotations (VBA)](Traverse_Annotations_Example_VB.htm)

## Remarks

Before you can get a feature's IDisplayDimension, use [IModelDoc2::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html) and swDisplayFeatureDimensions to display them.

All dimensions on this feature its sub-features are returned by either IFeature::GetFirstDisplayDimension and [IFeature::GetNextDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextDisplayDimension.html) or [IFeature::EnumDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~EnumDisplayDimensions.html). In the user-interface, this is equivalent to double-clicking a feature in the FeatureManager design tree to display all of the feature and sub-feature dimensions.

If you call this method from a sub-feature (for example, the sketch of a boss-extrude), then the IDisplayDimension object returned by IFeature::GetFirstDisplayDimension and IFeature::GetNextDisplayDimension contain only the dimensions found in the sketch.

Do not use [IAnnotation::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Visible.html) property to modify this method's return value.

This method might not return the same display dimension every time it is called.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetDisplayDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDisplayDimension.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
