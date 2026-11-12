---
title: "GetBrokenLeader2 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetBrokenLeader2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBrokenLeader2.html"
---

# GetBrokenLeader2 Method (IDisplayDimension)

Gets whether this display dimension has a broken or split leader.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBrokenLeader2() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.GetBrokenLeader2()
```

### C#

```csharp
System.int GetBrokenLeader2()
```

### C++/CLI

```cpp
System.int GetBrokenLeader2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Broken leader value as defined in [swDisplayDimensionLeaderText_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayDimensionLeaderText_e.html)

## VBA Syntax

See [DisplayDimension::GetBrokenLeader2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetBrokenLeader2.html).

## Remarks

Dimension text can be displayed above a solid leader line or the dimension leader line can be broken with the text displayed either horizontal or aligned with the leader line. You can use this method to determine which setting is used by this display dimension.

The setting can be local to the display dimension, or the display dimension might use the default document setting. This method returns a valid value only if it is using a local setting; if this display dimension uses the default document setting, it returns -1.

Use [IDisplayDimension::SetBrokenLeader2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetBrokenLeader2.html) to set this value.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetUseDocBrokenLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBrokenLeader.html)
[IDisplayDimension::SetBrokenLeader2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBrokenLeader2.html)
[IDisplayDimension::SolidLeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SolidLeader.html)

## Availability

SOLIDWORKS 99, datecode 1999207
