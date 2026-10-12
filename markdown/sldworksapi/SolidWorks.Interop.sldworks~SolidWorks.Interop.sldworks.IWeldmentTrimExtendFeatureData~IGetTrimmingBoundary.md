---
title: "IGetTrimmingBoundary Method (IWeldmentTrimExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentTrimExtendFeatureData"
member: "IGetTrimmingBoundary"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary.html"
---

# IGetTrimmingBoundary Method (IWeldmentTrimExtendFeatureData)

Gets the entities used to define the trimming boundaries.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTrimmingBoundary( _
   ByVal Count As System.Integer, _
   ByRef Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentTrimExtendFeatureData
Dim Count As System.Integer
Dim Type As System.Integer
Dim value As System.Object

value = instance.IGetTrimmingBoundary(Count, Type)
```

### C#

```csharp
System.object IGetTrimmingBoundary(
   System.int Count,
   out System.int Type
)
```

### C++/CLI

```cpp
System.Object^ IGetTrimmingBoundary(
   System.int Count,
   [Out] System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of trimming boundaries
- `Type`: Type of trimming boundary:

  - swSelSOLIDBODIES
  - SwSelFACES

### Return Value

- in-process, unmanaged C++: Pointer to an array of entities that define the trimming boundaries
- VBA, VB.NET, C#, and C++/CLI: Not supported
- See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple boundaries. Use [IWeldmentTrimExtendFeatureData::CornerType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.html) to determine the type of corner.

Before calling this method, call [IWeldmentTrimExtendFeatureData::GetTrimmingBoundaryCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount.html) to get Count.

## See Also

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html)
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::ISetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary.html)
[IWeldmentTrimExtendFeatureData::SetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
