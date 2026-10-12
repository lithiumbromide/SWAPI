---
title: "FeatureScopeBodies Property (ISurfaceCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceCutFeatureData"
member: "FeatureScopeBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScopeBodies.html"
---

# FeatureScopeBodies Property (ISurfaceCutFeatureData)

Gets or sets the solid bodies that the surface-cut feature affects in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScopeBodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceCutFeatureData
Dim value As System.Object

instance.FeatureScopeBodies = value

value = instance.FeatureScopeBodies
```

### C#

```csharp
System.object FeatureScopeBodies {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FeatureScopeBodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that the surface-cut feature affects

## VBA Syntax

See [SurfCutFeatureData::FeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~SurfCutFeatureData~FeatureScopeBodies.html).

## Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.html)
[ISurfaceCutFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~GetFeatureScopeBodiesCount.html)
[ISurfaceCutFeatureData::IGetFeatureScopeBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies.html)
[ISurfaceCutFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~ISetFeatureScopeBodies.html)
[ISurfaceCutFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~AutoSelect.html)
[ISurfaceCutFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScope.html)

## Availability

SOLIDWORKS 2013 SP1, Revision Number 21.1
