---
title: "AddCharacteristics Method (InspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgr"
member: "AddCharacteristics"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr~AddCharacteristics.html"
---

# AddCharacteristics Method (InspectionAddinMgr)

Adds characteristics for the specified annotations.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCharacteristics( _
   ByRef AnnotationsIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionAddinMgr
Dim AnnotationsIn As System.Object
Dim value As System.Object

value = instance.AddCharacteristics(AnnotationsIn)
```

### C#

```csharp
System.object AddCharacteristics(
   ref System.object AnnotationsIn
)
```

### C++/CLI

```cpp
System.Object^ AddCharacteristics(
   System.Object^% AnnotationsIn
)
```

### Parameters

- `AnnotationsIn`: Array of annotations

### Return Value

[ICharacteristicsData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## Remarks

This method is valid only if [IInspectionProjectData::Extraction](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~Extraction.html) is set to [swiCharacteristicInfoExtraction_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiCharacteristicInfoExtraction_e.html).swiExtraction_Manual.

## See Also

[InspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr.html)
[InspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
