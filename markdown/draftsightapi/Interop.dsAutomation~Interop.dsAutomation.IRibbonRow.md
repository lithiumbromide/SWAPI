---
title: "IRibbonRow Interface"
project: ""
interface: "IRibbonRow"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html"
---

# IRibbonRow Interface

Allows access to a ribbon row.

## Syntax

### Visual Basic

```vb
Public Interface IRibbonRow
```

### C#

```csharp
public interface IRibbonRow
```

### JScript

```
public interface IRibbonRow
```

### Managed Extensions for C++

```
public __gc __interface IRibbonRow
```

### C++/CLI

```cpp
public interface class IRibbonRow
```

## Examples

See the following ribbon-based add-in projects:

- `install_dir`**\APISDK\samples\C#\Simple\Ribbon**
- `install_dir`**\APISDK\samples\C++\Simple\Ribbon**
- `install_dir`**\APISDK\samples\COM\Simple\RibbonSample**
- `install_dir`**\APISDK\samples\JS\Simple\RibbonSample.html**

## Remarks

Only one ribbon row can be added to a [ribbon panel](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel.html).

Up to three ribbon rows can be added to a [ribbon row panel](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowPanel.html).

## Accessors

[IRibbonPanel::GetRibbonRow](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel~GetRibbonRow.html)

[IRibbonPanel::InsertRibbonRow](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel~InsertRibbonRow.html)

[IRibbonRowPanel::GetRibbonRows](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowPanel~GetRibbonRows.html)

[IRibbonRowPanel::InsertRibbonRow](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowPanel~InsertRibbonRow.html)

## Access Diagram

DSObjectModel.pdf#RibbonRow

[RibbonRow](DSObjectModel.pdf#RibbonRow)

## See Also

[IRibbonRow Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
