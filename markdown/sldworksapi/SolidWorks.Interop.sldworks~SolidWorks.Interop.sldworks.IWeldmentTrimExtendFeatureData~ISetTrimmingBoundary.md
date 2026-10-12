---
title: "ISetTrimmingBoundary Method (IWeldmentTrimExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentTrimExtendFeatureData"
member: "ISetTrimmingBoundary"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary.html"
---

# ISetTrimmingBoundary Method (IWeldmentTrimExtendFeatureData)

Gets the entities used to define the trimming boundaries.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetTrimmingBoundary( _
   ByVal Count As System.Integer, _
   ByRef TrimBoundArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentTrimExtendFeatureData
Dim Count As System.Integer
Dim TrimBoundArr As System.Object

instance.ISetTrimmingBoundary(Count, TrimBoundArr)
```

### C#

```csharp
void ISetTrimmingBoundary(
   System.int Count,
   ref System.object TrimBoundArr
)
```

### C++/CLI

```cpp
void ISetTrimmingBoundary(
   System.int Count,
   System.Object^% TrimBoundArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of trimming boundaries
- `TrimBoundArr`: - in-process, unmanaged C++: Pointer to an array of entities that define the trimming boundaries (see **Remarks**)

    - Solid bodies created by weldment members

      - or -
    - Planar faces on non-weldment members, or planar faces on weldment members, or both

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

Entities that define the trimming boundaries

## Remarks

Faces are valid for end-trim corner types only. You can only specify multiple trimming boundaries for end-trim corner types. Use [IWeldmentTrimExtendFeatureData::CornerType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.html) to determine the type of corner.

You must set the [bodies to trim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.html) and set the trimming boundary if changing a corner type.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html)
[IWeldmentTrimExtendFeatureData::SetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::IGetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount.html)
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
