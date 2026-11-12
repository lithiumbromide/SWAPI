---
title: "GetShowInBOM Method (IEdmEnumeratorCustomReference7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference7"
member: "GetShowInBOM"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7~GetShowInBOM.html"
---

# GetShowInBOM Method (IEdmEnumeratorCustomReference7)

Gets whether the specified file's user-defined file references are shown in a BOM.

## Syntax

### Visual Basic

```vb
Function GetShowInBOM( _
   ByVal lFileID As System.Integer, _
   ByVal lFolderID As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool GetShowInBOM(
   System.int lFileID,
   System.int lFolderID
)
```

### C++/CLI

```cpp
System.bool GetShowInBOM(
   System.int lFileID,
   System.int lFolderID
)
```

### Parameters

- `lFileID`: ID of referenced file
- `lFolderID`: ID of parent folder of referenced file

### Return Value

True if the specified file's user-defined file references are shown in a BOM, false if not

## Examples

[Access Custom File References (C#)](Access_Custom_File_References_Example_CSharp.htm)
[Access Custom File References (VB.NET)](Access_Custom_File_References_Example_VBNET.htm)

## See Also

[IEdmEnumeratorCustomReference7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7.html)
[IEdmEnumeratorCustomReference7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7_members.html)
[IEdmEnumeratorCustomReference7::GetShowInBOM Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference7~GetShowInBOM.html)

## Availability

SOLIDWORKS PDM Professional 2017
