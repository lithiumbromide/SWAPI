---
title: "EdmRawReference Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRawReference"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference.html"
---

# EdmRawReference Structure

Contains information about a file reference.

## Syntax

### Visual Basic

```vb
Public Structure EdmRawReference
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmRawReference : System.ValueType
```

### C++/CLI

```cpp
public value class EdmRawReference : public System.ValueType
```

## Examples

struct EdmRawReference

{
string [mbsRefID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference~mbsRefID.html);
string [mbsIncludePath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference~mbsIncludePath.html);
string [mbsRefName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference~mbsRefName.html);
integer [mlFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference~mlFlags.html);
integer [mlCount](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference~mlCount.html);
};

## Examples

[Update File Raw References (C#)](Update_File_Raw_References_Example_CSharp.htm)
[Update File Raw References (VB.NET)](Update_File_Raw_References_Example_VBNET.htm)

## Remarks

This structure is used by the [IEdmRawReferenceMgr](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRawReferenceMgr.html) interface.

## See Also

[EdmRawReference Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRawReference_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
