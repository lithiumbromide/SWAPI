---
title: "AddOrEditBalloons Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "AddOrEditBalloons"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~AddOrEditBalloons.html"
---

# AddOrEditBalloons Method (IInspectionAddinMgr)

Specifies settings for adding or modifying balloons in a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddOrEditBalloons( _
   ByVal BalloonSettings As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim BalloonSettings As System.Object
Dim value As System.Boolean

value = instance.AddOrEditBalloons(BalloonSettings)
```

### C#

```csharp
System.bool AddOrEditBalloons(
   System.object BalloonSettings
)
```

### C++/CLI

```cpp
System.bool AddOrEditBalloons(
   System.Object^ BalloonSettings
)
```

### Parameters

- `BalloonSettings`: [IBalloonSettings](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)

### Return Value

True if balloon settings successfully applied, false if not

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## Remarks

This method is valid only:

- for ballooned drawings.
- when IInspectionProjectData::Extraction is set to [swiCharacteristicInfoExtraction_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiCharacteristicInfoExtraction_e.html).swiExtraction_Manual.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
