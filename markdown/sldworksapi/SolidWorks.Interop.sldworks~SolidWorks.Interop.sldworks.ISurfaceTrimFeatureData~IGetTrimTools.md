---
title: "IGetTrimTools Method (ISurfaceTrimFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceTrimFeatureData"
member: "IGetTrimTools"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~IGetTrimTools.html"
---

# IGetTrimTools Method (ISurfaceTrimFeatureData)

Gets the trim tools for this surface trim feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTrimTools( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceTrimFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetTrimTools(Count)
```

### C#

```csharp
System.object IGetTrimTools(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetTrimTools(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of trim tools

### Return Value

- in-process, unmanaged C++: Pointer to an array of trim tools of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [SurfaceTrimFeatureData::IGetTrimTools](ms-its:sldworksapivb6.chm::/sldworks~SurfaceTrimFeatureData~IGetTrimTools.html).

## Remarks

Call [ISurfaceTrimFeatureData::GetTrimToolsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceTrimFeatureData~GetTrimToolsCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.html)
[ISurfaceTrimFeatureData::ISetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetTrimTools.html)
[ISurfaceTrimFeatureData::TrimTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~TrimTools.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
