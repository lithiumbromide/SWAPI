---
title: "ISetEntities Method (ISurfaceKnitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData"
member: "ISetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~ISetEntities.html"
---

# ISetEntities Method (ISurfaceKnitFeatureData)

Sets the faces and surfaces to knit.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetEntities( _
   ByVal Count As System.Integer, _
   ByRef FaceArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceKnitFeatureData
Dim Count As System.Integer
Dim FaceArr As System.Object

instance.ISetEntities(Count, FaceArr)
```

### C#

```csharp
void ISetEntities(
   System.int Count,
   ref System.object FaceArr
)
```

### C++/CLI

```cpp
void ISetEntities(
   System.int Count,
   System.Object^% FaceArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces
- `FaceArr`: - in-process, unmanaged C++: Pointer to an array of knit entities ([faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) and [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [SurfaceKnitFeatureData::ISetEntities](ms-its:sldworksapivb6.chm::/sldworks~SurfaceKnitFeatureData~ISetEntities.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html)
[ISurfaceKnitFeatureData::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~Entities.html)
[ISurfaceKnitFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~IGetEntities.html)
[ISurfaceKnitFeatureData::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~GetEntitiesCount.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
