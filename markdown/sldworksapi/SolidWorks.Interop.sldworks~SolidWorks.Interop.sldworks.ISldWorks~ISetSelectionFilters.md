---
title: "ISetSelectionFilters Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ISetSelectionFilters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.html"
---

# ISetSelectionFilters Method (ISldWorks)

Sets the status for multiple selection filters.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSelectionFilters( _
   ByVal Count As System.Integer, _
   ByRef SelType As System.Integer, _
   ByVal State As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Count As System.Integer
Dim SelType As System.Integer
Dim State As System.Boolean

instance.ISetSelectionFilters(Count, SelType, State)
```

### C#

```csharp
void ISetSelectionFilters(
   System.int Count,
   ref System.int SelType,
   System.bool State
)
```

### C++/CLI

```cpp
void ISetSelectionFilters(
   System.int Count,
   System.int% SelType,
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of values in SelType
- `SelType`: - in-process, unmanaged C++: Pointer to an array of long values representing the [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `State`:

## VBA Syntax

See [SldWorks::ISetSelectionFilters](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ISetSelectionFilters.html).

## Remarks

The state is applied to all elements in the SelType array. To determine if the selection filter is active, use [ISldWorks::GetApplySelectionFilter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetApplySelectionFilter.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilter.html)
[ISldWorks::GetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilters.html)
[ISldWorks::IGetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFilters.html)
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html)
[ISldWorks::SetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.html)
[ISldWorks::SetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.html)
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.html)
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
