---
title: "Close Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "Close"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~Close.html"
---

# Close Method (IPowerSelect)

Closes the current session of PowerSelect.

## Syntax

### Visual Basic (Declaration)

```vb
Function Close() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim value As System.Integer

value = instance.Close()
```

### C#

```csharp
System.int Close()
```

### C++/CLI

```cpp
System.int Close();
```

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::Close](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~Close.html).

## Examples

[Run PowerSelect (VBA)](Run_PowerSelect_VB6.htm)
[Select and Get Number of Edges, Loops, Faces, and Features (VBA)](Select_and_Get_Number_of_Edges,_Loops,_Faces,_and_Features_Example_VB6.htm)

## Remarks

Because you cannot have more than one SOLIDWORKS Utilities tool running at any one time, you must close a running PowerSelect session before you can use another SOLIDWORKS Utilities tool. To initialize a PowerSelect session, call [IPowerSelect::Init](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect~Init.html).

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::Init Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~Init.html)
[IPowerSelect::IRunPowerSelect Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~IRunPowerSelect.html)
[IPowerSelect::RunPowerSelect Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~RunPowerSelect.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
