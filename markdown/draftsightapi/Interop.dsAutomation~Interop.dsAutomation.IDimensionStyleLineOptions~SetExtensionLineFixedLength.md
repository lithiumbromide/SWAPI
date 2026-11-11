---
title: "SetExtensionLineFixedLength Method (IDimensionStyleLineOptions)"
project: ""
interface: "IDimensionStyleLineOptions"
member: "SetExtensionLineFixedLength"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~SetExtensionLineFixedLength.html"
---

# SetExtensionLineFixedLength Method (IDimensionStyleLineOptions)

Sets whether Dimension extension lines have a fixed length and sets the length.

## Syntax

### Visual Basic

```vb
Sub SetExtensionLineFixedLength( _
   ByVal IsEnabled As System.Boolean, _
   ByVal Value As System.Double _
)
```

### C#

```csharp
void SetExtensionLineFixedLength(
   System.bool IsEnabled,
   System.double Value
)
```

### JScript

```
function SetExtensionLineFixedLength(
   IsEnabled : System.boolean,
   Value : System.double
);
```

### Managed Extensions for C++

```
void SetExtensionLineFixedLength(
   System.bool IsEnabled,
   System.double Value
)
```

### C++/CLI

```cpp
void SetExtensionLineFixedLength(
   System.bool IsEnabled,
   System.double Value
)
```

### Parameters

- `IsEnabled`: True to enable a fixed length for extension lines, false to not
- `Value`: Fixed length, if IsEnabled is true

## See Also

[IDimensionStyleLineOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions.html)
[IDimensionStyleLineOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions_members.html)
[IDimensionStyleLineOptions::GetExtensionLineFixedLength Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions~GetExtensionLineFixedLength.html)
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
