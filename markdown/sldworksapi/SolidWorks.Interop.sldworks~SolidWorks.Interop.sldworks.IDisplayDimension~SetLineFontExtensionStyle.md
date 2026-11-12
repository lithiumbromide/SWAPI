---
title: "SetLineFontExtensionStyle Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetLineFontExtensionStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionStyle.html"
---

# SetLineFontExtensionStyle Method (IDisplayDimension)

Sets the line font style for the extension lines of this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLineFontExtensionStyle( _
   ByVal UseDoc As System.Boolean, _
   ByVal Style As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Style As System.Integer
Dim value As System.Boolean

value = instance.SetLineFontExtensionStyle(UseDoc, Style)
```

### C#

```csharp
System.bool SetLineFontExtensionStyle(
   System.bool UseDoc,
   System.int Style
)
```

### C++/CLI

```cpp
System.bool SetLineFontExtensionStyle(
   System.bool UseDoc,
   System.int Style
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True uses the document setting for the font style of extension lines, false uses the setting specified
  in Style
- `Style`: Extension line font style as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html); valid only if UseDoc = false

### Return Value

True if the extension line font style is set, false if not

## VBA Syntax

See [DisplayDimension::SetLineFontExtensionStyle](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetLineFontExtensionStyle.html).

## Remarks

After calling this method, call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetLineFontExtensionThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionThickness.html)
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.html)
[IDisplayDimension::ExtensionLineSameAsLeaderStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineSameAsLeaderStyle.html)
[IDisplayDimension::ExtensionLineUseDocumentDisplay Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineUseDocumentDisplay.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
