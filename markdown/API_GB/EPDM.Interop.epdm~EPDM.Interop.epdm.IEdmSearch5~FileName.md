---
title: "FileName Property (IEdmSearch5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch5"
member: "FileName"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~FileName.html"
---

# FileName Property (IEdmSearch5)

Gets or sets the name of the file or folder for which to search.

## Syntax

### Visual Basic

```vb
Property FileName As System.String
```

### C#

```csharp
System.string FileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of file or folder for which to search (see **Remarks**)

## Examples

See the [IEdmSearch9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html) examples.

## Examples

[Batch Update Card Variables (VB.NET)](Batch_Update_Variables_Example_VBNET.htm)
[Batch Update Card Variables (C#)](Batch_Update_Variables_Example_CSharp.htm)

## Remarks

If the search object was obtained using:

- [IEdmVault21::CreateSearch2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.html) (IEdmSearch9), then the name may require extended search syntax. (See [Search Syntax](SearchSyntax-epdmapi.html).)

- [IEdmVault5::CreateSearch](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~CreateSearch.html), then the name may contain a % wildcard character. For example, **%.txt** searches for all text files.

% indicates any sequence of characters of any length. You can also use underscore (_) as a wildcard for exactly one arbitrary character.

To search for strings containing the actual characters '%' and '_', enclose them in brackets [...]:

my[_]text[%]file.txt

You can also enclose the entire string in brackets, if no wildcards exist in it:

[my_text%file.txt]

## See Also

[IEdmSearch5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html)
[IEdmSearch5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
