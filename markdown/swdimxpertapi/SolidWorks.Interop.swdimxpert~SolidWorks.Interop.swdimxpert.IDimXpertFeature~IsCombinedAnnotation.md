---
title: "IsCombinedAnnotation Method (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "IsCombinedAnnotation"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~IsCombinedAnnotation.html"
---

# IsCombinedAnnotation Method (IDimXpertFeature)

Gets whether the pre-selected annotation is combined or not.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCombinedAnnotation() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
Dim value As System.Boolean

value = instance.IsCombinedAnnotation()
```

### C#

```csharp
System.bool IsCombinedAnnotation()
```

### C++/CLI

```cpp
System.bool IsCombinedAnnotation();
```

### Return Value

True if combined, false if not

## VBA Syntax

See [DimXpertFeature::IsCombinedAnnotation](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFeature~IsCombinedAnnotation.html).

## Remarks

A combined annotation shares a leader in the user interface.

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)
[IDimXpertFeature::SetCombineAnnotation Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~SetCombineAnnotation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
