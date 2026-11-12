---
title: "GetLinkedDisplayStates Method (ISwDMConfiguration12)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration12"
member: "GetLinkedDisplayStates"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetLinkedDisplayStates.html"
---

# GetLinkedDisplayStates Method (ISwDMConfiguration12)

Gets the names and number of linked display states.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLinkedDisplayStates( _
   ByRef DisplayStateNameList As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration12
Dim DisplayStateNameList As System.Object
Dim value As System.Integer

value = instance.GetLinkedDisplayStates(DisplayStateNameList)
```

### C#

```csharp
System.int GetLinkedDisplayStates(
   out System.object DisplayStateNameList
)
```

### C++/CLI

```cpp
System.int GetLinkedDisplayStates(
   [Out] System.Object^ DisplayStateNameList
)
```

### Parameters

- `DisplayStateNameList`: Array of strings containing the linked display state names

### Return Value

Number of linked display states

## VBA Syntax

See [SwDMConfiguration12::GetLinkedDisplayStates](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration12~GetLinkedDisplayStates.html).

## Examples

[Get Linked Display States (VB.NET)](Get_Linked_Display_States_Example_VBNET.htm)
[Get Linked Display States (C#)](Get_Linked_Display_States_Example_CSharp.htm)

## See Also

[ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.html)
[ISwDMConfiguration12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12_members.html)
[ISwDMConfiguration12::GetComponentVisibleByDisplayStateName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetComponentVisibleByDisplayStateName.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
