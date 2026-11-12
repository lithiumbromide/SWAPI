---
title: "GetCharacteristicsData Method (InspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgr"
member: "GetCharacteristicsData"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr~GetCharacteristicsData.html"
---

# GetCharacteristicsData Method (InspectionAddinMgr)

Gets the specified characteristic data.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCharacteristicsData( _
   ByVal CharId As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionAddinMgr
Dim CharId As System.Double
Dim value As System.Object

value = instance.GetCharacteristicsData(CharId)
```

### C#

```csharp
System.object GetCharacteristicsData(
   System.double CharId
)
```

### C++/CLI

```cpp
System.Object^ GetCharacteristicsData(
   System.double CharId
)
```

### Parameters

- `CharId`: ID of characteristic to retrieve

### Return Value

[ICharacteristicsData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html)

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[InspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr.html)
[InspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
