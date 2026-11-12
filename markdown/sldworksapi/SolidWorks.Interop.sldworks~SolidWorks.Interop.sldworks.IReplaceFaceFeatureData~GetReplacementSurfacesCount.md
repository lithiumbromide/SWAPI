---
title: "GetReplacementSurfacesCount Method (IReplaceFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReplaceFaceFeatureData"
member: "GetReplacementSurfacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetReplacementSurfacesCount.html"
---

# GetReplacementSurfacesCount Method (IReplaceFaceFeatureData)

Gets the number of replacement surfaces for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReplacementSurfacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IReplaceFaceFeatureData
Dim value As System.Integer

value = instance.GetReplacementSurfacesCount()
```

### C#

```csharp
System.int GetReplacementSurfacesCount()
```

### C++/CLI

```cpp
System.int GetReplacementSurfacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of replacement surfaces

## VBA Syntax

See [ReplaceFaceFeatureData::GetReplacementSurfacesCount](ms-its:sldworksapivb6.chm::/sldworks~ReplaceFaceFeatureData~GetReplacementSurfacesCount.html).

## Examples

See the [IReplaceFaceFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html) examples.

## Remarks

Call this method before calling [IReplaceFaceFeatureData::IGetReplacementSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReplaceFaceFeatureData~IGetReplacementSurfaces.html).

## See Also

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.html)
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.html)
[IReplaceFaceFeatureData::ISetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetReplacementSurfaces.html)
[IReplaceFaceFeatureData::ReplacementSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ReplacementSurfaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
