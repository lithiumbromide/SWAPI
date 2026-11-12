---
title: "GetAvailablePrintStyleTables Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "GetAvailablePrintStyleTables"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetAvailablePrintStyleTables.html"
---

# GetAvailablePrintStyleTables Method (IPrintManager)

Gets the currently available PrintStyle tables.

## Syntax

### Visual Basic

```vb
Sub GetAvailablePrintStyleTables( _
   ByRef PrintStyleTablesStrArray As System.Object _
)
```

### C#

```csharp
void GetAvailablePrintStyleTables(
   out System.object PrintStyleTablesStrArray
)
```

### JScript

```
function GetAvailablePrintStyleTables(
   PrintStyleTablesStrArray : System.Object
);
```

### Managed Extensions for C++

```
void GetAvailablePrintStyleTables(
   [PARAMFLAG::Out] System.Object* PrintStyleTablesStrArray
)
```

### C++/CLI

```cpp
void GetAvailablePrintStyleTables(
   [Out] System.Object^ PrintStyleTablesStrArray
)
```

### Parameters

- `PrintStyleTablesStrArray`: Array of the names of the currently available PrintStyle tables

## Examples

[Get and Set Print Options (VB.NET)](Get_and_Set_Print_Options_Example_VBNET.htm)
[Get and Set Print Options (C#)](Get_and_Set_Print_Options_Example_CSharp.htm)

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::StyleTable Property ()](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~StyleTable.html)

## Availability

DraftSight 2018 SP0
