---
title: "Replace Method (IFindReplaceAnnotations)"
project: "SOLIDWORKS Utilities API Help"
interface: "IFindReplaceAnnotations"
member: "Replace"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~Replace.html"
---

# Replace Method (IFindReplaceAnnotations)

Replaces the value returned by [IFindReplaceAnnotations::FindText](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~FindText.html) with the text specified by [IFindReplaceAnnotations::ReplaceText](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFindReplaceAnnotations~ReplaceText.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Replace() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFindReplaceAnnotations
Dim value As System.Integer

value = instance.Replace()
```

### C#

```csharp
System.int Replace()
```

### C++/CLI

```cpp
System.int Replace();
```

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IFindReplaceAnnotations::Replace](ms-its:swutilitiesapivb6.chm::/swutilities~IFindReplaceAnnotations~Replace.html).

## See Also

[IFindReplaceAnnotations Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations.html)
[IFindReplaceAnnotations Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations_members.html)
[IFindReplaceAnnotations::ReplaceAll Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFindReplaceAnnotations~ReplaceAll.html)

## Availability

SOLIDWORKS Utilities API 2008 FCS
