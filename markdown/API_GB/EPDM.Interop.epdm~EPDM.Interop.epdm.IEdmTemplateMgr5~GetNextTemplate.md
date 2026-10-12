---
title: "GetNextTemplate Method (IEdmTemplateMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTemplateMgr5"
member: "GetNextTemplate"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5~GetNextTemplate.html"
---

# GetNextTemplate Method (IEdmTemplateMgr5)

Gets the next template in this list.

## Syntax

### Visual Basic

```vb
Function GetNextTemplate( _
   ByVal poPos As IEdmPos5 _
) As IEdmTemplate5
```

### C#

```csharp
IEdmTemplate5 GetNextTemplate(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmTemplate5^ GetNextTemplate(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next template

### Return Value

[IEdmTemplate5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate5.html)

## Examples

[Execute Template (C#)](Execute_Template_Example_CSharp.htm)
[Execute Template (VB.NET)](Execute_Template_Example_VBNET.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first template, IEdmPos5. Call [IEdmTemplateMgr5::GetFirstTemplatePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5~GetFirstTemplatePosition.html) to obtain poPos.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the templates.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmTemplate5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTemplateMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5.html)
[IEdmTemplateMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplateMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
