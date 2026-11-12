---
title: "GetFileList Method (IEdmBatchUnlock)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUnlock"
member: "GetFileList"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock~GetFileList.html"
---

# GetFileList Method (IEdmBatchUnlock)

Gets the list of files to be unlocked.

## Syntax

### Visual Basic

```vb
Function GetFileList( _
   ByVal lEdmUnlockFileListFlags As System.Integer _
) As EdmSelectionList5
```

### C#

```csharp
EdmSelectionList5 GetFileList(
   System.int lEdmUnlockFileListFlags
)
```

### C++/CLI

```cpp
EdmSelectionList5^ GetFileList(
   System.int lEdmUnlockFileListFlags
)
```

### Parameters

- `lEdmUnlockFileListFlags`: Combination of [EdmUnlockFileListFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockFileListFlag.html) bits

### Return Value

[IEdmSelectionList5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html)

## Examples

See the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) examples.

## Remarks

See the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) remarks for information about using this method.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchUnlock Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html)
[IEdmBatchUnlock Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
