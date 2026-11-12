---
title: "ShowCommentx64 Method (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "ShowCommentx64"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowCommentx64.html"
---

# ShowCommentx64 Method (IEModelMarkupControl)

Displays the specified markup comment on 64-bit systems.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowCommentx64( _
   ByVal CommentIDx64 As System.Long _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim CommentIDx64 As System.Long

instance.ShowCommentx64(CommentIDx64)
```

### C#

```csharp
void ShowCommentx64(
   System.long CommentIDx64
)
```

### C++/CLI

```cpp
void ShowCommentx64(
   System.int64 CommentIDx64
)
```

### Parameters

- `CommentIDx64`: ID of markup comment to display on 64-bit systems

## VBA Syntax

See [EModelMarkupControl::ShowCommentx64](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~ShowCommentx64.html).

## Remarks

Call [IEModelMarkupControl::CommentIDx64](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentIDx64.html) before calling this method to determine the ID of the markup comment.

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)
[IEModelMarkupControl::ShowComment Method](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowComment.html)

## Availability

eDrawings API 2011 SP01
