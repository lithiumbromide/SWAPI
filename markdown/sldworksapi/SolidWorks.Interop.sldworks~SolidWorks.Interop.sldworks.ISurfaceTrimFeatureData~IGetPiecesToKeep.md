---
title: "IGetPiecesToKeep Method (ISurfaceTrimFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceTrimFeatureData"
member: "IGetPiecesToKeep"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~IGetPiecesToKeep.html"
---

# IGetPiecesToKeep Method (ISurfaceTrimFeatureData)

Gets the pieces to keep for this surface trim feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPiecesToKeep( _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceTrimFeatureData
Dim Count As System.Integer
Dim value As Body2

value = instance.IGetPiecesToKeep(Count)
```

### C#

```csharp
Body2 IGetPiecesToKeep(
   System.int Count
)
```

### C++/CLI

```cpp
Body2^ IGetPiecesToKeep(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of pieces to keep

### Return Value

- in-process, unmanaged C++: Pointer to an array of pieces to keep of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISurfaceTrimFeatureData::GetPiecesToKeepCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceTrimFeatureData~GetPiecesToKeepCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.html)
[ISurfaceTrimFeatureData::ISetPiecesToKeep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetPiecesToKeep.html)
[ISurfaceTrimFeatureData::PiecesToKeep Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~PiecesToKeep.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
