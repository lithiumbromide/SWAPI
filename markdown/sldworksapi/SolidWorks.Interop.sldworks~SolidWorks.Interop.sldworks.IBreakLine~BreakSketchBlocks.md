---
title: "BreakSketchBlocks Property (IBreakLine)"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: "BreakSketchBlocks"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~BreakSketchBlocks.html"
---

# BreakSketchBlocks Property (IBreakLine)

Gets or sets whether to break sketch blocks.

## Syntax

### Visual Basic (Declaration)

```vb
Property BreakSketchBlocks As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakLine
Dim value As System.Boolean

instance.BreakSketchBlocks = value

value = instance.BreakSketchBlocks
```

### C#

```csharp
System.bool BreakSketchBlocks {get; set;}
```

### C++/CLI

```cpp
property System.bool BreakSketchBlocks {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to break sketch blocks, false to not

## VBA Syntax

See [BreakLine::BreakSketchBlocks](ms-its:sldworksapivb6.chm::/sldworks~BreakLine~BreakSketchBlocks.html).

## See Also

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
