---
title: "SelectResults Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "SelectResults"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SelectResults.html"
---

# SelectResults Method (IPowerSelect)

Selects the results generated in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectResults() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim value As System.Integer

value = instance.SelectResults()
```

### C#

```csharp
System.int SelectResults()
```

### C++/CLI

```cpp
System.int SelectResults();
```

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SelectResults](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SelectResults.html).

## Examples

[Run PowerSelect (VBA)](Run_PowerSelect_VB6.htm)
[Select and Get Number of Edges, Loops, Faces, and Features (VBA)](Select_and_Get_Number_of_Edges,_Loops,_Faces,_and_Features_Example_VB6.htm)

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::RunPowerSelect Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~RunPowerSelect.html)
[IPowerSelect::IRunPowerSelect Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IRunPowerSelect.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
