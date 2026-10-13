---
title: "GetSelectedObjectsBBox Method (ISwAddinBroker)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwAddinBroker"
member: "GetSelectedObjectsBBox"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinBroker~GetSelectedObjectsBBox.html"
---

# GetSelectedObjectsBBox Method (ISwAddinBroker)

Gets the selected entities bounding box from an add-in.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSelectedObjectsBBox( _
   ByVal pDoc As System.Object, _
   ByVal Option As System.Integer, _
   ByRef BoxCorners As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwAddinBroker
Dim pDoc As System.Object
Dim Option As System.Integer
Dim BoxCorners As System.Object

instance.GetSelectedObjectsBBox(pDoc, Option, BoxCorners)
```

### C#

```csharp
void GetSelectedObjectsBBox(
   System.object pDoc,
   System.int Option,
   out System.object BoxCorners
)
```

### C++/CLI

```cpp
void GetSelectedObjectsBBox(
   System.Object^ pDoc,
   System.int Option,
   [Out] System.Object^ BoxCorners
)
```

### Parameters

- `pDoc`: SOLIDWORKS document
- `Option`: Option as defined in [swAddinBrokerBBoxOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddinBrokerBBoxOption_e.html)
- `BoxCorners`: Array of six doubles of the points of the bounding box

## VBA Syntax

See [SwAddinBroker::GetSelectedObjectsBBox](ms-its:swpublishedapivb6.chm::/swpublished~SwAddinBroker~GetSelectedObjectsBBox.html).

## Remarks

The order of the points follows the same convention as all SOLIDWORKS bounding boxes.

## See Also

[ISwAddinBroker Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinBroker.html)
[ISwAddinBroker Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinBroker_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
