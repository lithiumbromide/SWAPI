---
title: "IGetReplacementSurfaces Method (IReplaceFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReplaceFaceFeatureData"
member: "IGetReplacementSurfaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetReplacementSurfaces.html"
---

# IGetReplacementSurfaces Method (IReplaceFaceFeatureData)

Gets the replacement surfaces for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetReplacementSurfaces( _
   ByVal Count As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IReplaceFaceFeatureData
Dim Count As System.Integer
Dim value As Feature

value = instance.IGetReplacementSurfaces(Count)
```

### C#

```csharp
Feature IGetReplacementSurfaces(
   System.int Count
)
```

### C++/CLI

```cpp
Feature^ IGetReplacementSurfaces(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of replacement surfaces

### Return Value

- in-process, unmanaged C++: Pointer to an array of [replacement surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) of size Count
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IReplaceFaceFeatureData::GetReplacementSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReplaceFaceFeatureData~GetReplacementSurfacesCount.html) before calling this method to get the size of Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html)
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.html)
[IReplaceFaceFeatureData::ISetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetReplacementSurfaces.html)
[IReplaceFaceFeatureData::ReplacementSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ReplacementSurfaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
