---
title: "StyleTable Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "StyleTable"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~StyleTable.html"
---

# StyleTable Property (IPrintManager)

Gets or sets the name of the PrintStyle table.

## Syntax

### Visual Basic

```vb
Property StyleTable As System.String
```

### C#

```csharp
System.string StyleTable {get; set;}
```

### JScript

```
function get,set StyleTable : System.String
```

### Managed Extensions for C++

```
__property System.string* get_StyleTable();
__property void set_StyleTable(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ StyleTable {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the PrintStyle table

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## Remarks

Before setting this property, call [IPrintManager::GetAvailablePrintStyleTables](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetAvailablePrintStyleTables.html).

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1
