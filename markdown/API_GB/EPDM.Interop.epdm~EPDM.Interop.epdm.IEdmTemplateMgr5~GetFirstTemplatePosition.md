---
title: "GetFirstTemplatePosition Method (IEdmTemplateMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTemplateMgr5"
member: "GetFirstTemplatePosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5~GetFirstTemplatePosition.html"
---

# GetFirstTemplatePosition Method (IEdmTemplateMgr5)

Starts an enumeration of the templates installed in the vault.

## Syntax

### Visual Basic

```vb
Function GetFirstTemplatePosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstTemplatePosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstTemplatePosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first installed template

## Examples

[Execute Template (C#)](Execute_Template_Example_CSharp.htm)
[Execute Template (VB.NET)](Execute_Template_Example_VBNET.htm)

## Remarks

After calling this method, pass the position of the first template to [IEdmTemplateMgr5::GetNextTemplate](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5~GetNextTemplate.html) to get the first template in this list. Then call IEdmTemplateMgr5::GetNextTemplate repeatedly to get the rest of the templates in this list.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTemplateMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5.html)
[IEdmTemplateMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
