---
title: "CreateCallout2 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "CreateCallout2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateCallout2.html"
---

# CreateCallout2 Method (ISelectionMgr)

Creates a callout for the selection.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCallout2( _
   ByVal NumberOfRows As System.Integer, _
   ByVal LpHandler As System.Object _
) As Callout
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim NumberOfRows As System.Integer
Dim LpHandler As System.Object
Dim value As Callout

value = instance.CreateCallout2(NumberOfRows, LpHandler)
```

### C#

```csharp
Callout CreateCallout2(
   System.int NumberOfRows,
   System.object LpHandler
)
```

### C++/CLI

```cpp
Callout^ CreateCallout2(
   System.int NumberOfRows,
   System.Object^ LpHandler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumberOfRows`: Number of rows in the callout
- `LpHandler`: Pointer to the event handler for the callout ([ISwCalloutHandler](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwCalloutHandler.html))

### Return Value

[Callout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html)

## VBA Syntax

See [SelectionMgr::CreateCallout2](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~CreateCallout2.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

## Remarks

To create a callout independent of a selection, use [IModelDocExtension::CreateCallout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateCallout.html).

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::SetCallout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetCallout.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
