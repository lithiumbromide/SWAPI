---
title: "DisplayInTab Method (IRibbonPanel)"
project: ""
interface: "IRibbonPanel"
member: "DisplayInTab"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel~DisplayInTab.html"
---

# DisplayInTab Method (IRibbonPanel)

Specifies where to display this ribbon panel.

## Syntax

### Visual Basic

```vb
Sub DisplayInTab( _
   ByVal TabName As System.String, _
   ByVal Position As System.Integer _
)
```

### C#

```csharp
void DisplayInTab(
   System.string TabName,
   System.int Position
)
```

### JScript

```
function DisplayInTab(
   TabName : System.String,
   Position : System.int
);
```

### Managed Extensions for C++

```
void DisplayInTab(
   System.string* TabName,
   System.int Position
)
```

### C++/CLI

```cpp
void DisplayInTab(
   System.String^ TabName,
   System.int Position
)
```

### Parameters

- `TabName`: Name of tab
- `Position`: Position of this ribbon panel (1-based index)

## See Also

[IRibbonPanel Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel.html)
[IRibbonPanel Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel_members.html)

## Availability

DraftSight 2017 SP0
