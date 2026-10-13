---
title: "ReplacementSurfaces Property (IReplaceFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReplaceFaceFeatureData"
member: "ReplacementSurfaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ReplacementSurfaces.html"
---

# ReplacementSurfaces Property (IReplaceFaceFeatureData)

Gets or sets the replacement surfaces for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReplacementSurfaces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IReplaceFaceFeatureData
Dim value As System.Object

instance.ReplacementSurfaces = value

value = instance.ReplacementSurfaces
```

### C#

```csharp
System.object ReplacementSurfaces {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReplacementSurfaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of replacement surfaces

## VBA Syntax

See [ReplaceFaceFeatureData::ReplacementSurfaces](ms-its:sldworksapivb6.chm::/sldworks~ReplaceFaceFeatureData~ReplacementSurfaces.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html)
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.html)
[IReplaceFaceFeatureData::GetReplacementSurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetReplacementSurfacesCount.html)
[IReplaceFaceFeatureData::IGetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetReplacementSurfaces.html)
[IReplaceFaceFeatureData::ISetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetReplacementSurfaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
