---
title: "SetSelectEntitiesTypes Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "SetSelectEntitiesTypes"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~SetSelectEntitiesTypes.html"
---

# SetSelectEntitiesTypes Method (IPowerSelect)

Sets the types of entities for this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSelectEntitiesTypes( _
   ByVal selTypes As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim selTypes As System.Integer
Dim value As System.Integer

value = instance.SetSelectEntitiesTypes(selTypes)
```

### C#

```csharp
System.int SetSelectEntitiesTypes(
   System.int selTypes
)
```

### C++/CLI

```cpp
System.int SetSelectEntitiesTypes(
   System.int selTypes
)
```

### Parameters

- `selTypes`: Type of entities as defined in [gtPslSelectionType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtPslSelectionType_e.html)

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SetSelectEntitiesTypes](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SetSelectEntitiesTypes.html).

## Examples

[Run PowerSelect (VBA)](Run_PowerSelect_VB6.htm)
[Select and Get Number of Edges, Loops, Faces, and Features (VBA)](Select_and_Get_Number_of_Edges,_Loops,_Faces,_and_Features_Example_VB6.htm)

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)
[IPowerSelect::GetSelectEntitiesTypes Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetSelectEntitiesTypes.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
