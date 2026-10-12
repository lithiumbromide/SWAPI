---
title: "GetFirstLabelPosition Method (IEdmFolder5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFolder5"
member: "GetFirstLabelPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetFirstLabelPosition.html"
---

# GetFirstLabelPosition Method (IEdmFolder5)

Starts an enumeration of the labels in this folder.

## Syntax

### Visual Basic

```vb
Function GetFirstLabelPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstLabelPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstLabelPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first label in this folder

## Examples

[Create Labels on Folders (VB.NET)](Create_Label_Example_VBNET.htm)
[Create Labels on Folders (C#)](Create_Label_Example_CSharp.htm)

## Remarks

After calling this method, pass the returned first label position to [IEdmFolder5::GetNextLabel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5~GetNextLabel.html) to get the first label in the list. Then call IEdmFolder5::GetNextFile repeatedly to get the rest of the labels in the list.

C++ users not using smart-pointer wrapper functions must release the returned pointer, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmFolder5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5.html)
[IEdmFolder5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFolder5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
