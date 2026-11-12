---
title: "FindPrevious Method (IFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "IFindReplaceAnnotations"
member: "FindPrevious"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~FindPrevious.html"
---

# FindPrevious Method (IFindReplaceAnnotations)

Finds the previous occurrence of the text specified by [IFindReplaceAnnotations::FindText](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~FindText.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FindPrevious() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFindReplaceAnnotations
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

[IFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations.html)
[IFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations_members.html)
[IFindReplaceAnnotations::FindNext Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~FindNext.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
