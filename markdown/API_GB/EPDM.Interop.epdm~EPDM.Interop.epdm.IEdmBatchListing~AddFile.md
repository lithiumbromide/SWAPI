---
title: "AddFile Method (IEdmBatchListing)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing"
member: "AddFile"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~AddFile.html"
---

# AddFile Method (IEdmBatchListing)

Adds a file to the batch of files for which to create a listing.

## Syntax

### Visual Basic

```vb
Sub AddFile( _
   ByVal oIdOrPath As System.Object, _
   ByVal oFileDate As System.Date, _
   ByVal lParam As System.Integer, _
   Optional ByVal lEdmListFileFlags As System.Integer _
)
```

### C#

```csharp
void AddFile(
   System.object oIdOrPath,
   System.DateTime oFileDate,
   System.int lParam,
   System.int lEdmListFileFlags
)
```

### C++/CLI

```cpp
void AddFile(
   System.Object^ oIdOrPath,
   System.DateTime oFileDate,
   System.int lParam,
   System.int lEdmListFileFlags
)
```

### Parameters

- `oIdOrPath`: ID or path of the file to add
- `oFileDate`: Local file date
- `lParam`: Caller-defined argument
- `lEdmListFileFlags`: Reserved; must be 0

## Remarks

After calling this method for each file whose properties you want to list, call [IEdmBatchListing::CreateList](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing~CreateList.html) to create a listing for all the files.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing.html)
[IEdmBatchListing Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing_members.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
