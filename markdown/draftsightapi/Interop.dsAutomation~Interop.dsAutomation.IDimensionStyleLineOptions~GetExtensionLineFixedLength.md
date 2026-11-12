---
title: "GetExtensionLineFixedLength Method (IDimensionStyleLineOptions)"
project: ""
interface: "IDimensionStyleLineOptions"
member: "GetExtensionLineFixedLength"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~GetExtensionLineFixedLength.html"
---

# GetExtensionLineFixedLength Method (IDimensionStyleLineOptions)

Gets whether Dimension extension lines have a fixed length and gets the length.

## Syntax

### Visual Basic

```vb
Sub GetExtensionLineFixedLength( _
   ByRef IsEnabled As System.Boolean, _
   ByRef Value As System.Double _
)
```

### C#

```csharp
void GetExtensionLineFixedLength(
   out System.bool IsEnabled,
   out System.double Value
)
```

### JScript

```
function GetExtensionLineFixedLength(
   IsEnabled : System.boolean,
   Value : System.double
);
```

### Managed Extensions for C++

```
void GetExtensionLineFixedLength(
   [PARAMFLAG::Out] System.bool IsEnabled,
   [PARAMFLAG::Out] System.double Value
)
```

### C++/CLI

```cpp
void GetExtensionLineFixedLength(
   [Out] System.bool IsEnabled,
   [Out] System.double Value
)
```

### Parameters

- `IsEnabled`: True if a fixed length for Dimension extension lines is enabled, false if not
- `Value`: Fixed length

## See Also

[IDimensionStyleLineOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions.html)
[IDimensionStyleLineOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions_members.html)
[IDimensionStyleLineOptions::SetExtensionLineFixedLength Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~SetExtensionLineFixedLength.html)
[IDimensionStyleLineOptions::ExtensionLine1Style Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~ExtensionLine1Style.html)
[IDimensionStyleLineOptions::ExtensionLine2Style Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~ExtensionLine2Style.html)
[IDimensionStyleLineOptions::ExtensionLineColor Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~ExtensionLineColor.html)
[IDimensionStyleLineOptions::ExtensionLineDistancePastDimensionLines Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~ExtensionLineDistancePastDimensionLines.html)
[IDimensionStyleLineOptions::ExtensionLineLineWeight Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~ExtensionLineLineWeight.html)
[IDimensionStyleLineOptions::ExtensionLineOffset Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~ExtensionLineOffset.html)
[IDimensionStyleLineOptions::HideExtensionLine1 Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~HideExtensionLine1.html)
[IDimensionStyleLineOptions::HideExtensionLine2 Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~HideExtensionLine2.html)

## Availability

DraftSight V1R1.2
