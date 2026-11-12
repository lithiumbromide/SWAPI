---
title: "AddDisplayText Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "AddDisplayText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayText.html"
---

# AddDisplayText Method (IDisplayDimension)

Overrides the display text.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDisplayText( _
   ByVal Text As System.String, _
   ByVal Position As System.Object, _
   ByVal Format As System.Object, _
   ByVal Attachment As System.Integer, _
   ByVal WidthFactor As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim Text As System.String
Dim Position As System.Object
Dim Format As System.Object
Dim Attachment As System.Integer
Dim WidthFactor As System.Double
Dim value As System.Boolean

value = instance.AddDisplayText(Text, Position, Format, Attachment, WidthFactor)
```

### C#

```csharp
System.bool AddDisplayText(
   System.string Text,
   System.object Position,
   System.object Format,
   System.int Attachment,
   System.double WidthFactor
)
```

### C++/CLI

```cpp
System.bool AddDisplayText(
   System.String^ Text,
   System.Object^ Position,
   System.Object^ Format,
   System.int Attachment,
   System.double WidthFactor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`: Text to display
- `Position`: Location of the text; array of 3 doubles
- `Format`: Object for the text format
- `Attachment`: Justification of the text as defined in [swTextJustification_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextJustification_e.html)
- `WidthFactor`: Horizontal scale factor of the text

### Return Value

True if successful, false if not

## VBA Syntax

See [DisplayDimension::AddDisplayText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~AddDisplayText.html).

## Examples

[Replace Dimension with Text (VBA)](Replace_Dimension_with_Text_Example_VB.htm)

## Remarks

The new graphics displayed by this method are temporary. When the user changes the dimension, this display dimension reverts back to the SOLIDWORKS standard.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::IAddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText.html)
[IDisplayDimension::HorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~HorizontalJustification.html)
[IDisplayDimension::VerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~VerticalJustification.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
