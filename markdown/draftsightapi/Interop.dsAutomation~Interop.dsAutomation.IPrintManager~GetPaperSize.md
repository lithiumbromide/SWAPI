---
title: "GetPaperSize Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "GetPaperSize"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPaperSize.html"
---

# GetPaperSize Method (IPrintManager)

Gets the size of the paper.

## Syntax

### Visual Basic

```vb
Sub GetPaperSize( _
   ByRef Length As System.Double, _
   ByRef Width As System.Double _
)
```

### C#

```csharp
void GetPaperSize(
   out System.double Length,
   out System.double Width
)
```

### JScript

```
function GetPaperSize(
   Length : System.double,
   Width : System.double
);
```

### Managed Extensions for C++

```
void GetPaperSize(
   [PARAMFLAG::Out] System.double Length,
   [PARAMFLAG::Out] System.double Width
)
```

### C++/CLI

```cpp
void GetPaperSize(
   [Out] System.double Length,
   [Out] System.double Width
)
```

### Parameters

- `Length`: Length of paper
- `Width`: Width of paper

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## Remarks

Units (inches or millimeters) for Length and Width are dependent on the [paper size](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html).

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::AvailablePaperSizes Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~AvailablePaperSizes.html)
[IPrintManager::PaperSize Property](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html)
[IPrintManager::SetClosestValidPaperSize Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetClosestValidPaperSize.html)

## Availability

DraftSight V1R1
