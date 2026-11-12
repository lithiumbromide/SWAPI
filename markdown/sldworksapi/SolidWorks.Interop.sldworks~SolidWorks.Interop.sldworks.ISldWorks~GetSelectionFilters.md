---
title: "GetSelectionFilters Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetSelectionFilters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilters.html"
---

# GetSelectionFilters Method (ISldWorks)

Gets all active selection filters.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionFilters() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

value = instance.GetSelectionFilters()
```

### C#

```csharp
System.object GetSelectionFilters()
```

### C++/CLI

```cpp
System.Object^ GetSelectionFilters();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of long values representing the [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) enumeration

## VBA Syntax

See [SldWorks::GetSelectionFilters](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetSelectionFilters.html).

## Examples

[Set and Toggle Selection Filters (VBA)](Clear,_Set,_and_Toggle_Selection_Filters_Example_VB.htm)

## Remarks

To determine if the selection filter is active, call [ISldWorks::GetApplySelectionFilter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetApplySelectionFilter.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilter.html)
[ISldWorks::IGetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFilters.html)
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html)
[ISldWorks::ISetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.html)
[ISldWorks::SetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.html)
[ISldWorks::SetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.html)
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
