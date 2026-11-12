---
title: "options Property (gtcocswFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswFindReplaceAnnotations"
member: "options"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations~options.html"
---

# options Property (gtcocswFindReplaceAnnotations)

Gets or sets the options to use to filter the search for this find and replace annotation operation.

## Syntax

### Visual Basic (Declaration)

```vb
Property options As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswFindReplaceAnnotations
Dim value As System.Integer

instance.options = value

value = instance.options
```

### C#

```csharp
System.int options {get; set;}
```

### C++/CLI

```cpp
property System.int options {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Options as described by [gtFraOptionType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtFraOptionType_e.html)

## VBA Syntax

See [IFindReplaceAnnotations::options](ms-its:swutilitiesapivb6.chm::/swutilities~IFindReplaceAnnotations~options.html).

## See Also

[gtcocswFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations.html)
[gtcocswFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations_members.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
