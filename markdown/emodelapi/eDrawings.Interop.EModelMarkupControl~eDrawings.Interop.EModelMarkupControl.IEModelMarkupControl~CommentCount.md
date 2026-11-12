---
title: "CommentCount Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "CommentCount"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentCount.html"
---

# CommentCount Property (IEModelMarkupControl)

Gets the total number of markup comments.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CommentCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim value As System.Integer

value = instance.CommentCount
```

### C#

```csharp
System.int CommentCount {get;}
```

### C++/CLI

```cpp
property System.int CommentCount {
   System.int get();
}
```

### Property Value

Number of total markup comments

## VBA Syntax

See [EModelMarkupControl::CommentCount](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~CommentCount.html).

## Examples

See the [IEModelMarkupControl](eDrawings.Interop.EModelMarkupControl.html) example.

## Remarks

Call this method before calling [IEModelMarkupControl::CommentID](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentID.html).

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)
[IEModelMarkupControl::ShowComment Method](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowComment.html)
[IEModelMarkupControl::CommentName Property](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentName.html)

## Availability

eDrawings API 2005 SP0
