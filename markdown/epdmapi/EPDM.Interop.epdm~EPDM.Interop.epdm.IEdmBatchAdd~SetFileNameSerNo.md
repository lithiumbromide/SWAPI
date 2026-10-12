---
title: "SetFileNameSerNo Method (IEdmBatchAdd)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchAdd"
member: "SetFileNameSerNo"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~SetFileNameSerNo.html"
---

# SetFileNameSerNo Method (IEdmBatchAdd)

For internal use only; do not use.

## Syntax

### Visual Basic

```vb
Sub SetFileNameSerNo( _
   ByVal oSerialNumberName As System.Object, _
   Optional ByVal lFlags As System.Integer _
)
```

### C#

```csharp
void SetFileNameSerNo(
   System.object oSerialNumberName,
   System.int lFlags
)
```

### C++/CLI

```cpp
void SetFileNameSerNo(
   System.Object^ oSerialNumberName,
   System.int lFlags
)
```

### Parameters

- `oSerialNumberName`: File name or the ID of the serial number generator
- `lFlags`: Must be 0

## Remarks

This method specifies that when a file is batch added to the vault, its data card is created with a name that is either the added file's serial number or its name.

By default when new files are added to the vault, file data cards are created with serial number names. Use this method to specify that when batch adding a file to the vault ([IEdmBatchAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html)::Add* methods), the file's data card name is the file name instead of the file's serial number.

If you don't call this method before calling the IEdmBatchAdd::Add* methods, they will create one serial number for the file and another serial number for the file data card. To synchronize the serial numbers:

1. Generate the added file's serial number using [IEdmSerNoGen7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen7.html).
2. Call this method, specifying oSerialNumberName with the added file's serial number generator ID.
3. Repeat steps 1 and 2 for each new file.
4. Call one of the IEdmBatchAdd::Add* methods to add the new files to the batch.
5. Call [IEdmBatchAdd::CommitAdd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd~CommitAdd.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchAdd Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd.html)
[IEdmBatchAdd Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchAdd_members.html)
[IEdmFolder12::SetFileNameSerNo Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder12~SetFileNameSerNo.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
