---
title: "IAddDisplayText Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "IAddDisplayText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText.html"
---

# IAddDisplayText Method (IDisplayDimension)

Overrides the display text for this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddDisplayText( _
   ByVal Text As System.String, _
   ByRef Position As System.Double, _
   ByVal Format As TextFormat, _
   ByVal Attachment As System.Integer, _
   ByVal WidthFactor As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim Text As System.String
Dim Position As System.Double
Dim Format As TextFormat
Dim Attachment As System.Integer
Dim WidthFactor As System.Double
Dim value As System.Boolean

value = instance.IAddDisplayText(Text, Position, Format, Attachment, WidthFactor)
```

### C#

```csharp
System.bool IAddDisplayText(
   System.string Text,
   ref System.double Position,
   TextFormat Format,
   System.int Attachment,
   System.double WidthFactor
)
```

### C++/CLI

```cpp
System.bool IAddDisplayText(
   System.String^ Text,
   System.double% Position,
   TextFormat^ Format,
   System.int Attachment,
   System.double WidthFactor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`: Text to display
- `Position`: Location of the text; pointer to an array of 3 doubles
- `Format`: Pointer to [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object
- `Attachment`: Justification of the text as defined in [swTextJustification_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextJustification_e.html)
- `WidthFactor`: Horizontal scale factor of the text

### Return Value

True if successful, false if not

## VBA Syntax

See [DisplayDimension::IAddDisplayText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~IAddDisplayText.html).

## Remarks

The new graphics displayed by this method are temporary. When the user changes the dimension, this display dimension reverts back to the SOLIDWORKS standard.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::AddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayText.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
