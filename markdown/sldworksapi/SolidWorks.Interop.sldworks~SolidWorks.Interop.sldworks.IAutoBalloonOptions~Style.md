---
title: "Style Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~Style.html"
---

# Style Property (IAutoBalloonOptions)

Gets and sets the style of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
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

Style of the balloons as defined in [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html); specify -1 to use the document default balloon style (see **Remarks**)

## VBA Syntax

See [AutoBalloonOptions::Style](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~Style.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

| To get or set document default values for Style... | Use... |
| --- | --- |
| Get | IModelDocExtension::GetUserPreferenceInteger ((swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) |
| Set | IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonStyle_e.< Value >) |

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
