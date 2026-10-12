---
title: "ShowSaveMarkup Method (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "ShowSaveMarkup"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ShowSaveMarkup.html"
---

# ShowSaveMarkup Method (IEModelMarkupControl)

Saves the markup comments to either the specified file or to the default markup file.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowSaveMarkup( _
   ByVal SaveName As System.String, _
   ByVal SaveAs As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim SaveName As System.String
Dim SaveAs As System.Boolean

instance.ShowSaveMarkup(SaveName, SaveAs)
```

### C#

```csharp
void ShowSaveMarkup(
   System.string SaveName,
   System.bool SaveAs
)
```

### C++/CLI

```cpp
void ShowSaveMarkup(
   System.String^ SaveName,
   System.bool SaveAs
)
```

### Parameters

- `SaveName`: Name of the file where to save the markup comments
- `SaveAs`:

  | If... | Then.. |
  | --- | --- |
  | TRUE | A dialog is displayed prompting the user to select the markup to save and the file name to which to save the markup. SaveName is ignored. |
  | FALSE | If... Then markups from all reviewers are saved to... SaveName is empty The default file name in the current directory SaveName is specified The file specified in SaveName |
  | If... | Then markups from all reviewers are saved to... |
  | SaveName is empty | The default file name in the current directory |
  | SaveName is specified | The file specified in SaveName |

## VBA Syntax

See [EModelMarkupControl::ShowSaveMarkup](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~ShowSaveMarkup.html).

## Examples

See the [IEModelMarkupControl](eDrawings.Interop.EModelMarkupControl.html) examples.

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)
[IEModelViewControl::IsMarkupModified](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~IsMarkupModified.html)
[IEModelViewControl::OpenMarkupFile](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenMarkupFile.html)

## Availability

eDrawings API 2005 SP0
