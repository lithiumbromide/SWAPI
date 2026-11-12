---
title: "GetFileFromPath Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "GetFileFromPath"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFileFromPath.html"
---

# GetFileFromPath Method (IEdmVault5)

Gets an interface to the file with the specified file system path.

## Syntax

### Visual Basic

```vb
Function GetFileFromPath( _
   ByVal bsFilePath As System.String, _
   Optional ByRef ppoRetParentFolder As IEdmFolder5 _
) As IEdmFile5
```

### C#

```csharp
IEdmFile5 GetFileFromPath(
   System.string bsFilePath,
   out IEdmFolder5 ppoRetParentFolder
)
```

### C++/CLI

```cpp
IEdmFile5^ GetFileFromPath(
   System.String^ bsFilePath,
   [Out] IEdmFolder5^ ppoRetParentFolder
)
```

### Parameters

- `bsFilePath`: File system path to the file for which to get an interface
- `ppoRetParentFolder`: [IEdmFolder5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html); 0 to not return an interface

### Return Value

[IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html); Null if file specified in bsFilePath does not exist

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)
[Get File Version Information (C#)](Get_File_Version_Information_Example_CSharp.htm)
[Get File Version Information (VB.NET)](Get_File_Version_Information_Example_VBNET.htm)
[Set Part Number Using Default Serial Numbers (C#)](Set_Part_Number_Using_Default_Serial_Numbers_Example_CSharp.htm)
[Set Part Number Using Default Serial Numbers (VB.NET)](Set_Part_Number_Using_Default_Serial_Numbers_Example_VBNET.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The file was not found.
- E_EDM_NOT_LOGGED_IN: You must call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) before calling this method.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)
[IEdmVault5::GetFolderFromPath Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFolderFromPath.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
