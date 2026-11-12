---
title: "IGetSelectionFiltersCount Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetSelectionFiltersCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html"
---

# IGetSelectionFiltersCount Method (ISldWorks)

Gets the number of active selection filters.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSelectionFiltersCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

value = instance.IGetSelectionFiltersCount()
```

### C#

```csharp
System.int IGetSelectionFiltersCount()
```

### C++/CLI

```cpp
System.int IGetSelectionFiltersCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of all active selection filters

## VBA Syntax

See [SldWorks::IGetSelectionFiltersCount](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetSelectionFiltersCount.html).

## Remarks

Call this method before calling [ISldWorks::IGetSelectionFilters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetSelectionFilters.html) to determine the size of the array to pass that to that method.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilter.html)
[ISldWorks::GetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilters.html)
[ISldWorks::ISetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.html)
[ISldWorks::SetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.html)
[ISldWorks::SetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.html)
[ISldWorks::GetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetApplySelectionFilter.html)
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
