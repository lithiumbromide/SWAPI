---
title: "SetFolderVar Method (IEdmBatchUpdate2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUpdate2"
member: "SetFolderVar"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~SetFolderVar.html"
---

# SetFolderVar Method (IEdmBatchUpdate2)

Adds a folder card variable to the batch of variables to update.

## Syntax

### Visual Basic

```vb
Sub SetFolderVar( _
   ByVal lFolderID As System.Integer, _
   ByVal lVariableID As System.Integer, _
   ByRef poValue As System.Object, _
   Optional ByVal lEdmBatchFlags As System.Integer _
)
```

### C#

```csharp
void SetFolderVar(
   System.int lFolderID,
   System.int lVariableID,
   ref System.object poValue,
   System.int lEdmBatchFlags
)
```

### C++/CLI

```cpp
void SetFolderVar(
   System.int lFolderID,
   System.int lVariableID,
   System.Object^% poValue,
   System.int lEdmBatchFlags
)
```

### Parameters

- `lFolderID`: ID of folder to which to write the card variable
- `lVariableID`: ID of folder card variable to update
- `poValue`: New value of the folder card variable
- `lEdmBatchFlags`: Combination of [EdmBatchFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchFlags.html) bits

## Examples

See the [IEdmBatchUpdate2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchUpdate2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2.html)
[IEdmBatchUpdate2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.3
