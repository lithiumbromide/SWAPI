---
title: "PaperSizeInLocale Method (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "PaperSizeInLocale"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSizeInLocale.html"
---

# PaperSizeInLocale Method (IPrintManager)

Gets the name of the localized paper size that corresponds to the specified non-localized paper size.

## Syntax

### Visual Basic

```vb
Function PaperSizeInLocale( _
   ByVal PaperSize As System.String _
) As System.String
```

### C#

```csharp
System.string PaperSizeInLocale(
   System.string PaperSize
)
```

### JScript

```
function PaperSizeInLocale(
   PaperSize : System.String
) : System.String;
```

### Managed Extensions for C++

```
System.string* PaperSizeInLocale(
   System.string* PaperSize
)
```

### C++/CLI

```cpp
System.String^ PaperSizeInLocale(
   System.String^ PaperSize
)
```

### Parameters

- `PaperSize`: Name of the non-localized paper size

### Return Value

Name of the localized paper size corresponding to PaperSize

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::AvailablePaperSizesInLocale Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~AvailablePaperSizesInLocale.html)
[IPrintManager::GetPaperSize Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPaperSize.html)
[IPrintManager::PaperSize Property](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PaperSize.html)
[IPrintManager::AvailablePaperSizes Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~AvailablePaperSizes.html)

## Availability

DraftSight V1R2.0
