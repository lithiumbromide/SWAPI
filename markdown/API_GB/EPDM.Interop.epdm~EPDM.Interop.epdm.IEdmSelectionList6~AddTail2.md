---
title: "AddTail2 Method (IEdmSelectionList6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSelectionList6"
member: "AddTail2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6~AddTail2.html"
---

# AddTail2 Method (IEdmSelectionList6)

Adds an item to the end of this list.

## Syntax

### Visual Basic

```vb
Sub AddTail2( _
   ByRef poObject As EdmSelectionObject _
)
```

### C#

```csharp
void AddTail2(
   ref EdmSelectionObject poObject
)
```

### C++/CLI

```cpp
void AddTail2(
   EdmSelectionObject% poObject
)
```

### Parameters

- `poObject`: [EdmSelectionObject](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject.html) structure; describes the object to add to the end of the list

## Examples

[Display Menu of Commands (VB.NET)](Display_Menu_of_Commands_Example_VBNET.htm)

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmSelectionList6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6.html)
[IEdmSelectionList6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
