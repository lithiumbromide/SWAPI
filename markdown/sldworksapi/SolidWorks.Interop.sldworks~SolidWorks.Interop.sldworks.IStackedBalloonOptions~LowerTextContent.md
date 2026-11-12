---
title: "LowerTextContent Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "LowerTextContent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~LowerTextContent.html"
---

# LowerTextContent Property (IStackedBalloonOptions)

Gets and sets the style of the lower text of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property LowerTextContent As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Integer

instance.LowerTextContent = value

value = instance.LowerTextContent
```

### C#

```csharp
System.int LowerTextContent {get; set;}
```

### C++/CLI

```cpp
property System.int LowerTextContent {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Style of the lower text of the balloons as defined in [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html); specify -1 to use the document default lower text style (see **Remarks**)

## VBA Syntax

See [StackedBalloonOptions::LowerTextContent](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~LowerTextContent.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

This property is valid only when [IStackedBalloonOptions::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions~Style.html) is set to [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html).swBS_SplitCirc.

| To get or set document default values for LowerTextContent... | Use... |
| --- | --- |
| Get | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBOMLowerText, swUserPreferenceOption_e.swDetailingNoOptionSpecified) |
| Set | IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBOMLowerText, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonTextContent_e.< Value >) |

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
