---
title: "SetCombineAnnotation Method (IDimXpertFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertFeature"
member: "SetCombineAnnotation"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~SetCombineAnnotation.html"
---

# SetCombineAnnotation Method (IDimXpertFeature)

Sets whether the pre-selected annotation is a combined annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCombineAnnotation( _
   ByVal Combine As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertFeature
Dim Combine As System.Boolean
Dim value As System.Integer

value = instance.SetCombineAnnotation(Combine)
```

### C#

```csharp
System.int SetCombineAnnotation(
   System.bool Combine
)
```

### C++/CLI

```cpp
System.int SetCombineAnnotation(
   System.bool Combine
)
```

### Parameters

- `Combine`: True to combine the annotation, false to not

### Return Value

Result code as defined in [swDimXpertCombineAnnotation_e](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.swDimXpertCombineAnnotation_e.html)

## VBA Syntax

See [DimXpertFeature::SetCombineAnnotation](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertFeature~SetCombineAnnotation.html).

## See Also

[IDimXpertFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature.html)
[IDimXpertFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature_members.html)
[IDimXpertFeature::IsCombinedAnnotation Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertFeature~IsCombinedAnnotation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
