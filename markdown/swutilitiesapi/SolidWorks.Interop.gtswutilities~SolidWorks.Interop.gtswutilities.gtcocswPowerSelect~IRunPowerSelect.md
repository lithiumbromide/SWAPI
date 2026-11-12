---
title: "IRunPowerSelect Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "IRunPowerSelect"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~IRunPowerSelect.html"
---

# IRunPowerSelect Method (gtcocswPowerSelect)

Runs PowerSelect using the previously set filters and entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function IRunPowerSelect( _
   ByVal lResultOptions As System.Integer, _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lResultOptions As System.Integer
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.IRunPowerSelect(lResultOptions, lErrorcode)
```

### C#

```csharp
System.int IRunPowerSelect(
   System.int lResultOptions,
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int IRunPowerSelect(
   System.int lResultOptions,
   [Out] System.int lErrorcode
)
```

### Parameters

- `lResultOptions`: Type of results as defined in [gtResultOptions_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtResultOptions_e.html) (see Remarks)
- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Array of the number of edges, loops, faces, and features

## VBA Syntax

See [IPowerSelect::IRunPowerSelect](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~IRunPowerSelect.html).

## Remarks

If IResultOptions is set to gtResultShowUI, then a dialog is displayed and the entities are selected in the dialog but are not selected in the graphics area. Users can select the entities by clicking Close, or users can click Cancel to cancel the selections.

A -1 is returned for any entity that was not set by [IPowerSelect::SetSelectEntitiesTypes](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect~SetSelectEntitiesTypes.html).

An error is returned if filters were not set by [IPowerSelect::ISetFeatureTypeFilter](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect~ISetFeatureTypeFilter.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
