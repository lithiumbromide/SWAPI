---
title: "PaperSize Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "PaperSize"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html"
---

# PaperSize Property (IPrintManager)

Gets or sets the name of the size of the paper.

## Syntax

### Visual Basic

```vb
Property PaperSize As System.String
```

### C#

```csharp
System.string PaperSize {get; set;}
```

### JScript

```
function get,set PaperSize : System.String
```

### Managed Extensions for C++

```
__property System.string* get_PaperSize();
__property void set_PaperSize(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ PaperSize {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the size of the paper

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## Remarks

Use [IPrintManager::AvailablePaperSizes](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~AvailablePaperSizes.html) to determine which paper sizes are available for your printer.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::GetPaperSize Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPaperSize.html)
[IPrintManager::SetClosestValidPaperSize Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetClosestValidPaperSize.html)

## Availability

DraftSight V1R1
