---
title: "GetFileList Method (IEdmBatchGet)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchGet"
member: "GetFileList"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet~GetFileList.html"
---

# GetFileList Method (IEdmBatchGet)

Gets a list of the files in this batch.

## Syntax

### Visual Basic

```vb
Function GetFileList( _
   ByVal lEdmGetFileListFlags As System.Integer _
) As EdmSelectionList5
```

### C#

```csharp
EdmSelectionList5 GetFileList(
   System.int lEdmGetFileListFlags
)
```

### C++/CLI

```cpp
EdmSelectionList5^ GetFileList(
   System.int lEdmGetFileListFlags
)
```

### Parameters

- `lEdmGetFileListFlags`: Combination of [EdmGetFileListFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGetFileListFlag.html) bits

### Return Value

[IEdmSelectionList5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html); list of files in this batch

## Examples

See the [IEdmBatchGet](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchGet Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet.html)
[IEdmBatchGet Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchGet_members.html)

## Availability

Version 6.3 of SOLIDWORKS PDM Professional
