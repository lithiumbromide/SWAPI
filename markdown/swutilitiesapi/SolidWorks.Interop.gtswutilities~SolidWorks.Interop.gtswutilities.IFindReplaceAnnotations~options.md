---
title: "options Property (IFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "IFindReplaceAnnotations"
member: "options"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~options.html"
---

# options Property (IFindReplaceAnnotations)

Gets or sets the options to use to filter the search for this find and replace annotation operation.

## Syntax

### Visual Basic (Declaration)

```vb
Property options As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFindReplaceAnnotations
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

[IFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations.html)
[IFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations_members.html)
[IFindReplaceAnnotations::AnnotationFilter Property](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~AnnotationFilter.html)
[IFindReplaceAnnotations::FindNext Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~FindNext.html)
[IFindReplaceAnnotations::FindPrevious Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~FindPrevious.html)
[IFindReplaceAnnotations::FindText Property](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~FindText.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
