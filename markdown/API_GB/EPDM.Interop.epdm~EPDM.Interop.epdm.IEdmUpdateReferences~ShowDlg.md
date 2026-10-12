---
title: "ShowDlg Method (IEdmUpdateReferences)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUpdateReferences"
member: "ShowDlg"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUpdateReferences~ShowDlg.html"
---

# ShowDlg Method (IEdmUpdateReferences)

Displays the command dialog box for all of the files added to the batch with [IEdmUpdateReferences::AddFile](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUpdateReferences~AddFile.html).

## Syntax

### Visual Basic

```vb
Sub ShowDlg( _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal lFlags As System.Integer, _
   Optional ByVal lFolderID As System.Integer _
)
```

### C#

```csharp
void ShowDlg(
   System.int lParentWnd,
   System.int lFlags,
   System.int lFolderID
)
```

### C++/CLI

```cpp
void ShowDlg(
   System.int lParentWnd,
   System.int lFlags,
   System.int lFolderID
)
```

### Parameters

- `lParentWnd`: Parent window handle
- `lFlags`: Must be 0; reserved for future use
- `lFolderID`: ID of the active folder; 0 to ignore

## Examples

[Update References (C#)](Update_References_Example_CSharp.htm)
[Update References (VB.NET)](Update_References_Example_VBNET.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUpdateReferences Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUpdateReferences.html)
[IEdmUpdateReferences Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUpdateReferences_members.html)

## Availability

SOLIDWORKS PDM Professional 2011
