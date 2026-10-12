---
title: "RunPowerSelect Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "RunPowerSelect"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~RunPowerSelect.html"
---

# RunPowerSelect Method (IPowerSelect)

Runs PowerSelect using the previously set filters and entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunPowerSelect( _
   ByVal lResultOptions As System.Integer, _
   ByRef lErrorcode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lResultOptions As System.Integer
Dim lErrorcode As System.Integer
Dim value As System.Object

value = instance.RunPowerSelect(lResultOptions, lErrorcode)
```

### C#

```csharp
System.object RunPowerSelect(
   System.int lResultOptions,
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.Object^ RunPowerSelect(
   System.int lResultOptions,
   [Out] System.int lErrorcode
)
```

### Parameters

- `lResultOptions`: Type of results as defined in [gtResultOptions_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtResultOptions_e.html) (see **Remarks**)
- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Array of the number of edges, loops, faces, and features

## VBA Syntax

See [IPowerSelect::RunPowerSelect](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~RunPowerSelect.html).

## Remarks

If IResultOptions is set to gtResultShowUI, then a dialog is displayed and the entities are selected in the dialog but are not selected in the graphics area. Users can select the entities by clicking Close, or users can click Cancel to cancel the selections.

A -1 is returned for any entity that was not set by [IPowerSelect::SetSelectEntitiesTypes](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect~SetSelectEntitiesTypes.html).

An error is returned if filters were not set by [IPowerSelect::SetFeatureTypeFilter](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect~SetFeatureTypeFilter.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::IRunPowerSelect Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IRunPowerSelect.html)
[IPowerSelect::Init Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~Init.html)
[IPowerSelect::Close Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~Close.html)
[IPowerSelect::SelectResults Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SelectResults.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
