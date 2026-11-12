---
title: "SetVar Method (IEdmBatchUpdate2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUpdate2"
member: "SetVar"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~SetVar.html"
---

# SetVar Method (IEdmBatchUpdate2)

Adds a file card variable to the batch of variables to update.

## Syntax

### Visual Basic

```vb
Sub SetVar( _
   ByVal lFileID As System.Integer, _
   ByVal lVariableID As System.Integer, _
   ByRef poValue As System.Object, _
   ByVal bsConfiguration As System.String, _
   Optional ByVal lEdmBatchFlags As System.Integer _
)
```

### C#

```csharp
void SetVar(
   System.int lFileID,
   System.int lVariableID,
   ref System.object poValue,
   System.string bsConfiguration,
   System.int lEdmBatchFlags
)
```

### C++/CLI

```cpp
void SetVar(
   System.int lFileID,
   System.int lVariableID,
   System.Object^% poValue,
   System.String^ bsConfiguration,
   System.int lEdmBatchFlags
)
```

### Parameters

- `lFileID`: ID of file to which to write the file card variable
- `lVariableID`: ID of file card variable to update
- `poValue`: New value of the file card variable
- `bsConfiguration`: Name of configuration to which to write the file card variable; ignored if lEdmBatchFlags contains EdmBatchFlags.EdmBatch_AllConfigs
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
