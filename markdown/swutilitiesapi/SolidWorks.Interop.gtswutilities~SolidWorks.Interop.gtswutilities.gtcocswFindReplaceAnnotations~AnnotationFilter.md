---
title: "AnnotationFilter Property (gtcocswFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswFindReplaceAnnotations"
member: "AnnotationFilter"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations~AnnotationFilter.html"
---

# AnnotationFilter Property (gtcocswFindReplaceAnnotations)

Gets or sets the type of annotations to find.

## Syntax

### Visual Basic (Declaration)

```vb
Property AnnotationFilter As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswFindReplaceAnnotations
Dim value As System.Integer

instance.AnnotationFilter = value

value = instance.AnnotationFilter
```

### C#

```csharp
System.int AnnotationFilter {get; set;}
```

### C++/CLI

```cpp
property System.int AnnotationFilter {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of annotations to find as defined by [gtFraFilterType_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtFraFilterType_e.html)

## VBA Syntax

See [IFindReplaceAnnotations::AnnotationFilter](ms-its:swutilitiesapivb6.chm::/swutilities~IFindReplaceAnnotations~AnnotationFilter.html).

## See Also

[gtcocswFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations.html)
[gtcocswFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations_members.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
