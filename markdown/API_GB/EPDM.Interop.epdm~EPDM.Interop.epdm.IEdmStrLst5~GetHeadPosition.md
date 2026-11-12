---
title: "GetHeadPosition Method (IEdmStrLst5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmStrLst5"
member: "GetHeadPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5~GetHeadPosition.html"
---

# GetHeadPosition Method (IEdmStrLst5)

Starts an enumeration of the strings in this list.

## Syntax

### Visual Basic

```vb
Function GetHeadPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetHeadPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetHeadPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position in the list of the first string (see **Remarks**)

## Examples

See the [IEdmStrLst5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html) examples.

## Remarks

After calling this method, pass the returned position of the first string to [IEdmStrLst5::GetNext](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5~GetNext.html) to get the first string in this list. Then call IEdmStrLst5::GetNext repeatedly to get the rest of the strings in this list.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmStrLst5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html)
[IEdmStrLst5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
