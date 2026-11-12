---
title: "GetComponentVisibleByDisplayStateName Method (ISwDMConfiguration12)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration12"
member: "GetComponentVisibleByDisplayStateName"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetComponentVisibleByDisplayStateName.html"
---

# GetComponentVisibleByDisplayStateName Method (ISwDMConfiguration12)

Gets the visibility states and path and file names of the components in the given display state.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetComponentVisibleByDisplayStateName( _
   ByVal DisplayStateName As System.String, _
   ByRef ComponentVisibleList As System.Object, _
   ByRef ComponentFileDirectory As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration12
Dim DisplayStateName As System.String
Dim ComponentVisibleList As System.Object
Dim ComponentFileDirectory As System.Object

instance.GetComponentVisibleByDisplayStateName(DisplayStateName, ComponentVisibleList, ComponentFileDirectory)
```

### C#

```csharp
void GetComponentVisibleByDisplayStateName(
   System.string DisplayStateName,
   out System.object ComponentVisibleList,
   out System.object ComponentFileDirectory
)
```

### C++/CLI

```cpp
void GetComponentVisibleByDisplayStateName(
   System.String^ DisplayStateName,
   [Out] System.Object^ ComponentVisibleList,
   [Out] System.Object^ ComponentFileDirectory
)
```

### Parameters

- `DisplayStateName`: Display state name
- `ComponentVisibleList`: Array of booleans indicating whether the components in `ComponentFileDirectory` are visible in the given display state; true if visble, false if suppressed
- `ComponentFileDirectory`: Array of paths and file names of the components in the given display state

## VBA Syntax

See [SwDMConfiguration12::GetComponentVisibleByDisplayStateName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration12~GetComponentVisibleByDisplayStateName.html).

## Examples

[Get Linked Display States (VB.NET)](Get_Linked_Display_States_Example_VBNET.htm)
[Get Linked Display States (C#)](Get_Linked_Display_States_Example_CSharp.htm)

## See Also

[ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.html)
[ISwDMConfiguration12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12_members.html)
[ISwDMConfiguration12::GetLinkedDisplayStates Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12~GetLinkedDisplayStates.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
