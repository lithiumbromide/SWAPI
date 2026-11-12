---
title: "GetApplySelectionFilter Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetApplySelectionFilter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetApplySelectionFilter.html"
---

# GetApplySelectionFilter Method (ISldWorks)

Gets the current state of the selection filter.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetApplySelectionFilter() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

value = instance.GetApplySelectionFilter()
```

### C#

```csharp
System.bool GetApplySelectionFilter()
```

### C++/CLI

```cpp
System.bool GetApplySelectionFilter();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selection filter is active, false if not

## VBA Syntax

See [SldWorks::GetApplySelectionFilter](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetApplySelectionFilter.html).

## Examples

[Set and Toggle Selection Filters (VBA)](Clear,_Set,_and_Toggle_Selection_Filters_Example_VB.htm)

## Remarks

If the selection filter is active, then the settings found in [ISldWorks::GetSelectionFilter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetSelectionFilter.html) and [ISldWorks::GetSelectionFilters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetSelectionFilters.html) or [ISldWorks::IGetSelectionFilters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetSelectionFilters.html) apply.

| Use... | To... |
| --- | --- |
| ISldWorks::SetApplySelectionFilter | Activate or deactivate the selection filter |
| ISldWorks::SetSelectionFilter and ISldWorks::SetSelectionFilters or ISldWorks::ISetSelectionFilters | Change the current filters in use |

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html)
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
