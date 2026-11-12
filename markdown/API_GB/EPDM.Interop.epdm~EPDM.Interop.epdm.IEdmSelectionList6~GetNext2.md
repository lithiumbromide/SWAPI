---
title: "GetNext2 Method (IEdmSelectionList6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSelectionList6"
member: "GetNext2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6~GetNext2.html"
---

# GetNext2 Method (IEdmSelectionList6)

Gets the next item in this list.

## Syntax

### Visual Basic

```vb
Sub GetNext2( _
   ByVal poPos As IEdmPos5, _
   ByRef poSel As EdmSelectionObject _
)
```

### C#

```csharp
void GetNext2(
   IEdmPos5 poPos,
   out EdmSelectionObject poSel
)
```

### C++/CLI

```cpp
void GetNext2(
   IEdmPos5^ poPos,
   [Out] EdmSelectionObject poSel
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the item to get (see **Remarks**)
- `poSel`: [EdmSelectionObject](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelectionObject.html) structure

## Examples

See the [IEdmSelectionList5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5.html) examples.

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first item, IEdmPos5. Call [IEdmSelectionList5::GetHeadPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5~GetHeadPosition.html) to obtain IEdmPos5.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the items.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ programmers must free the object returned in poSel.

**Note**: Objects added with the now obsolete [IEdmSelectionList5::AddTail](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList5~AddTail.html) are not completely defined. If you added an object using IEdmSelectionList5::AddTail, the EdmSelectionObject structure returned by this method contains the following:

- The meType member is always [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html).EdmObject_File.
- The mbsPath member contains only the file name provided as argument to IEdmSelectionList5::AddTail, not the entire path.
- The members mlGetVersion, mlLocalVersion, and mlLatestVersion are all -1.

To add completely defined objects to this list, call [IEdmSelectionList6.AddTail2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6~AddTail2.html).

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: You have gone past the end of the list.

## See Also

[IEdmSelectionList6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6.html)
[IEdmSelectionList6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSelectionList6_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
