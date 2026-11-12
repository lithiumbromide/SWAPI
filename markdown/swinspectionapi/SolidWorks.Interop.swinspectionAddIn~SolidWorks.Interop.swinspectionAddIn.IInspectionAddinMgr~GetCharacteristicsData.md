---
title: "GetCharacteristicsData Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "GetCharacteristicsData"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetCharacteristicsData.html"
---

# GetCharacteristicsData Method (IInspectionAddinMgr)

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
Dim instance As IInspectionAddinMgr
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

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
