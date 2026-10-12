---
title: "BoundingSketch Property (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "BoundingSketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~BoundingSketch.html"
---

# BoundingSketch Property (ICoreFeatureData)

Gets or sets the bounding sketch for this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BoundingSketch As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim value As Feature

instance.BoundingSketch = value

value = instance.BoundingSketch
```

### C#

```csharp
Feature BoundingSketch {get; set;}
```

### C++/CLI

```cpp
property Feature^ BoundingSketch {
   Feature^ get();
   void set (    Feature^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [CoreFeatureData::BoundingSketch](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~BoundingSketch.html).

## Examples

[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)
[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
