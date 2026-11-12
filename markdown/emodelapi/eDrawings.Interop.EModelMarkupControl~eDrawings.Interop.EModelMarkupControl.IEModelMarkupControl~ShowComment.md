---
title: "ShowComment Method (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "ShowComment"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowComment.html"
---

# ShowComment Method (IEModelMarkupControl)

Displays the specified markup comment.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowComment( _
   ByVal CommentID As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim CommentID As System.Integer

instance.ShowComment(CommentID)
```

### C#

```csharp
void ShowComment(
   System.int CommentID
)
```

### C++/CLI

```cpp
void ShowComment(
   System.int CommentID
)
```

### Parameters

- `CommentID`: ID of markup comment to display

## VBA Syntax

See [EModelMarkupControl::ShowComment](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~ShowComment.html).

## Examples

See the [IEModelMarkupControl](eDrawings.Interop.EModelMarkupControl.html) examples.

## Remarks

Call [IEModelMarkupControl::CommentID](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentID.html) before calling this method to determine the ID of the markup comment.

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)
[IEModelMarkupControl::CommentName Property](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentName.html)
[IEModelMarkupControl::ShowCommentx64 Method](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowCommentx64.html)

## Availability

eDrawings API 2005 SP0
