---
title: "GetHeadPosition Method (IEdmSelectionList5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSelectionList5"
member: "GetHeadPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5~GetHeadPosition.html"
---

# GetHeadPosition Method (IEdmSelectionList5)

Starts an enumeration of the items in this list.

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

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of first element in this list

## Examples

See the [IEdmSelectionList5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html) examples.

## Remarks

After calling this method, pass the position of the first item to [IEdmSelectionList5::GetNext](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5~GetNext.html) to get the first item in this list. Then call IEdmSelectionList5::GetNext repeatedly to get the rest of the items in this list.

C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmSelectionList5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html)
[IEdmSelectionList5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
