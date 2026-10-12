---
title: "FindText Property (gtcocswFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswFindReplaceAnnotations"
member: "FindText"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations~FindText.html"
---

# FindText Property (gtcocswFindReplaceAnnotations)

Gets or sets the text to find.

## Syntax

### Visual Basic (Declaration)

```vb
Property FindText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswFindReplaceAnnotations
Dim value As System.String

instance.FindText = value

value = instance.FindText
```

### C#

```csharp
System.string FindText {get; set;}
```

### C++/CLI

```cpp
property System.String^ FindText {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Text to find

## VBA Syntax

See [IFindReplaceAnnotations::FindText](ms-its:swutilitiesapivb6.chm::/swutilities~IFindReplaceAnnotations~FindText.html).

## Remarks

| To... | Call... |
| --- | --- |
| Find the next occurrence of pVal | IFindReplaceAnnotations::FindNext |
| Find the previous occurrence of pVal | IFindReplaceAnnotations::FindPrevious |
| Replace the text in this occurrence with the text specified by IFindReplaceAnnotations::ReplaceText | IFindReplaceAnnotations::Replace |
| Replace the text in all matching occurrences with the text specified by IFindReplaceAnnotations::ReplaceText | IFindReplaceAnnotations::Replace |

## See Also

[gtcocswFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations.html)
[gtcocswFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations_members.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
