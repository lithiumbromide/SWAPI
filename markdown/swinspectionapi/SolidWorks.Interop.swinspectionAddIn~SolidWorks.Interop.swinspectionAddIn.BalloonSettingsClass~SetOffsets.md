---
title: "SetOffsets Method (BalloonSettingsClass)"
project: "SOLIDWORKS Inspection API Help"
interface: "BalloonSettingsClass"
member: "SetOffsets"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettingsClass~SetOffsets.html"
---

# SetOffsets Method (BalloonSettingsClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function SetOffsets( _
   ByVal Type As System.Integer, _
   ByVal IsVisible As System.Boolean, _
   ByVal X_Offset As System.Double, _
   ByVal Y_Offset As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As BalloonSettingsClass
Dim Type As System.Integer
Dim IsVisible As System.Boolean
Dim X_Offset As System.Double
Dim Y_Offset As System.Double
Dim value As System.Boolean

value = instance.SetOffsets(Type, IsVisible, X_Offset, Y_Offset)
```

### C#

```csharp
public virtual System.bool SetOffsets(
   System.int Type,
   System.bool IsVisible,
   System.double X_Offset,
   System.double Y_Offset
)
```

### C++/CLI

```cpp
public:
virtual System.bool SetOffsets(
   System.int Type,
   System.bool IsVisible,
   System.double X_Offset,
   System.double Y_Offset
)
```

### Parameters

- `Type`:
- `IsVisible`:
- `X_Offset`:
- `Y_Offset`:

## See Also

[BalloonSettingsClass Class](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettingsClass.html)
[BalloonSettingsClass Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettingsClass_members.html)
