---
title: "AutoSelect Property (ISurfaceCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceCutFeatureData"
member: "AutoSelect"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~AutoSelect.html"
---

# AutoSelect Property (ISurfaceCutFeatureData)

Gets or sets whether to automatically select all or only specific bodies for the surface-cut feature to affect in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSelect As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceCutFeatureData
Dim value As System.Boolean

instance.AutoSelect = value

value = instance.AutoSelect
```

### C#

```csharp
System.bool AutoSelect {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoSelect {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically select all bodies, false to select specific bodies for [ISurfaceCutFeatureData::FeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceCutFeatureData~FeatureScopeBodies.html) or [ISurfaceCutFeatureData::ISetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceCutFeatureData~ISetFeatureScopeBodies.html)

## VBA Syntax

See [SurfCutFeatureData::AutoSelect](ms-its:sldworksapivb6.chm::/sldworks~SurfCutFeatureData~AutoSelect.html).

## Examples

[Insert Surface-cut Feature (C#)](Insert_Surface-cut_Feature_Example_CSharp.htm)
[Insert Surface-cut Feature (VB.NET)](Insert_Surface-cut_Feature_Example_VBNET.htm)
[Insert Surface-cut Feature (VBA)](Insert_Surface-cut_Feature_Example_VB.htm)

## Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

This property is only available when [ISurfaceCutFeatureData::FeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceCutFeatureData~FeatureScope.html) is true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.html)
[ISurfaceCutFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~GetFeatureScopeBodiesCount.html)
[ISurfaceCutFeatureData::IGetFeatureScopeBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies.html)

## Availability

SOLIDWORKS 2013 SP1, Revision Number 21.1
