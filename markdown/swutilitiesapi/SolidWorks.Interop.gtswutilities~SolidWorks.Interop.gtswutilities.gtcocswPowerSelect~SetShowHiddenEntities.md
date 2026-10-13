---
title: "SetShowHiddenEntities Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "SetShowHiddenEntities"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~SetShowHiddenEntities.html"
---

# SetShowHiddenEntities Method (gtcocswPowerSelect)

Sets whether to show both non-hidden and hidden entities or to show only non-hidden entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetShowHiddenEntities( _
   ByVal varShow As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim varShow As System.Boolean
Dim value As System.Integer

value = instance.SetShowHiddenEntities(varShow)
```

### C#

```csharp
System.int SetShowHiddenEntities(
   System.bool varShow
)
```

### C++/CLI

```cpp
System.int SetShowHiddenEntities(
   System.bool varShow
)
```

### Parameters

- `varShow`: True to show both non-hidden and hidden entities, false to show only non-hidden entities

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::SetShowHiddenEntities](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~SetShowHiddenEntities.html).

## Remarks

Use [IPowerSelect::GetShowHiddenEntities](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect~GetShowHiddenEntities.html) to get whether or not to show both non-hidden and hidden entities or to show only non-hidden entities.

This method is the equivalent to the user-interface Show features of hidden body option on the Power Select dialog.

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
