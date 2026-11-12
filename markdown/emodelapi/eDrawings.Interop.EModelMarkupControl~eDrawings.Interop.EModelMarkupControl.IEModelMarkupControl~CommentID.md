---
title: "CommentID Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "CommentID"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentID.html"
---

# CommentID Property (IEModelMarkupControl)

Gets the ID for the specified markup comment.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CommentID( _
   ByVal CommentIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim CommentIndex As System.Integer
Dim value As System.Integer

value = instance.CommentID(CommentIndex)
```

### C#

```csharp
System.int CommentID(
   System.int CommentIndex
) {get;}
```

### C++/CLI

```cpp
property System.int CommentID {
   System.int get(System.int CommentIndex);
}
```

### Parameters

- `CommentIndex`: Index number of the markup comment to get

### Property Value

ID of markup comment specified by CommentIndex

## VBA Syntax

See [EModelMarkupControl::CommentID](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~CommentID.html).

## Examples

See the [IEModelMarkupControl](eDrawings.Interop.EModelMarkupControl.html) example.

## Remarks

Use [IEModelMarkupControl::CommentCount](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentCount.html) before using this property to determine the index number of the markup comments.

Use this property before using:

- [IEModelMarkupControl::CommentName](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentName.html)
- [IEModelMarkupControl::ShowComment](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowComment.html)

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)
[IEModelMarkupControl::CommentIDx64 Property](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentIDx64.html)

## Availability

eDrawings API 2005 SP0
