---
title: "GetNextDisplayDimension Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetNextDisplayDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextDisplayDimension.html"
---

# GetNextDisplayDimension Method (IFeature)

Gets the next display dimension associated with this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextDisplayDimension( _
   ByVal DispIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim DispIn As System.Object
Dim value As System.Object

value = instance.GetNextDisplayDimension(DispIn)
```

### C#

```csharp
System.object GetNextDisplayDimension(
   System.object DispIn
)
```

### C++/CLI

```cpp
System.Object^ GetNextDisplayDimension(
   System.Object^ DispIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DispIn`: [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object obtained with [IFeature::GetFirstDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstDisplayDimension.html) or from your previous call to this method

### Return Value

Next [IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object based on the DispIn argument, or NULL if there are no more dimensions

## VBA Syntax

See [Feature::GetNextDisplayDimension](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetNextDisplayDimension.html).

## Examples

[Traverse Annotations (C#)](Traverse_Annotations_Example_CSharp.htm)
[Traverse Annotations (VB.NET)](Traverse_Annotations_Example_VBNET.htm)
[Traverse Annotations (VBA)](Traverse_Annotations_Example_VB.htm)

## Remarks

Before you can get a feature's IDisplayDimension, use [IModelDoc2::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html) and swDisplayFeatureDimension to display them.

All dimensions on this feature and its sub-features are returned by either [IFeature::GetFirstDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstDisplayDimension.html) and IFeature::GetNextDisplayDimension or [IFeature::EnumDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~EnumDisplayDimensions.html). In the user-interface, this is equivalent to double-clicking a feature in the FeatureManager design tree to display all of the feature and sub-feature dimensions.

If you call this method from a sub-feature (for example, the sketch of a boss-extrude), then the IDisplayDimension object returned by IFeature::GetFirstDisplayDimension and IFeature::GetNextDisplayDimension contain only the dimensions found in the sketch.

This method might not always return display dimensions in the same order.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetDisplayDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDisplayDimension.html)
