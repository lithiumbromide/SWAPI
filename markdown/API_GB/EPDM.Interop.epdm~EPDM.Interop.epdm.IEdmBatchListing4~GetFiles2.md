---
title: "GetFiles2 Method (IEdmBatchListing4)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing4"
member: "GetFiles2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing4~GetFiles2.html"
---

# GetFiles2 Method (IEdmBatchListing4)

Gets all the files in this listing.

## Syntax

### Visual Basic

```vb
Sub GetFiles2( _
   ByRef ppoFiles As EdmListFile2() _
)
```

### C#

```csharp
void GetFiles2(
   out EdmListFile2[] ppoFiles
)
```

### C++/CLI

```cpp
void GetFiles2(
   [Out] array<EdmListFile2> ppoFiles
)
```

### Parameters

- `ppoFiles`: Array of [EdmListFile2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFile2.html) structures; one structure for each file in the listing

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

This method does not work with assemblies that contain weldment components or cutlist items.

Before calling this method, call [IEdmBatchListing2::CreateListEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2~CreateListEx.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing4 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing4.html)
[IEdmBatchListing4 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing4_members.html)

## Availability

SOLIDWORKS PDM Professional 2017
