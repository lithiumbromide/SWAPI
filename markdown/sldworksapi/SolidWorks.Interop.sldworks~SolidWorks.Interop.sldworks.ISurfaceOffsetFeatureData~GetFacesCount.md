---
title: "GetFacesCount Method (ISurfaceOffsetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceOffsetFeatureData"
member: "GetFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~GetFacesCount.html"
---

# GetFacesCount Method (ISurfaceOffsetFeatureData)

Obsolete. Superseded by [ISurfaceOffsetFeatureData::GetEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceOffsetFeatureData~GetEntitiesCount.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceOffsetFeatureData
Dim value As System.Integer

value = instance.GetFacesCount()
```

### C#

```csharp
System.int GetFacesCount()
```

### C++/CLI

```cpp
System.int GetFacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of offset faces

## VBA Syntax

See [SurfaceOffsetFeatureData::GetFacesCount](ms-its:sldworksapivb6.chm::/sldworks~SurfaceOffsetFeatureData~GetFacesCount.html).

## Remarks

Call this method before calling [ISurfaceOffsetFeatureData::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceOffsetFeatureData~IGetFaces.html).

## See Also

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.html)
[ISurfaceOffsetFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~ISetFaces.html)
[ISurfaceOffsetFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Faces.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
