---
title: "FindReplaceAnnotations Property (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "FindReplaceAnnotations"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~FindReplaceAnnotations.html"
---

# FindReplaceAnnotations Property (IUtilities)

Gets an IFindReplaceAnnotations object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FindReplaceAnnotations As gtcocswFindReplaceAnnotations
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilities
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

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
