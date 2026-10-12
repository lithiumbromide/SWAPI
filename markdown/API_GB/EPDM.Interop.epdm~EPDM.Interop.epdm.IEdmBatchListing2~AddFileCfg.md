---
title: "AddFileCfg Method (IEdmBatchListing2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing2"
member: "AddFileCfg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2~AddFileCfg.html"
---

# AddFileCfg Method (IEdmBatchListing2)

Adds a file to the batch of files for which to create a listing using variables from the specified configuration.

## Syntax

### Visual Basic

```vb
Sub AddFileCfg( _
   ByVal oIdOrPath As System.Object, _
   ByVal oFileDate As System.Date, _
   ByVal lParam As System.Integer, _
   Optional ByVal bsConfigName As System.String, _
   Optional ByVal lEdmListFileFlags As System.Integer _
)
```

### C#

```csharp
void AddFileCfg(
   System.object oIdOrPath,
   System.DateTime oFileDate,
   System.int lParam,
   System.string bsConfigName,
   System.int lEdmListFileFlags
)
```

### C++/CLI

```cpp
void AddFileCfg(
   System.Object^ oIdOrPath,
   System.DateTime oFileDate,
   System.int lParam,
   System.String^ bsConfigName,
   System.int lEdmListFileFlags
)
```

### Parameters

- `oIdOrPath`: Path of file to add
- `oFileDate`: Local file date
- `lParam`: Caller-defined argument
- `bsConfigName`: Name of the configuration from which to read the file variables; default is an empty string
- `lEdmListFileFlags`: Combination of [EdmListFileFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFileFlags.html) bits; default is 0

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

This method extends IEdmBatchListing::AddFile and IEdmBAtchListing::AddFolder by adding the ability to specify the configuration from which to read the file variables.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2.html)
[IEdmBatchListing2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing2_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
