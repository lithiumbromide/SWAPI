---
title: "IInspectionProjectData Interface"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: ""
kind: "interface"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html"
---

# IInspectionProjectData Interface

Allows access to inspection project data.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IInspectionProjectData
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
```

### C#

```csharp
public interface IInspectionProjectData
```

### C++/CLI

```cpp
public interface class IInspectionProjectData
```

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData.html).

## Remarks

This interface sets initial properties before the inspection project is created. Use [ICharacteristicsData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.ICharacteristicsData.html) and [IBalloonSettings](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IBalloonSettings.html) to modify these properties for individual characteristics and balloons after the inspection project is created.

For more information, see the **SOLIDWORKS Inspection Add-in user-interface help > SOLIDWORKS Inspection > SOLIDWORKS Inspection Add-in > Getting Started > Creating an Inspection Project > Create Inspection Project PropertyManager** topic.

## Accessors

[IInspectionAddinMgr::CreateInspectionProjectData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~CreateInspectionProjectData.html)

[IInspectionAddinMgr::GetInspectionProjectData](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetInspectionProjectData.html)

## See Also

[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)
[SolidWorks.Interop.swinspectionAddIn Namespace](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn_namespace.html)
