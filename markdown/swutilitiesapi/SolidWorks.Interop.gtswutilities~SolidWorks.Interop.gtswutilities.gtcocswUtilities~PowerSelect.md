---
title: "PowerSelect Property (gtcocswUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilities"
member: "PowerSelect"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities~PowerSelect.html"
---

# PowerSelect Property (gtcocswUtilities)

Gets an IPowerSelect object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PowerSelect As gtcocswPowerSelect
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilities
Dim value As gtcocswPowerSelect

value = instance.PowerSelect
```

### C#

```csharp
gtcocswPowerSelect PowerSelect {get;}
```

### C++/CLI

```cpp
property gtcocswPowerSelect^ PowerSelect {
   gtcocswPowerSelect^ get();
}
```

### Property Value

Pointer to an [IPowerSelect](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect.html) object

## VBA Syntax

See [IUtilities::PowerSelect](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~PowerSelect.html).

## See Also

[gtcocswUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities.html)
[gtcocswUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
