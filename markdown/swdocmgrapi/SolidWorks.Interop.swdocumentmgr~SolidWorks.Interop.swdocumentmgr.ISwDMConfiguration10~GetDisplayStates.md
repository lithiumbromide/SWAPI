---
title: "GetDisplayStates Method (ISwDMConfiguration10)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration10"
member: "GetDisplayStates"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10~GetDisplayStates.html"
---

# GetDisplayStates Method (ISwDMConfiguration10)

Gets the names of the display states for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayStates() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration10
Dim value As System.Object

value = instance.GetDisplayStates()
```

### C#

```csharp
System.object GetDisplayStates()
```

### C++/CLI

```cpp
System.Object^ GetDisplayStates();
```

### Return Value

Array of the names of the display states for this configuration

## VBA Syntax

See [SwDMConfiguration10::GetDisplayStates](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration10~GetDisplayStates.html).

## Remarks

The first name in the list is the active display state.

## See Also

[ISwDMConfiguration10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10.html)
[ISwDMConfiguration10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10_members.html)

## Availability

SOLIDWORKS Document Manager API 2008 SP5
