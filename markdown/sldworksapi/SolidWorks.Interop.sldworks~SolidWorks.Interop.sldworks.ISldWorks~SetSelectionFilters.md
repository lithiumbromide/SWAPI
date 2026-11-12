---
title: "SetSelectionFilters Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetSelectionFilters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.html"
---

# SetSelectionFilters Method (ISldWorks)

Sets the status for multiple selection filters.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSelectionFilters( _
   ByVal SelType As System.Object, _
   ByVal State As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim SelType As System.Object
Dim State As System.Boolean

instance.SetSelectionFilters(SelType, State)
```

### C#

```csharp
void SetSelectionFilters(
   System.object SelType,
   System.bool State
)
```

### C++/CLI

```cpp
void SetSelectionFilters(
   System.Object^ SelType,
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelType`: Array of long values representing the [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `State`: True to activate the selection filters, false to not

## VBA Syntax

See [SldWorks::SetSelectionFilters](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetSelectionFilters.html).

## Examples

[Set and Toggle Selection Filters (VBA)](Clear,_Set,_and_Toggle_Selection_Filters_Example_VB.htm)

## Remarks

The state is applied to all elements in the SelType array. To determine if the selection filter is active, use [ISldWorks::GetApplySelectionFilter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetApplySelectionFilter.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilter.html)
[ISldWorks::GetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilters.html)
[ISldWorks::IGetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFilters.html)
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html)
[ISldWorks::ISetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.html)
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.html)
[ISldWorks::SetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
