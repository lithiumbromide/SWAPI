---
title: "GetFirstLabelPosition Method (IEdmEnumeratorVersion5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorVersion5"
member: "GetFirstLabelPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetFirstLabelPosition.html"
---

# GetFirstLabelPosition Method (IEdmEnumeratorVersion5)

Starts an enumeration of the labels set on this file.

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

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first label set on this file

## Remarks

After calling this method, pass the returned first label position to [IEdmEnumeratorVersion5::GetNextLabel](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5~GetNextLabel.html) to get the first label set on this file. Call IEdmEnumeratorVersion5::GetNextLabel repeatedly to get the rest of the labels set on this file.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmEnumeratorVersion5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5.html)
[IEdmEnumeratorVersion5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVersion5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
