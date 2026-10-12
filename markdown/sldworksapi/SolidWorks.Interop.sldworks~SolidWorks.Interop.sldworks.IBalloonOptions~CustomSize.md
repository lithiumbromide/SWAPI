---
title: "CustomSize Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "CustomSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~CustomSize.html"
---

# CustomSize Property (IBalloonOptions)

Gets and sets the user-defined size of the balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomSize As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
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

User-defined size of balloons; valid only when [IBalloonOptions::Size](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions~Size.html) is set to [swBalloonFit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html).swBF_UserDef

## VBA Syntax

See [BalloonOptions::CustomSize](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~CustomSize.html).

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
