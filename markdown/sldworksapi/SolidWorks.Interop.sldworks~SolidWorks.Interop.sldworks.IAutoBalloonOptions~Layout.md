---
title: "Layout Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "Layout"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~Layout.html"
---

# Layout Property (IAutoBalloonOptions)

Gets and sets the style of the layout of balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layout As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
Dim value As System.Integer

instance.Layout = value

value = instance.Layout
```

### C#

```csharp
System.int Layout {get; set;}
```

### C++/CLI

```cpp
property System.int Layout {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Style of the balloon layout as defined in [swBalloonLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonLayoutType_e.html); specify -1 to use the document default layout style (see **Remarks**)

## VBA Syntax

See [AutoBalloonOptions::Layout](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~Layout.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

| To get or set the document default values for Layout... | Use... |
| --- | --- |
| Get | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, swUserPreferenceOption_e.swDetailingNoOptionSpecified) |
| Set | IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonLayoutType_e.< Value >) |

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
