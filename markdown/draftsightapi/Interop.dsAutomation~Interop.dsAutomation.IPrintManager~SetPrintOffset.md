---
title: "SetPrintOffset Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "SetPrintOffset"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetPrintOffset.html"
---

# SetPrintOffset Method (IPrintManager)

Sets the margins for print offset.

## Syntax

### Visual Basic

```vb
Sub SetPrintOffset( _
   ByVal XOffset As System.Double, _
   ByVal YOffset As System.Double _
)
```

### C#

```csharp
void SetPrintOffset(
   System.double XOffset,
   System.double YOffset
)
```

### JScript

```
function SetPrintOffset(
   XOffset : System.double,
   YOffset : System.double
);
```

### Managed Extensions for C++

```
void SetPrintOffset(
   System.double XOffset,
   System.double YOffset
)
```

### C++/CLI

```cpp
void SetPrintOffset(
   System.double XOffset,
   System.double YOffset
)
```

### Parameters

- `XOffset`: X margin for print offset
- `YOffset`: Y margin for print offset

## Remarks

Units (inches or millimeters) for the margins for print offset are dependent on the specified [paper size](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html).

[IPrintManager::PrintOnCenter](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PrintOnCenter.html) must be set to false for the margins for print offset to be used.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::GetPrintOffset Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPrintOffset.html)

## Availability

DraftSight V1R1
