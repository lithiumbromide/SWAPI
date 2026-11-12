---
title: "GetUseDocTextFormat Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetUseDocTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat.html"
---

# GetUseDocTextFormat Method (IAnnotation)

Gets whether SOLIDWORKS is currently using the document default text format setting for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocTextFormat( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.GetUseDocTextFormat(Index)
```

### C#

```csharp
System.bool GetUseDocTextFormat(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool GetUseDocTextFormat(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Number indicating which text within this annotation to check (see **Remarks**)

### Return Value

True if the setting is a document default setting, false if not

## VBA Syntax

See [Annotation::GetUseDocTextFormat](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetUseDocTextFormat.html).

## Remarks

The behavior of this method differs slightly depending on the type of annotation.

- [Weld](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html), [Datum Target](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym.html), [Datum Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag.html), and [Surface Finish](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html) Symbols

  These symbols always use the document default setting for dimension text format of the text objects within the symbol. Therefore, this method always returns True for these annotation types. The index argument is not used and should be set to 0.
- [Geometric Tolerance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html) Symbols, [Display Dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html), and [Simple Notes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

  These symbols can use the document default setting to display all of the text objects within the symbol (dimension text setting for the geometric tolerance symbols and display dimensions, or note text setting for notes), in which case this method returns True. They can also use a local format, in which case this method returns false. The index argument is not used and should be set to 0.
- [Blocks](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html) (and compound notes created in SOLIDWORKS 2015 and earlier)

  These symbols can contain several different pieces of text, each individually using the document default setting for notes or a local format. The index argument identifies the text. The index value is 0-based. If the index value is invalid, this method returns True. To get the number of text or text format objects, use [IAnnotation::GetTextFormatCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetTextFormatCount.html).

To get the text format object for this annotation, use [IAnnotation::GetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetTextFormat.html), [IAnnotation::IGetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetTextFormat.html), [IAnnotation::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetTextFormat.html), or [IAnnotation::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~ISetTextFormat.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
