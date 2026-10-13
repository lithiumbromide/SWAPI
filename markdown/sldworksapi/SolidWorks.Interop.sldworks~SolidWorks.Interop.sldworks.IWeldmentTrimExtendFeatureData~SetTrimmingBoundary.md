---
title: "SetTrimmingBoundary Method (IWeldmentTrimExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentTrimExtendFeatureData"
member: "SetTrimmingBoundary"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.html"
---

# SetTrimmingBoundary Method (IWeldmentTrimExtendFeatureData)

Sets the trimming boundaries for this weldment trim extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTrimmingBoundary( _
   ByVal TrimBoundVar As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentTrimExtendFeatureData
Dim TrimBoundVar As System.Object

instance.SetTrimmingBoundary(TrimBoundVar)
```

### C#

```csharp
void SetTrimmingBoundary(
   System.object TrimBoundVar
)
```

### C++/CLI

```cpp
void SetTrimmingBoundary(
   System.Object^ TrimBoundVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TrimBoundVar`: Number of trimming boundaries

### Return Value

Array of trimming boundaries:

- Solid bodies created by weldment members

  - or -
- Planar faces on non-weldment members, or planar faces on weldment members, or both

See Remarks.

## VBA Syntax

See [WeldmentTrimExtendFeatureData::SetTrimmingBoundary](ms-its:sldworksapivb6.chm::/sldworks~WeldmentTrimExtendFeatureData~SetTrimmingBoundary.html).

## Remarks

Faces are valid for end-trim corner types only. You can only specify multiple trimming boundaries for end-trim corner types. Use [IWeldmentTrimExtendFeatureData::CornerType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.html) to determine the type of corner.

You must set the [bodies to trim](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.html) and set the trimming boundary if changing a corner type.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html)
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::IGetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
