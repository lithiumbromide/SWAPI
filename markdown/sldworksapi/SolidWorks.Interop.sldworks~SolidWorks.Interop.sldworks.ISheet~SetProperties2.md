---
title: "SetProperties2 Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SetProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties2.html"
---

# SetProperties2 Method (ISheet)

Sets the properties for this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetProperties2( _
   ByVal PaperSz As System.Integer, _
   ByVal Templ As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal FirstAngle As System.Boolean, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double, _
   ByVal SameCustomPropAsSheetInDocProp As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim PaperSz As System.Integer
Dim Templ As System.Integer
Dim Scale1 As System.Double
Dim Scale2 As System.Double
Dim FirstAngle As System.Boolean
Dim Width As System.Double
Dim Height As System.Double
Dim SameCustomPropAsSheetInDocProp As System.Boolean

instance.SetProperties2(PaperSz, Templ, Scale1, Scale2, FirstAngle, Width, Height, SameCustomPropAsSheetInDocProp)
```

### C#

```csharp
void SetProperties2(
   System.int PaperSz,
   System.int Templ,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.double Width,
   System.double Height,
   System.bool SameCustomPropAsSheetInDocProp
)
```

### C++/CLI

```cpp
void SetProperties2(
   System.int PaperSz,
   System.int Templ,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.double Width,
   System.double Height,
   System.bool SameCustomPropAsSheetInDocProp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PaperSz`: Paper size as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html) (see **Remarks**)
- `Templ`: Template as defined in [swDwgTemplates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html) (see **Remarks**)
- `Scale1`: Scale numerator (see **Remarks**)
- `Scale2`: Scale denominator (see **Remarks**)
- `FirstAngle`: True if you want first angle projection, false if not
- `Width`: Custom paper width if PaperSz = swDwgPaperSizes_e.swDwgPaperUserDefined (see **Remarks**)
- `Height`: Custom paper height if PaperSz = swDwgPaperSizes_e.swDwgPaperUserDefined (see **Remarks**)
- `SameCustomPropAsSheetInDocProp`: True to select the **Same as sheet specified in Document Properties** check box in the Sheet Properties dialog, false to not (see **Remarks**)

## VBA Syntax

See [Sheet::SetProperties2](ms-its:sldworksapivb6.chm::/sldworks~Sheet~SetProperties2.html).

## Examples

[Set Drawing Sheet Properties (C#)](Set_Drawing_Sheet_Properties_Example_CSharp.htm)
[Set Drawing Sheet Properties (VB.NET)](Set_Drawing_Sheet_Properties_Example_VBNET.htm)
[Set Drawing Sheet Properties (VBA)](Set_Drawing_Sheet_Properties_Example_VB.htm)

## Remarks

| If you... | Then... |
| --- | --- |
| Specify a custom template | The current custom template is used by this sheet until you call ISheet::SetTemplateName and pass in a different custom template name. |
| Specify a value for Templ that does not match PaperSz | The template does not fit the paper size. Templ does not override the PaperSz setting. |
| Change the scale of the sheet using Scale1 and Scale2 | Any drawing view that is set to use the sheet's scale takes the new scale setting. |
| Set SameCustomPropAsSheetInDocProp to true | The Tools > Options > Document Properties > Drawing Sheets > Use custom property values from the sheet check box must be preselected. |

**NOTE:** You can also use [ISheet::SetSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SetSize.html) to set the size of the sheet and the standard sheet size.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetProperties2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties2.html)
[ISheet::GetTemplateName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.html)
[ISheet::SetTemplateName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.html)
[ISheet::GetSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.html)
[ISheet::PageSetup Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
