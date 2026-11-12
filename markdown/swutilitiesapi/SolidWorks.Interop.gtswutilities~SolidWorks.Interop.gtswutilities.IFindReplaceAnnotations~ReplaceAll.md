---
title: "ReplaceAll Method (IFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "IFindReplaceAnnotations"
member: "ReplaceAll"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~ReplaceAll.html"
---

# ReplaceAll Method (IFindReplaceAnnotations)

Replaces all matching occurrences of the text returned by [IFindReplaceAnnotations::FindText](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~FindText.html) with the text specified by [IFindReplaceAnnotations::ReplaceText](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~ReplaceText.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceAll() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFindReplaceAnnotations
Dim value As System.Integer

value = instance.ReplaceAll()
```

### C#

```csharp
System.int ReplaceAll()
```

### C++/CLI

```cpp
System.int ReplaceAll();
```

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IFindReplaceAnnotations::ReplaceAll](ms-its:swutilitiesapivb6.chm::/swutilities~IFindReplaceAnnotations~ReplaceAll.html).

## See Also

[IFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations.html)
[IFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations_members.html)
[IFindReplaceAnnotations::Replace Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~Replace.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
