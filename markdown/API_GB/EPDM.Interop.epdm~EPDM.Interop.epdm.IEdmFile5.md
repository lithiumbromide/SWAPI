---
title: "IEdmFile5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: ""
kind: "interface"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html"
---

# IEdmFile5 Interface

Allows you to access a file in SOLIDWORKS PDM Professional.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmFile5
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmFile5 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmFile5 : public IEdmObject5
```

## Examples

[Traverse Folders and Files in Vault (C#)](Traverse_Folders_and_Files_in_Vault_Example_CSharp.htm)
[Traverse Folders and Files in Vault (VB.NET)](Traverse_Folders_and_Files_in_Vault_Example_VBNET.htm)
[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)
[Set Part Number Using Default Serial Numbers (C#)](Set_Part_Number_Using_Default_Serial_Numbers_Example_CSharp.htm)
[Set Part Number Using Default Serial Numbers (VB.NET)](Set_Part_Number_Using_Default_Serial_Numbers_Example_VBNET.htm)
[Get File Information (VB.NET)](Get_File_Info_Example_VBNET.htm)
[Get File Information (C#)](Get_File_Info_Example_CSharp.htm)

## Remarks

This interface:

- inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).
- is extended by [IEdmFile6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile6.html) which provides the ability to move, rename, and categorize files.

## Accessors

[IEdmFolder5::GetFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFile.html)

[IEdmFolder5::GetNextFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextFile.html)

[IEdmLabel5::GetNextFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel5~GetNextFile.html)

[IEdmReference5::File](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~File.html)

[IEdmState5::GetNextFle](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5~GetNextFile.html)

[IEdmVault5::GetFileFromPath](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetFileFromPath.html)

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

## See Also

[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
