---
title: "GetActiveLineStyle Method (ILineStyleManager)"
project: ""
interface: "ILineStyleManager"
member: "GetActiveLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetActiveLineStyle.html"
---

# GetActiveLineStyle Method (ILineStyleManager)

Gets the active simple LineStyle loaded in this document.

## Syntax

### Visual Basic

```vb
Function GetActiveLineStyle() As LineStyle
```

### C#

```csharp
LineStyle GetActiveLineStyle()
```

### JScript

```
function GetActiveLineStyle() : LineStyle;
```

### Managed Extensions for C++

```
LineStyle* GetActiveLineStyle();
```

### C++/CLI

```cpp
LineStyle^ GetActiveLineStyle();
```

### Return Value

Active simple [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) loaded in this document

## Remarks

You must [create simple LineStyles](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateLineStyle.html) and [load simple LineStyles](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~LoadLineStyle.html) before you can get them.

## See Also

[ILineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager.html)
[ILineStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager_members.html)
[ILineStyleManager::GetLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetLineStyle.html)
[ILineStyleManager::GetLineStyles Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetLineStyles.html)
[ILineStyleManager::RemoveLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~RemoveLineStyle.html)

## Availability

DraftSight V1R4.0
