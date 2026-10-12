---
title: "SetApplySelectionFilter Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetApplySelectionFilter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.html"
---

# SetApplySelectionFilter Method (ISldWorks)

Sets the current state of the selection filter.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetApplySelectionFilter( _
   ByVal State As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim State As System.Boolean

instance.SetApplySelectionFilter(State)
```

### C#

```csharp
void SetApplySelectionFilter(
   System.bool State
)
```

### C++/CLI

```cpp
void SetApplySelectionFilter(
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `State`: True to activate the selection filter, false to not

## VBA Syntax

See [SldWorks::SetApplySelectionFilter](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetApplySelectionFilter.html).

## Remarks

If the selection filter is active, then the settings found in [ISldWorks::GetSelectionFilter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetSelectionFilter.html) and [ISldWorks::GetSelectionFilters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetSelectionFilters.html) or [ISldworks::IGetSelectionFilters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetSelectionFilters.html) apply.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::SetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.html)
[ISldWorks::SetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.html)
[ISldWorks::ISetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.html)
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html)
[ISldWorks::GetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetApplySelectionFilter.html)

## Availability

SOLIDWORKS 99, datecode 1999207
