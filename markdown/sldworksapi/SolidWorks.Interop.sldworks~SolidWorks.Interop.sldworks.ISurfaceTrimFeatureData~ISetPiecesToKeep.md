---
title: "ISetPiecesToKeep Method (ISurfaceTrimFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceTrimFeatureData"
member: "ISetPiecesToKeep"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetPiecesToKeep.html"
---

# ISetPiecesToKeep Method (ISurfaceTrimFeatureData)

Sets the pieces to keep for this surface trim feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPiecesToKeep( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceTrimFeatureData
Dim Count As System.Integer
Dim BodyArr As Body2

instance.ISetPiecesToKeep(Count, BodyArr)
```

### C#

```csharp
void ISetPiecesToKeep(
   System.int Count,
   ref Body2 BodyArr
)
```

### C++/CLI

```cpp
void ISetPiecesToKeep(
   System.int Count,
   Body2^% BodyArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of pieces to keep
- `BodyArr`: - in-process, unmanaged C++: Pointer to an array of pieces to keep of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.html)
[ISurfaceTrimFeatureData::GetPiecesToKeepCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~GetPiecesToKeepCount.html)
[ISurfaceTrimFeatureData::IGetPiecesToKeep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~IGetPiecesToKeep.html)
[ISurfaceTrimFeatureData::PiecesToKeep Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~PiecesToKeep.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
