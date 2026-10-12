---
title: "EdmWorkflowInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmWorkflowInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmWorkflowInfo.html"
---

# EdmWorkflowInfo Structure

Holds information about a file's workflow state.

## Syntax

### Visual Basic

```vb
Public Structure EdmWorkflowInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmWorkflowInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmWorkflowInfo : public System.ValueType
```

## Examples

struct EdmWorkflowInfo
string [mbsStateName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmWorkflowInfo~mbsStateName.html);
string [mbsStateIcon](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmWorkflowInfo~mbsStateIcon.html);
string [mbsWorkflowName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmWorkflowInfo~mbsWorkflowName.html);
};

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

This structure is referenced in the [EdmListFile2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2.html) structure.

## See Also

[EdmWorkflowInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmWorkflowInfo_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
