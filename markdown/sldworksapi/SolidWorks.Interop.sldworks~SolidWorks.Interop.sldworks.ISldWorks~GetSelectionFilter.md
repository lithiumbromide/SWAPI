---
title: "GetSelectionFilter Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetSelectionFilter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilter.html"
---

# GetSelectionFilter Method (ISldWorks)

Gets the current selection filter settings for the specified item type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionFilter( _
   ByVal SelType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim SelType As System.Integer
Dim value As System.Boolean

value = instance.GetSelectionFilter(SelType)
```

### C#

```csharp
System.bool GetSelectionFilter(
   System.int SelType
)
```

### C++/CLI

```cpp
System.bool GetSelectionFilter(
   System.int SelType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelType`: Selection type to verify as defined in [swSelelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

True if selection of the specified type is allowed, false if selection of the specified type is disabled

## VBA Syntax

See [SldWorks::GetSelectionFilter](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetSelectionFilter.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetApplySelectionFilter.html)
[ISldWorks::GetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilters.html)
[ISldWorks::IGetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFilters.html)
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.html)
[ISldWorks::ISetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.html)
[ISldWorks::SetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.html)
[ISldWorks::SetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.html)
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.html)

## Availability

SOLIDWORKS 99, datecode 1999207
