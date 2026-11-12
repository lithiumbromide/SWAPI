---
title: "GetLineStyle Method (ILineStyleManager)"
project: ""
interface: "ILineStyleManager"
member: "GetLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetLineStyle.html"
---

# GetLineStyle Method (ILineStyleManager)

Gets the specified simple LineStyle loaded in this document.

## Syntax

### Visual Basic

```vb
Function GetLineStyle( _
   ByVal Name As System.String _
) As LineStyle
```

### C#

```csharp
LineStyle GetLineStyle(
   System.string Name
)
```

### JScript

```
function GetLineStyle(
   Name : System.String
) : LineStyle;
```

### Managed Extensions for C++

```
LineStyle* GetLineStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
LineStyle^ GetLineStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the loaded simple LineStyle to get

### Return Value

Simple [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html)

## Examples

[Load and Activate LineStyles (C#)](Load_and_Activate_LineStyles_Example_CSharp.htm)
[Load and Activate LineStyles (VB.NET)](Laod_and_Activate_LineStyles_Example_VBNET.htm)
[Load and Activate LineStyles (VBA)](Load_and_Activate_LineStyles_Example_VBA.htm)
[Load and Activate LineStyles (JavaScript)](Load_and_Activate_LineStyles_Example_JS.htm)

## Remarks

You must [create simple LineStyles](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateLineStyle.html) and [load simple LineStyles](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~LoadLineStyle.html) before you can get them.

## See Also

[ILineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager.html)
[ILineStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager_members.html)
[ILineStyleManager::GetActiveLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetActiveLineStyle.html)
[ILineStyleManager::GetLineStyles Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetLineStyles.html)
[ILineStyleManager::RemoveLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~RemoveLineStyle.html)

## Availability

DraftSight V1R4.0
