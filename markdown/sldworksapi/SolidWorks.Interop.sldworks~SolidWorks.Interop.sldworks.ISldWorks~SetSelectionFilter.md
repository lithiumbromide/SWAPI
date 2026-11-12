---
title: "SetSelectionFilter Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetSelectionFilter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.html"
---

# SetSelectionFilter Method (ISldWorks)

Sets the current selection filter values for the specified item type.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSelectionFilter( _
   ByVal SelType As System.Integer, _
   ByVal State As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim SelType As System.Integer
Dim State As System.Boolean

instance.SetSelectionFilter(SelType, State)
```

### C#

```csharp
void SetSelectionFilter(
   System.int SelType,
   System.bool State
)
```

### C++/CLI

```cpp
void SetSelectionFilter(
   System.int SelType,
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelType`: Selection type enable or disable as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `State`: True to enable selection of the specified type, false to disable the end-user's ability to select the item

## VBA Syntax

See [SldWorks::SetSelectionFilter](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetSelectionFilter.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetApplySelectionFilter.html)
[ISldWorks::GetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilter.html)
[ISldWorks::GetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilters.html)
[ISldWorks::IGetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFilters.html)
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html)
[ISldWorks::ISetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.html)
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.html)
[ISldWorks::SetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.html)

## Availability

SOLIDWORKS 99, datecode 1999207
