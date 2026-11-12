---
title: "GetTrimmingBoundary Method (IWeldmentTrimExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentTrimExtendFeatureData"
member: "GetTrimmingBoundary"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.html"
---

# GetTrimmingBoundary Method (IWeldmentTrimExtendFeatureData)

Gets the entities used to define the trimming boundaries.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrimmingBoundary( _
   ByRef Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentTrimExtendFeatureData
Dim Type As System.Integer
Dim value As System.Object

value = instance.GetTrimmingBoundary(Type)
```

### C#

```csharp
System.object GetTrimmingBoundary(
   out System.int Type
)
```

### C++/CLI

```cpp
System.Object^ GetTrimmingBoundary(
   [Out] System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of trimming boundary:

  - swSelSOLIDBODIES
  - SwSelFACES

### Return Value

Array of the entities that define the trimming boundaries

## VBA Syntax

See [WeldmentTrimExtendFeatureData::GetTrimmingBoundary](ms-its:sldworksapivb6.chm::/sldworks~WeldmentTrimExtendFeatureData~GetTrimmingBoundary.html).

## Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple boundaries. Use [IWeldmentTrimExtendFeatureData::CornerType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.html) to determine the type of corner.

## See Also

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html)
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount.html)
[IWeldmentTrimExtendFeatureData::IGetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::ISetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::SetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
