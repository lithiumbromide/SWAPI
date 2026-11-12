---
title: "ISetTrimTools Method (ISplitBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitBodyFeatureData"
member: "ISetTrimTools"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetTrimTools.html"
---

# ISetTrimTools Method (ISplitBodyFeatureData)

Gets the trimming surfaces used as trim tools in this Split feature.

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
Dim instance As ISplitBodyFeatureData
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

- `Count`: Number of trimming surfaces used as trim tools
- `DispArr`: - in-process, unmanaged C++: Pointer to an array of trimming surfaces used as trim tools :

    - Planar and non-planar faces
    - Reference planes
    - Reference surfaces
    - Sketches
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html)
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html)
[ISplitBodyFeatureData::GetTrimToolsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetTrimToolsCount.html)
[ISplitBodyFeatureData::IGetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetTrimTools.html)
[ISplitBodyFeatureData::TrimTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TrimTools.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
