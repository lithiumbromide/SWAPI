---
title: "GetDictionary Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "GetDictionary"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetDictionary.html"
---

# GetDictionary Method (IEdmVault5)

Gets or creates the specified dictionary.

## Syntax

### Visual Basic

```vb
Function GetDictionary( _
   ByVal bsName As System.String, _
   ByVal bCreateIfNew As System.Boolean _
) As IEdmDictionary5
```

### C#

```csharp
IEdmDictionary5 GetDictionary(
   System.string bsName,
   System.bool bCreateIfNew
)
```

### C++/CLI

```cpp
IEdmDictionary5^ GetDictionary(
   System.String^ bsName,
   System.bool bCreateIfNew
)
```

### Parameters

- `bsName`: Name of dictionary to get or create
- `bCreateIfNew`: True to create the dictionary if it does not exist, false to not

### Return Value

[IEdmDictionary5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmDictionary5.html); Null if bCreateIfNew is false and the dictionary with bsName does not exist

## Examples

[Change Card Variables Add-in (VB.NET)](Change_Card_Variables_Addin_Example_VBNET.htm)
[Change Card Variables Add-in (C#)](Change_Card_Variables_Addin_Example_CSharp.htm)
[Create and Delete Dictionaries (C#)](Create_and_Delete_Dictionaries_Example_CSharp.htm)
[Create and Delete Dictionaries (VB.NET)](Create_and_Delete_Dictionaries_Example_VBNET.htm)

## Remarks

A dictionary in SOLIDWORKS PDM Professional is a way of storing arbitrary data in the SOLIDWORKS PDM Professional database. The data is organized into key-value pairs. The values are always strings. The keys can be either integers or strings.

**NOTE:** If you intend to store file- or folder-specific data and want the data to be deleted or copied whenever the file or folder is deleted or copied, consider using card variables instead of dictionaries. Card variables stored using [IEdmEnumeratorVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5.html) do not require corresponding controls in the file or folder data card.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The dictionary with the specified name does not exist, and bCreateIfNew is false.
- E_EDM_NOT_LOGGED_IN: You must call [IEdmVault5::Login](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~Login.html) or [IEdmVault5::LoginAuto](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~LoginAuto.html) before calling this method.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
