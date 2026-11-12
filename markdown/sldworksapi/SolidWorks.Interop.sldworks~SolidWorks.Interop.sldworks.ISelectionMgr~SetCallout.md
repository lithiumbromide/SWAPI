---
title: "SetCallout Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "SetCallout"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetCallout.html"
---

# SetCallout Method (ISelectionMgr)

Adds a callout to the currently selected object.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCallout( _
   ByVal Index As System.Integer, _
   ByVal PCallout As Callout _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim PCallout As Callout
Dim value As System.Boolean

value = instance.SetCallout(Index, PCallout)
```

### C#

```csharp
System.bool SetCallout(
   System.int Index,
   Callout PCallout
)
```

### C++/CLI

```cpp
System.bool SetCallout(
   System.int Index,
   Callout^ PCallout
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index number of the selected object
- `PCallout`: [Callout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) (see **Remarks**)

### Return Value

True if the callout is added to the selected object, false if not

## VBA Syntax

See [SelectionMgr::SetCallout](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~SetCallout.html).

## Remarks

Use [ISelectionMgr::CreateCallout2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~CreateCallout2.html) to set the properties of the callout. Then use ISelectionMgr::SetCallout to add the callout to an already selected object.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision number 14.0
