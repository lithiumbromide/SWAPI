---
title: "SetOffsets Method (IBalloonSettings)"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: "SetOffsets"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings~SetOffsets.html"
---

# SetOffsets Method (IBalloonSettings)

Sets whether to balloon the specified offset type in the document and gets the current offsets for the specified offset type.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOffsets( _
   ByVal Type As System.Integer, _
   ByVal IsVisible As System.Boolean, _
   ByVal X_Offset As System.Double, _
   ByVal Y_Offset As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
Dim Type As System.Integer
Dim IsVisible As System.Boolean
Dim X_Offset As System.Double
Dim Y_Offset As System.Double
Dim value As System.Boolean

value = instance.SetOffsets(Type, IsVisible, X_Offset, Y_Offset)
```

### C#

```csharp
System.bool SetOffsets(
   System.int Type,
   System.bool IsVisible,
   System.double X_Offset,
   System.double Y_Offset
)
```

### C++/CLI

```cpp
System.bool SetOffsets(
   System.int Type,
   System.bool IsVisible,
   System.double X_Offset,
   System.double Y_Offset
)
```

### Parameters

- `Type`: Offset type as defined by [swiBalloonSettingsOffsetTypes_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiBalloonSettingsOffsetTypes_e.html)
- `IsVisible`: True to balloon the offset type in the document, false to just include it in the inspection report
- `X_Offset`: X offset for the default location of the balloons
- `Y_Offset`: Y offset for the default location of the balloons

### Return Value

True if offset settings successfully set, false if not

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings_members.html) methods.

## Remarks

X_Offset and Y_Offset are from the upper left-hand corner of the attribute to the upper left-hand corner of the balloon. The offsets can be positive or negative numbers.

For more information, see the Ballooning Settings PropertyManager - Offsets section of the **SOLIDWORKS Inspection Add-in user-interface help > SOLIDWORKS Inspection > SOLIDWORKS Inspection Add-in > Getting Started > Balloons** topic.

## See Also

[IBalloonSettings Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html)
[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
