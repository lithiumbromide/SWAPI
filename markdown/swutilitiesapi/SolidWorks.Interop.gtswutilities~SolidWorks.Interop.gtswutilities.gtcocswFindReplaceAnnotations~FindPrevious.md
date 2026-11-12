---
title: "FindPrevious Method (gtcocswFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswFindReplaceAnnotations"
member: "FindPrevious"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations~FindPrevious.html"
---

# FindPrevious Method (gtcocswFindReplaceAnnotations)

Finds the previous occurrence of the text specified by [IFindReplaceAnnotations::FindText](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~FindText.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FindPrevious() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswFindReplaceAnnotations
Dim value As System.Integer

value = instance.FindPrevious()
```

### C#

```csharp
System.int FindPrevious()
```

### C++/CLI

```cpp
System.int FindPrevious();
```

### Return Value

Error code as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IFindReplaceAnnotations::FindPrevious](ms-its:swutilitiesapivb6.chm::/swutilities~IFindReplaceAnnotations~FindPrevious.html).

## Remarks

You can use [IFindReplaceAnnotations::AnnotationFilter](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~AnnotationFilter.html) to filter your search and [IFindReplaceAnnotations::options](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~options.html) to further refine your search.

## See Also

[gtcocswFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations.html)
[gtcocswFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations_members.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
