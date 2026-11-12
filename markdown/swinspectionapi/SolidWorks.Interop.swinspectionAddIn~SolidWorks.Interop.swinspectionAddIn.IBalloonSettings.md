---
title: "IBalloonSettings Interface"
project: "SOLIDWORKS Inspection API Help"
interface: "IBalloonSettings"
member: ""
kind: "interface"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html"
---

# IBalloonSettings Interface

Allows access to inspection balloon settings.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IBalloonSettings
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonSettings
```

### C#

```csharp
public interface IBalloonSettings
```

### C++/CLI

```cpp
public interface class IBalloonSettings
```

## VBA Syntax

See [BalloonSettings](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~BalloonSettings.html).

## Remarks

This interface:

- is valid only after the inspection project is created and the model has been ballooned.
- can be used to add or edit balloons in ballooned drawings only.
- analogous to the Ballooning Settings PropertyManager that displays when you select **Tools > SOLIDWORKS Inspection > Add/Edit Balloons**.

For more information, see the **SOLIDWORKS Inspection Add-in user-interface help > SOLIDWORKS Inspection > SOLIDWORKS Inspection Add-in > Getting Started > Balloons** topic.

## Accessors

[IInspectionAddinMgr::GetBalloonSettings](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetBalloonSettings.html)

## See Also

[IBalloonSettings Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings_members.html)
[SolidWorks.Interop.swinspectionAddIn Namespace](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn_namespace.html)
