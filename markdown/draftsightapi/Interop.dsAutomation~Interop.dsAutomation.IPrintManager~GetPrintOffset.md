---
title: "GetPrintOffset Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "GetPrintOffset"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPrintOffset.html"
---

# GetPrintOffset Method (IPrintManager)

Gets the margins for print offset.

## Syntax

### Visual Basic

```vb
Sub GetPrintOffset( _
   ByRef XOffset As System.Double, _
   ByRef YOffset As System.Double _
)
```

### C#

```csharp
void GetPrintOffset(
   out System.double XOffset,
   out System.double YOffset
)
```

### JScript

```
function GetPrintOffset(
   XOffset : System.double,
   YOffset : System.double
);
```

### Managed Extensions for C++

```
void GetPrintOffset(
   [PARAMFLAG::Out] System.double XOffset,
   [PARAMFLAG::Out] System.double YOffset
)
```

### C++/CLI

```cpp
void GetPrintOffset(
   [Out] System.double XOffset,
   [Out] System.double YOffset
)
```

### Parameters

- `XOffset`: X margin for print offset
- `YOffset`: Y margin for print offset

## Remarks

Units (inches or millimeters) for the margins for print offset are dependent on the specified [paper size](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html).

[IPrintManager::PrintOnCenter](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PrintOnCenter.html) must be set to false for the margins for print offset to be used. Use [IPrintManager::SetPrintOffset](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetPrintOffset.html) to set the margins for print offset.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1
