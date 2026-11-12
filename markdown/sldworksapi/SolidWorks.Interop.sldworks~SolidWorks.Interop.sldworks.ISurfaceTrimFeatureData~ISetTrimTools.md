---
title: "ISetTrimTools Method (ISurfaceTrimFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceTrimFeatureData"
member: "ISetTrimTools"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetTrimTools.html"
---

# ISetTrimTools Method (ISurfaceTrimFeatureData)

Sets the trim tools for this surface trim feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetTrimTools( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceTrimFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object

instance.ISetTrimTools(Count, DispArr)
```

### C#

```csharp
void ISetTrimTools(
   System.int Count,
   ref System.object DispArr
)
```

### C++/CLI

```cpp
void ISetTrimTools(
   System.int Count,
   System.Object^% DispArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of trim tools
- `DispArr`: - in-process, unmanaged C++: Pointer to an array of trim tools of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.html)
[ISurfaceTrimFeatureData::GetTrimToolsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~GetTrimToolsCount.html)
[ISurfaceTrimFeatureData::IGetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~IGetTrimTools.html)
[ISurfaceTrimFeatureData::TrimTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~TrimTools.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
