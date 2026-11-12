---
title: "FindReplaceAnnotations Property (gtcocswUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilities"
member: "FindReplaceAnnotations"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities~FindReplaceAnnotations.html"
---

# FindReplaceAnnotations Property (gtcocswUtilities)

Gets an IFindReplaceAnnotations object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FindReplaceAnnotations As gtcocswFindReplaceAnnotations
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilities
Dim value As gtcocswFindReplaceAnnotations

value = instance.FindReplaceAnnotations
```

### C#

```csharp
gtcocswFindReplaceAnnotations FindReplaceAnnotations {get;}
```

### C++/CLI

```cpp
property gtcocswFindReplaceAnnotations^ FindReplaceAnnotations {
   gtcocswFindReplaceAnnotations^ get();
}
```

### Property Value

Pointer to [IFindReplaceAnnotations](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations.html) object

## VBA Syntax

See [IUtilities::FindReplaceAnnotations](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~FindReplaceAnnotations.html).

## See Also

[gtcocswUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities.html)
[gtcocswUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
