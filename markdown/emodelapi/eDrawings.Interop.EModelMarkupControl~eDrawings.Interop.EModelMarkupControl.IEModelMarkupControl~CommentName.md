---
title: "CommentName Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "CommentName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentName.html"
---

# CommentName Property (IEModelMarkupControl)

Gets the name of the specified markup comment.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CommentName( _
   ByVal CommentIndex As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim CommentIndex As System.Integer
Dim value As System.String

value = instance.CommentName(CommentIndex)
```

### C#

```csharp
System.string CommentName(
   System.int CommentIndex
) {get;}
```

### C++/CLI

```cpp
property System.String^ CommentName {
   System.String^ get(System.int CommentIndex);
}
```

### Parameters

- `CommentIndex`: Index number indicating the markup comment to get

### Property Value

Name of markup comment specified by CommentIndex

## VBA Syntax

See [EModelMarkupControl::CommentName](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~CommentName.html).

## Examples

See the [IEModelMarkupControl](eDrawings.Interop.EModelMarkupControl.html) example.

## Remarks

Call [IEModelMarkupControl::CommentCount](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentCount.html) before calling this property to get the index number of the markup comments

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)
[IEModelMarkupControl::ShowComment Method](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowComment.html)
[IEModelMarkupControl::CommentID Property](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentID.html)
[IEModelMarkupControl::ShowCommentx64 Method ()](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowCommentx64.html)
[IEModelMarkupControl::CommentCountx64 Property ()](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentCountx64.html)
[IEModelMarkupControl::CommentIDx64 Property ()](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentIDx64.html)

## Availability

eDrawings API 2005 SP0
