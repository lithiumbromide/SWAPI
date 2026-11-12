---
title: "PowerSelect Property (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "PowerSelect"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~PowerSelect.html"
---

# PowerSelect Property (IUtilities)

Gets an IPowerSelect object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PowerSelect As gtcocswPowerSelect
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilities
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

## Examples

[Select and Get Number of Edges, Loops, Faces, and Features (VBA)](Select_and_Get_Number_of_Edges,_Loops,_Faces,_and_Features_Example_VB6.htm)

## See Also

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
