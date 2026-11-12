---
title: "SetClosestValidPaperSize Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "SetClosestValidPaperSize"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetClosestValidPaperSize.html"
---

# SetClosestValidPaperSize Method (IPrintManager)

Sets the size of the paper to a valid size for the printer that is closest to the specified length and width.

## Syntax

### Visual Basic

```vb
Sub SetClosestValidPaperSize( _
   ByVal Length As System.Double, _
   ByVal Width As System.Double _
)
```

### C#

```csharp
void SetClosestValidPaperSize(
   System.double Length,
   System.double Width
)
```

### JScript

```
function SetClosestValidPaperSize(
   Length : System.double,
   Width : System.double
);
```

### Managed Extensions for C++

```
void SetClosestValidPaperSize(
   System.double Length,
   System.double Width
)
```

### C++/CLI

```cpp
void SetClosestValidPaperSize(
   System.double Length,
   System.double Width
)
```

### Parameters

- `Length`: Length of paper
- `Width`: Width of paper

## Remarks

Units (inches or millimeters) for Length and Width are dependent on the closest valid [paper size](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html).

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::AvailablePaperSizes Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~AvailablePaperSizes.html)
[IPrintManager::PaperSize Property](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html)
[IPrintManager::GetPaperSize Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPaperSize.html)

## Availability

DraftSight V1R1
