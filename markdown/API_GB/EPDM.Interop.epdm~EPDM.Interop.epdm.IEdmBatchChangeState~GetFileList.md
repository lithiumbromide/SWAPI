---
title: "GetFileList Method (IEdmBatchChangeState)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState"
member: "GetFileList"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState~GetFileList.html"
---

# GetFileList Method (IEdmBatchChangeState)

Gets the list of files affected by the state change or transition revocation.

## Syntax

### Visual Basic

```vb
Function GetFileList( _
   ByVal lEdmChangeStateFileListFlags As System.Integer _
) As EdmSelectionList5
```

### C#

```csharp
EdmSelectionList5 GetFileList(
   System.int lEdmChangeStateFileListFlags
)
```

### C++/CLI

```cpp
EdmSelectionList5^ GetFileList(
   System.int lEdmChangeStateFileListFlags
)
```

### Parameters

- `lEdmChangeStateFileListFlags`: Combination of [EdmChangeStateFileListFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmChangeStateFileListFlag.html) bits

### Return Value

[IEdmSelectionList5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html); list of affected objects

## Examples

See the [IEdmBatchChangeState4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState4.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchChangeState Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState.html)
[IEdmBatchChangeState Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
