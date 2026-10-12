---
title: "UpperTextContent Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "UpperTextContent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~UpperTextContent.html"
---

# UpperTextContent Property (IStackedBalloonOptions)

Gets and sets the style of the upper text of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpperTextContent As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Integer

instance.UpperTextContent = value

value = instance.UpperTextContent
```

### C#

```csharp
System.int UpperTextContent {get; set;}
```

### C++/CLI

```cpp
property System.int UpperTextContent {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Style of the upper text as defined in [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html); specify -1 to use the document default upper text style (see **Remarks**)

## VBA Syntax

See [StackedBalloonOptions::UpperTextContent](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~UpperTextContent.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

| To get or set document default values for UpperTextContent... | Use... |
| --- | --- |
| Get | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBOMUpperText, swUserPreferenceOption_e.swDetailingNoOptionSpecified) |
| Set | IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBOMUpperText, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonTextContent_e.< Value >) |

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
