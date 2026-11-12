---
title: "GetTrimmingBoundaryCount Method (IWeldmentTrimExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentTrimExtendFeatureData"
member: "GetTrimmingBoundaryCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount.html"
---

# GetTrimmingBoundaryCount Method (IWeldmentTrimExtendFeatureData)

Gets the number of trimming boundaries.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrimmingBoundaryCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentTrimExtendFeatureData
Dim value As System.Integer

value = instance.GetTrimmingBoundaryCount()
```

### C#

```csharp
System.int GetTrimmingBoundaryCount()
```

### C++/CLI

```cpp
System.int GetTrimmingBoundaryCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of trimming boundaries

## VBA Syntax

See [WeldmentTrimExtendFeatureData::GetTrimmingBoundaryCount](ms-its:sldworksapivb6.chm::/sldworks~WeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount.html).

## Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple boundaries. Use [IWeldmentTrimExtendFeatureData::CornerType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.html) to determine the type of corner.

Call this method before calling [IWeldmentTrimExtendFeaturedata::IGetTrimmingBoundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary.html)

## See Also

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html)
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::ISetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::SetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
