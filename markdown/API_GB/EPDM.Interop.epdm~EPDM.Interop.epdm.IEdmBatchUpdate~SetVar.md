---
title: "SetVar Method (IEdmBatchUpdate)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUpdate"
member: "SetVar"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate~SetVar.html"
---

# SetVar Method (IEdmBatchUpdate)

Obsolete. Superseded by [IEdmBatchUpdate2::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate2~SetVar.html).

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

- `lFileID`: ID of file to which to write the variable
- `lVariableID`: ID of variable to update; retrieve using [IEdmVariableMgr5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5.html)
- `poValue`: New value of the variable
- `bsConfiguration`: Name of the configuration to which to write the variable; empty string for files without configurations
- `lEdmBatchFlags`: Combination of [EdmBatchFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBatchFlags.html) bits

## Remarks

See the [IEdmBatchUpdate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate.html) remarks for information about using this method.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchUpdate Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate.html)
[IEdmBatchUpdate Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUpdate_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.2
