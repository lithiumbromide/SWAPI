---
title: "Run Method (IEdmTemplate5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTemplate5"
member: "Run"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5~Run.html"
---

# Run Method (IEdmTemplate5)

Executes this template in the specified folder.

## Syntax

### Visual Basic

```vb
Function Run( _
   ByVal hParentWnd As System.Integer, _
   ByVal lCurrentFolderID As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int Run(
   System.int hParentWnd,
   System.int lCurrentFolderID
)
```

### C++/CLI

```cpp
System.int Run(
   System.int hParentWnd,
   System.int lCurrentFolderID
)
```

### Parameters

- `hParentWnd`: Parent window handle
- `lCurrentFolderID`: ID of folder in which to run this template

### Return Value

User-interface refresh flags as defined in [EdmRefreshFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefreshFlag.html)

## Examples

[Execute Template (C#)](Execute_Template_Example_CSharp.htm)
[Execute Template (VB.NET)](Execute_Template_Example_VBNET.htm)

## Remarks

This method is extended by [IEdmTemplate53::RunEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate53~RunEx.html) which returns information about all of the files and folders created by the template.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTemplate5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5.html)
[IEdmTemplate5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
