---
title: "EdmTaskSel Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmTaskSel"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel.html"
---

# EdmTaskSel Structure

Passed as argument to [IEdmTaskProperties::SetSel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetSel.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmTaskSel
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmTaskSel : System.ValueType
```

### C++/CLI

```cpp
public value class EdmTaskSel : public System.ValueType
```

## Examples

struct EdmTaskSel{
[EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel~meType.html);
integer [mlID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel~mlID.html);
integer [mlParentID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel~mlParentID.html);
integer [mlVersion](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel~mlVersion.html);
string [mbsConfiguration](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel~mbsConfiguration.html);
};

## Remarks

The struct contains a selected item that should be processed by the task.

## See Also

[EdmTaskSel Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSel_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Programming Tasks](Tasks.htm)

## Availability

SOLIDWORKS PDM Professional 2010
