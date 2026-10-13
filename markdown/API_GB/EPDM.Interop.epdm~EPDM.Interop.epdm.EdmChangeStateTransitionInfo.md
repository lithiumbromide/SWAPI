---
title: "EdmChangeStateTransitionInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmChangeStateTransitionInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateTransitionInfo.html"
---

# EdmChangeStateTransitionInfo Structure

Workflow state transition information.

## Syntax

### Visual Basic

```vb
Public Structure EdmChangeStateTransitionInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmChangeStateTransitionInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmChangeStateTransitionInfo : public System.ValueType
```

## Examples

struct EdmChangeStateTransitionInfo

{
short [mbIsRevoke](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateTransitionInfo~mbIsRevoke.html);
integer [mlCommitsNum](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateTransitionInfo~mlCommitsNum.html);
integer [mlRequiredNum](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateTransitionInfo~mlRequiredNum.html);
string [moDescription](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateTransitionInfo~moDescription.html);
string [moIcon](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateTransitionInfo~moIcon.html);
string [moName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateTransitionInfo~moName.html);
};

## Examples

[Batch Change States of Files (VB.NET)](Batch_Change_States_of_Files_Example_VBNET.htm)
[Batch Change States of Files (C#)](Batch_Change_States_of_Files_Example_CSharp.htm)

## See Also

[EdmChangeStateTransitionInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateTransitionInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2013
