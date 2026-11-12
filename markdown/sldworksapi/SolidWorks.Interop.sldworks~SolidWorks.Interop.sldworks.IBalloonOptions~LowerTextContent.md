---
title: "LowerTextContent Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "LowerTextContent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~LowerTextContent.html"
---

# LowerTextContent Property (IBalloonOptions)

Gets and sets the style of the lower text of the balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property LowerTextContent As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
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

Style of the lower text as defined in [swBalloonTextContent_e](ms-its:swconst.chm::/Solidworks.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html); specify -1 to use the document default lower text style (See **Remarks**)

## VBA Syntax

See [BalloonOptions::LowerTextContent](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~LowerTextContent.html).

## Remarks

This property is valid only when [IBalloonOptions::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions~Style.html) is set to [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html).swBS_SplitCirc.

| To get or set document default values... | Use... |
| --- | --- |
| Get | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBOMLowerText, swUserPreferenceOption_e.swDetailingNoOptionSpecified) |
| Set | IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBOMLowerText, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonTextContent_e.< Value >) |

See:

- [INote::PropertyLinkedText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.html) for examples of link strings usable with swBalloonTextContent_e.swBalloonTextCustomProperties.
- SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
