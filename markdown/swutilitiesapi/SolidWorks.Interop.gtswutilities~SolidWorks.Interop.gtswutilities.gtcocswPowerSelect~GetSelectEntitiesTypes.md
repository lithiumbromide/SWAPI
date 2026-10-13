---
title: "GetSelectEntitiesTypes Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "GetSelectEntitiesTypes"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~GetSelectEntitiesTypes.html"
---

# GetSelectEntitiesTypes Method (gtcocswPowerSelect)

Gets the types of entities set in this PowerSelect session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectEntitiesTypes( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.GetSelectEntitiesTypes(lErrorcode)
```

### C#

```csharp
System.int GetSelectEntitiesTypes(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int GetSelectEntitiesTypes(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Type of entities as defined in [gtPslSelectionType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtPslSelectionType_e.html)

## VBA Syntax

See [IPowerSelect::GetSelectEntitiesTypes](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetSelectEntitiesTypes.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
