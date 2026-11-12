---
title: "GetConfigurations Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetConfigurations"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetConfigurations.html"
---

# GetConfigurations Method (IEdmFile5)

Gets a list of names of the configurations for the specified version of this file.

## Syntax

### Visual Basic

```vb
Function GetConfigurations( _
   Optional ByRef poVersionNoOrRevisionName As System.Object _
) As EdmStrLst5
```

### C#

```csharp
EdmStrLst5 GetConfigurations(
   ref System.object poVersionNoOrRevisionName
)
```

### C++/CLI

```cpp
EdmStrLst5^ GetConfigurations(
   System.Object^% poVersionNoOrRevisionName
)
```

### Parameters

- `poVersionNoOrRevisionName`: Version number or revision name; 0 or empty string to get configurations for the latest version of this file

### Return Value

[IEdmStrList5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html)

## Examples

[Get File Information (VB.NET)](Get_File_Info_Example_VBNET.htm)
[Get File Information (C#)](Get_File_Info_Example_CSharp.htm)

## Remarks

Some file types, such as files from AutoCAD and SOLIDWORKS, can contain several configurations or layouts. These configurations are visible as pages in the SOLIDWORKS PDM Professional file data cards.

C++ users not using smart pointer wrapper functions must release the returned interface, IEdmStrLst5.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_PERMISSION_DENIED: The logged-in user does not have read-access to the specified version or revision.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)
[IEdmFile14::GenerateDefaultConfigValues Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile14~GenerateDefaultConfigValues.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
