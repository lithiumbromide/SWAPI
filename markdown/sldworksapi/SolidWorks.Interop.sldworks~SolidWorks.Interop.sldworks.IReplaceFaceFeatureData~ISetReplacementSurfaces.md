---
title: "ISetReplacementSurfaces Method (IReplaceFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReplaceFaceFeatureData"
member: "ISetReplacementSurfaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetReplacementSurfaces.html"
---

# ISetReplacementSurfaces Method (IReplaceFaceFeatureData)

Sets the replacement surfaces for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetReplacementSurfaces( _
   ByVal Count As System.Integer, _
   ByRef SurfDisp As Feature _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IReplaceFaceFeatureData
Dim Count As System.Integer
Dim SurfDisp As Feature

instance.ISetReplacementSurfaces(Count, SurfDisp)
```

### C#

```csharp
void ISetReplacementSurfaces(
   System.int Count,
   ref Feature SurfDisp
)
```

### C++/CLI

```cpp
void ISetReplacementSurfaces(
   System.int Count,
   Feature^% SurfDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of replacement surfaces
- `SurfDisp`: - in-process, unmanaged C++: Pointer to an array of [replacement surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) of size Count
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html)
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.html)
[IReplaceFaceFeatureData::GetReplacementSurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetReplacementSurfacesCount.html)
[IReplaceFaceFeatureData::IGetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetReplacementSurfaces.html)
[IReplaceFaceFeatureData::ReplacementSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ReplacementSurfaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
