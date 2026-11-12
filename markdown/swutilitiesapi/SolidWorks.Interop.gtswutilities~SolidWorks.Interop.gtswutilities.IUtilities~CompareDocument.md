---
title: "CompareDocument Property (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "CompareDocument"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~CompareDocument.html"
---

# CompareDocument Property (IUtilities)

Gets an ICompareDocument object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CompareDocument As gtcocswCompareDocument
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilities
Dim value As gtcocswCompareDocument

value = instance.CompareDocument
```

### C#

```csharp
gtcocswCompareDocument CompareDocument {get;}
```

### C++/CLI

```cpp
property gtcocswCompareDocument^ CompareDocument {
   gtcocswCompareDocument^ get();
}
```

### Property Value

Pointer to an [ICompareDocument](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareDocument.html) object

## VBA Syntax

See [IUtilities::CompareDocument](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~CompareDocument.html).

## See Also

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
