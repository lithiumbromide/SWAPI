---
title: "GetShowHiddenEntities Method (IPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "IPowerSelect"
member: "GetShowHiddenEntities"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect~GetShowHiddenEntities.html"
---

# GetShowHiddenEntities Method (IPowerSelect)

Gets whether to show both non-hidden and hidden entities or to only show non-hidden entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetShowHiddenEntities( _
   ByRef lErrorcode As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPowerSelect
Dim lErrorcode As System.Integer
Dim value As System.Boolean

value = instance.GetShowHiddenEntities(lErrorcode)
```

### C#

```csharp
System.bool GetShowHiddenEntities(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.bool GetShowHiddenEntities(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error code as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

True to show both non-hidden and hidden entities, false to only show non-hidden entities

## VBA Syntax

See [IPowerSelect::GetShowHiddenEntities](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~GetShowHiddenEntities.html).

## Remarks

Use [IPowerSelect::SetShowHiddenEntities](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect~SetShowHiddenEntities.html) to set whether or not to show both non-hidden and hidden entities or to only show non-hidden entities.

This method is the equivalent to the user-interface Show features of hidden body option on the Power Select dialog.

## See Also

[IPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect.html)
[IPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
