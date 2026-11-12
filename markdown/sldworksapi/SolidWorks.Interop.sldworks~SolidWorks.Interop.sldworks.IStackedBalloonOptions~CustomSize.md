---
title: "CustomSize Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "CustomSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~CustomSize.html"
---

# CustomSize Property (IStackedBalloonOptions)

Gets and sets the user-defined size of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Double

instance.CustomSize = value

value = instance.CustomSize
```

### C#

```csharp
System.double CustomSize {get; set;}
```

### C++/CLI

```cpp
property System.double CustomSize {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

User-defined size of the balloons; valid only when [IStackedBalloonOptions::Size](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions~Size.html) is set to [swBalloonFit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html).swBF_UserDef

## VBA Syntax

See [StackedBalloonOptions::CustomSize](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~CustomSize.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
