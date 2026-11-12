---
title: "PrintStyleTable Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "PrintStyleTable"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~PrintStyleTable.html"
---

# PrintStyleTable Property (IExportSettings)

Gets or sets the print style table.

## Syntax

### Visual Basic

```vb
Property PrintStyleTable As System.String
```

### C#

```csharp
System.string PrintStyleTable {get; set;}
```

### JScript

```
function get,set PrintStyleTable : System.String
```

### Managed Extensions for C++

```
__property System.string* get_PrintStyleTable();
__property void set_PrintStyleTable(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ PrintStyleTable {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Print style table; Nothing or null by default

## Examples

See the [IExportSettings](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html) examples.

## Remarks

To set this property, call [IPrintManager::GetAvailablePrintStyleTables](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetAvailablePrintStyleTables.html) to get the currently available print style tables.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2018 SP0
