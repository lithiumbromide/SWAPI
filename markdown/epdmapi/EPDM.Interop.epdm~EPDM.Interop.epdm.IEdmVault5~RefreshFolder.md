---
title: "RefreshFolder Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "RefreshFolder"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~RefreshFolder.html"
---

# RefreshFolder Method (IEdmVault5)

Refreshes the file listing in the specified folder.

## Syntax

### Visual Basic

```vb
Sub RefreshFolder( _
   ByVal bsFolderPath As System.String _
)
```

### C#

```csharp
void RefreshFolder(
   System.string bsFolderPath
)
```

### C++/CLI

```cpp
void RefreshFolder(
   System.String^ bsFolderPath
)
```

### Parameters

- `bsFolderPath`: File system path to the folder to refresh

## Examples

[Execute Template (C#)](Execute_Template_Example_CSharp.htm)
[Execute Template (VB.NET)](Execute_Template_Example_VBNET.htm)

## Remarks

If you use API methods to add, check out, or change the state of a file, the API does not automatically refresh its folder in File Explorer. That would be inefficient when processing a large number of files. If you check in a file using the API and browse to its folder using File Explorer, it appears to the user that the file is still checked out. This folder can be refreshed by one of the following techniques:

- Calling this method
- Pressing F5
- Navigating to a different folder and back again

There is no way to force a refresh on other machines.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
