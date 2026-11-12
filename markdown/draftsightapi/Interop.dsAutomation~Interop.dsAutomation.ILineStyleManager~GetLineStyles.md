---
title: "GetLineStyles Method (ILineStyleManager)"
project: ""
interface: "ILineStyleManager"
member: "GetLineStyles"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetLineStyles.html"
---

# GetLineStyles Method (ILineStyleManager)

Gets all of the simple LineStyles loaded in this document.

## Syntax

### Visual Basic

```vb
Function GetLineStyles() As System.Object
```

### C#

```csharp
System.object GetLineStyles()
```

### JScript

```
function GetLineStyles() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetLineStyles();
```

### C++/CLI

```cpp
System.Object^ GetLineStyles();
```

### Return Value

Array of the simple [LineStyles](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) loaded in this document

## Remarks

You must [create simple LineStyles](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateLineStyle.html) and [load simple LineStyles](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~LoadLineStyle.html) before you can get them.

## See Also

[ILineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager.html)
[ILineStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager_members.html)
[ILineStyleManager::GetActiveLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetActiveLineStyle.html)
[ILineStyleManager::GetLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetLineStyle.html)
[ILineStyleManager::RemoveLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~RemoveLineStyle.html)

## Availability

DraftSight V1R4.0
