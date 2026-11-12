---
title: "EdmBatchError2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBatchError2"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError2.html"
---

# EdmBatchError2 Structure

Contains error information.

## Syntax

### Visual Basic

```vb
Public Structure EdmBatchError2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBatchError2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBatchError2 : public System.ValueType
```

## Examples

struct EdmBatchError2{
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError2~mlFileID.html);
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError2~mlFolderID.html);
integer [mlVariableID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError2~mlVariableID.html);
integer [mlErrorCode](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError2~mlErrorCode.html);
};

## Examples

[Batch Update Card Variables (VB.NET)](Batch_Update_Variables_Example_VBNET.htm)
[Batch Update Card Variables (C#)](Batch_Update_Variables_Example_CSharp.htm)

## Remarks

Extends the [EdmBatchError structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError.html) and is returned by [IEdmBatchUpdate2::CommitUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~CommitUpdate.html).

## See Also

[EdmBatchError2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
