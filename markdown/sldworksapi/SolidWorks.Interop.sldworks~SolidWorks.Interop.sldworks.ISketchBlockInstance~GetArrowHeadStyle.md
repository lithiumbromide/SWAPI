---
title: "GetArrowHeadStyle Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "GetArrowHeadStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetArrowHeadStyle.html"
---

# GetArrowHeadStyle Method (ISketchBlockInstance)

Gets the arrowhead style of the leader on this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadStyle() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Integer

value = instance.GetArrowHeadStyle()
```

### C#

```csharp
System.int GetArrowHeadStyle()
```

### C++/CLI

```cpp
System.int GetArrowHeadStyle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Arrowhead style as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

## VBA Syntax

See [SketchBlockInstance::GetArrowHeadStyle](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~GetArrowHeadStyle.html).

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::GetLeaderStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderStyle.html)
[ISketchBlockInstance::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetLeader.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
