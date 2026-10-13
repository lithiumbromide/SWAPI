---
title: "AnnotationFilter Property (IFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "IFindReplaceAnnotations"
member: "AnnotationFilter"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~AnnotationFilter.html"
---

# AnnotationFilter Property (IFindReplaceAnnotations)

Gets or sets the type of annotations to find.

## Syntax

### Visual Basic (Declaration)

```vb
Property AnnotationFilter As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFindReplaceAnnotations
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

[IFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations.html)
[IFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations_members.html)
[IFindReplaceAnnotations::FindNext Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~FindNext.html)
[IFindReplaceAnnotations::FindPrevious Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~FindPrevious.html)
[IFindReplaceAnnotations::FindText Property](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~FindText.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
