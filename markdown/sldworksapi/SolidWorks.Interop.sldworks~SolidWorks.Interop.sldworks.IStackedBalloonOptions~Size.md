---
title: "Size Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "Size"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~Size.html"
---

# Size Property (IStackedBalloonOptions)

Gets and sets the size of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property Size As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Integer

instance.Size = value

value = instance.Size
```

### C#

```csharp
System.int Size {get; set;}
```

### C++/CLI

```cpp
property System.int Size {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Balloon size as defined in [swBalloonFit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html); specify -1 to use the document default balloon size (see **Remarks**)

## VBA Syntax

See [StackedBalloonOptions::Size](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~Size.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

| To get or set document default values for Size... | Use... |
| --- | --- |
| Get | IModelDocExtension::GetUserPreferenceInteger ((swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, swUserPreferenceOption_e.swDetailingNoOptionSpecified) |
| Set | IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonFit_e.< Value >) |

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
