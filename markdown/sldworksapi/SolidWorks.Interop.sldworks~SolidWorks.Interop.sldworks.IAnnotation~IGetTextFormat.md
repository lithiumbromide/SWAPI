---
title: "IGetTextFormat Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "IGetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.html"
---

# IGetTextFormat Method (IAnnotation)

Gets the text format for the specified text in this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTextFormat( _
   ByVal Index As System.Integer _
) As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Index As System.Integer
Dim value As TextFormat

value = instance.IGetTextFormat(Index)
```

### C#

```csharp
TextFormat IGetTextFormat(
   System.int Index
)
```

### C++/CLI

```cpp
TextFormat^ IGetTextFormat(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Number indicating which text within this annotation to check

### Return Value

Pointer to [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) of the specified piece of text

## VBA Syntax

See [Annotation::IGetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~Annotation~IGetTextFormat.html).

## Remarks

The behavior of this method differs depending on the type of annotation.

- [Datum Target](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag.html) and [Datum Feature Symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym.html)

  These symbols always use the document default setting for dimension text format to
  display text within the symbol. The index argument is not used and should be set
  to 0.
- [Geometric Tolerance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html), [Display Dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html), [Simple Notes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html), [Surface Finish](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html), and [Weld Symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html)

  These symbols can either use the document default setting to display text within
  the symbol (dimension text setting for the geometric tolerance symbols and display
  dimensions, or note text setting for notes) or they can use a local format. The index
  argument is not used and should be set to 0.
- [Blocks](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html) (and compound notes in documents created in SOLIDWORKS 2015 and earlier)

  These symbols might contain several different pieces of text; each piece can use
  the document default setting for notes or a local format. The index argument identifies
  the text. The index value is 0-based. If the index value is invalid, then this method
  returns a NULL pointer. To get the number of text or [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) objects, use [IAnnotation::GetTextFormatCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetTextFormatCount.html).
- Rich Text Format

  If a note contains embedded rich text information in the string, this method returns
  a text format that does not necessarily reflect what is displayed on the screen for
  that note. Use [INote::HasMultipleFonts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~HasMultipleFonts.html) to determine if the note contains embedded
  rich text information.

ITextFormat is returned if it is for a local setting or for the document
default setting. To determine whether or not this annotation is using the document
default settings for text format, use [IAnnotation::GetUseDocTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetUseDocTextFormat.html). To set the
text format information, use [IAnnotation::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetTextFormat.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.html)
[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.html)
[IAnnotation::GetTextFormatCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount.html)
[IAnnotation::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.html)
[IAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0.
