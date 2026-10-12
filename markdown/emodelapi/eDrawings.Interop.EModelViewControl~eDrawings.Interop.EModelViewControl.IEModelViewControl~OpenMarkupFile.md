---
title: "OpenMarkupFile Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "OpenMarkupFile"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenMarkupFile.html"
---

# OpenMarkupFile Method (IEModelViewControl)

Opens the specified markup (*.markup) eDrawings file.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OpenMarkupFile( _
   ByVal inFileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim inFileName As System.String

instance.OpenMarkupFile(inFileName)
```

### C#

```csharp
void OpenMarkupFile(
   System.string inFileName
)
```

### C++/CLI

```cpp
void OpenMarkupFile(
   System.String^ inFileName
)
```

### Parameters

- `inFileName`: Fully qualified path and file name

## VBA Syntax

See [EModelViewControl::OpenMarkupFile](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OpenMarkupFile.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

To be accessed by the following methods, the markup eDrawings file must be loaded or markups must exist in the eDrawings file:

- [IEModelMarkupControl::CommentCount](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentCount.html)
- [IEModelMarkupControl::CommentID](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentID.html)
- [IEModelMarkupControl::CommentName](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~CommentName.html)
- [IEModelMarkupControl::ShowComment](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowComment.html)

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::Password Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Password.html)
[IEModelViewControl::UserName Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~UserName.html)
[IEModelViewControl::OpenDoc Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenDoc.html)

## Availability

eDrawings API 2006 SP0
