---
title: "EdmBatchError Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBatchError"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError.html"
---

# EdmBatchError Structure

Contains error information.

## Syntax

### Visual Basic

```vb
Public Structure EdmBatchError
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBatchError : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBatchError : public System.ValueType
```

## Examples

struct EdmBatchError{
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError~mlFileID.html);
integer [mlVariableID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError~mlVariableID.html);
integer [mlErrorCode](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError~mlErrorCode.html);
};

## Remarks

Returned by [IEdmBatchUpdate::Commit](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate~Commit.html)

## See Also

[EdmBatchError Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchError_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.2 of SOLIDWORKS PDM Professional
