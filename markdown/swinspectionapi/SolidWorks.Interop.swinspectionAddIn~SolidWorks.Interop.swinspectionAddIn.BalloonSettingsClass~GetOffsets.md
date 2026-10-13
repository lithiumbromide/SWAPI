---
title: "GetOffsets Method (BalloonSettingsClass)"
project: "SOLIDWORKS Inspection API Help"
interface: "BalloonSettingsClass"
member: "GetOffsets"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.BalloonSettingsClass~GetOffsets.html"
---

# GetOffsets Method (BalloonSettingsClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function GetOffsets( _
   ByVal Type As System.Integer, _
   ByRef IsVisible As System.Boolean, _
   ByRef X_Offset As System.Double, _
   ByRef Y_Offset As System.Double _
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

value = instance.GetOffsets(Type, IsVisible, X_Offset, Y_Offset)
```

### C#

```csharp
public virtual System.bool GetOffsets(
   System.int Type,
   out System.bool IsVisible,
   out System.double X_Offset,
   out System.double Y_Offset
)
```

### C++/CLI

```cpp
public:
virtual System.bool GetOffsets(
   System.int Type,
   [Out] System.bool IsVisible,
   [Out] System.double X_Offset,
   [Out] System.double Y_Offset
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
