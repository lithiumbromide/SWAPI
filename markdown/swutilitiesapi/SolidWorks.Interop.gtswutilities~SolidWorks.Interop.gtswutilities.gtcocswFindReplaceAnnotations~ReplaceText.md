---
title: "ReplaceText Property (gtcocswFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswFindReplaceAnnotations"
member: "ReplaceText"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations~ReplaceText.html"
---

# ReplaceText Property (gtcocswFindReplaceAnnotations)

Gets or sets the text with which to replace the text returned by [IFindReplaceAnnotations::FindText](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~FindText.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReplaceText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswFindReplaceAnnotations
Dim value As System.String

instance.ReplaceText = value

value = instance.ReplaceText
```

### C#

```csharp
System.string ReplaceText {get; set;}
```

### C++/CLI

```cpp
property System.String^ ReplaceText {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Text with which to replace the text returned by [IFindReplaceAnnotations::FindText](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~FindText.html)

## VBA Syntax

See [IFindReplaceAnnotations::ReplaceText](ms-its:swutilitiesapivb6.chm::/swutilities~IFindReplaceAnnotations~ReplaceText.html).

## Remarks

| To... | Call... |
| --- | --- |
| Replace the text returned by IFindReplaceAnnotations::FindText with the text specified by this property | IFindReplaceAnnotations::Replace |
| Replace all matching occurrences of the text returned by IFindReplaceAnnotations::FindText with the text specified by this property | IFindReplaceAnnotations::ReplaceAll |

## See Also

[gtcocswFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations.html)
[gtcocswFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFindReplaceAnnotations_members.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
