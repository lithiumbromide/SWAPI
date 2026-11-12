---
title: "Printer Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "Printer"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~Printer.html"
---

# Printer Property (IPrintManager)

Gets or sets the name of the printer to use.

## Syntax

### Visual Basic

```vb
Property Printer As System.String
```

### C#

```csharp
System.string Printer {get; set;}
```

### JScript

```
function get,set Printer : System.String
```

### Managed Extensions for C++

```
__property System.string* get_Printer();
__property void set_Printer(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ Printer {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the printer to use (see **Remarks**)

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## Remarks

Possible printer names include all of the output devices configured on your system ([IPrintManager::GetAvailablePrinters](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetAvailablePrinters.html)) and the following built-in plotters that print to files in the specified format:

- PDF
- JPG
- PNG
- SVG

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::GetAvailablePrinters Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetAvailablePrinters.html)

## Availability

DraftSight V1R1
