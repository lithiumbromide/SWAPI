---
title: "OnStringValueChanged Method (ISwCalloutHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwCalloutHandler"
member: "OnStringValueChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwCalloutHandler~OnStringValueChanged.html"
---

# OnStringValueChanged Method (ISwCalloutHandler)

Allows access to and modifcation of text in a specific row in a callout.

## Syntax

### Visual Basic (Declaration)

```vb
Function OnStringValueChanged( _
   ByVal pManipulator As System.Object, _
   ByVal RowID As System.Integer, _
   ByVal Text As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwCalloutHandler
Dim pManipulator As System.Object
Dim RowID As System.Integer
Dim Text As System.String
Dim value As System.Boolean

value = instance.OnStringValueChanged(pManipulator, RowID, Text)
```

### C#

```csharp
System.bool OnStringValueChanged(
   System.object pManipulator,
   System.int RowID,
   System.string Text
)
```

### C++/CLI

```cpp
System.bool OnStringValueChanged(
   System.Object^ pManipulator,
   System.int RowID,
   System.String^ Text
)
```

### Parameters

- `pManipulator`: [ICallout](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) object whose text was edited
- `RowID`: Row in which the text was edi
- `Text`: New text of RowID

### Return Value

True to use updated text in RowID, false to use original text in RowID

## VBA Syntax

See [SwCalloutHandler::OnStringValueChanged](ms-its:swpublishedapivb6.chm::/swpublished~SwCalloutHandler~OnStringValueChanged.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

## See Also

[ISwCalloutHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwCalloutHandler.html)
[ISwCalloutHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwCalloutHandler_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
