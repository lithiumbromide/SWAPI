---
title: "CommentIDx64 Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "CommentIDx64"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentIDx64.html"
---

# CommentIDx64 Property (IEModelMarkupControl)

Gets the ID for the specified markup comment on 64-bit systems.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CommentIDx64( _
   ByVal CommentIndex As System.Integer _
) As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim CommentIndex As System.Integer
Dim value As System.Long

value = instance.CommentIDx64(CommentIndex)
```

### C#

```csharp
System.long CommentIDx64(
   System.int CommentIndex
) {get;}
```

### C++/CLI

```cpp
property System.int64 CommentIDx64 {
   System.int64 get(System.int CommentIndex);
}
```

### Parameters

- `CommentIndex`: Index number of the markup comment to get on 64-bit systems

### Property Value

ID of markup comment specified by CommentIndex

## VBA Syntax

See [EModelMarkupControl::CommentIDx64](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~CommentIDx64.html).

## Remarks

Use [IEModelMarkupControl::CommentCountx64](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentCountx64.html) before using this property to determine the index number of the markup comments.

Use this property before using:

- [IEModelMarkupControl::CommentName](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentName.html)
- [IEModelMarkupControl::ShowCommentx64](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowCommentx64.html)

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)
[IEModelMarkupControl::CommentID Property](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentID.html)

## Availability

eDrawings API 2011 SP01
