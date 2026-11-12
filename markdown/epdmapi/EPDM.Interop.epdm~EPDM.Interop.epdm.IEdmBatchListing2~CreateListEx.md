---
title: "CreateListEx Method (IEdmBatchListing2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing2"
member: "CreateListEx"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2~CreateListEx.html"
---

# CreateListEx Method (IEdmBatchListing2)

Creates a listing of the properties of the files and folders that were added to the batch using [IEdmBatchListing::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~AddFile.html), [IEdmBatchListing::AddFolder](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~AddFolder.html), and [IEdmBatchListing2::AddFileCfg](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2~AddFileCfg.html).

## Syntax

### Visual Basic

```vb
Sub CreateListEx( _
   ByVal bsColumnSetName As System.String, _
   ByVal lEdmCreateListExFlags As System.Integer, _
   ByRef ppoColumns() As EdmListCol, _
   Optional ByVal poAux As System.Object _
)
```

### C#

```csharp
void CreateListEx(
   System.string bsColumnSetName,
   System.int lEdmCreateListExFlags,
   out EdmListCol[] ppoColumns,
   System.object poAux
)
```

### C++/CLI

```cpp
void CreateListEx(
   System.String^ bsColumnSetName,
   System.int lEdmCreateListExFlags,
   [Out] array<EdmListCol>^ ppoColumns,
   System.Object^ poAux
)
```

### Parameters

- `bsColumnSetName`: Empty string, one of the set names returned by [IEdmBatchListing::GetColumnSetNames](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~GetColumnSetNames.html), or a list of variable names separated by newline characters and starting with a newline character (e.g., "\nAuthor\nProject\nDate")
- `lEdmCreateListExFlags`: Combination of [EdmCreateListExFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCreateListExFlags.html) bits
- `ppoColumns`: Array of [EdmListCol](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListCol.html) structures; one structure for each column in the column set
- `poAux`: Reserved for future use

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

This method extends [IEdmBatchListing::CreateList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~CreateList.html) by adding the ability to configure from where the file variables are read.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2.html)
[IEdmBatchListing2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
