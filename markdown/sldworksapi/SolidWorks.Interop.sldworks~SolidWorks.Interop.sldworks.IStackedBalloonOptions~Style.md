---
title: "Style Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~Style.html"
---

# Style Property (IStackedBalloonOptions)

Gets and sets the style of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Integer

instance.Style = value

value = instance.Style
```

### C#

```csharp
System.int Style {get; set;}
```

### C++/CLI

```cpp
property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Balloon style as defined in [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html); specify -1 to use the document default balloon style

## VBA Syntax

See [StackedBalloonOptions::Style](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~Style.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

| To get or set document default values for Style... | Use... |
| --- | --- |
| Get | IModelDocExtension::GetUserPreferenceInteger ((swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) |
| Set | IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonStyle_e.< Value >) |

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
