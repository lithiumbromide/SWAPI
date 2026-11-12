---
title: "SetSelectEntitiesTypes Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "SetSelectEntitiesTypes"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~SetSelectEntitiesTypes.html"
---

# SetSelectEntitiesTypes Method (gtcocswPowerSelect)

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
Dim instance As gtcocswPowerSelect
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

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
