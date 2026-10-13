---
title: "GetLeaderStyle Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "GetLeaderStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderStyle.html"
---

# GetLeaderStyle Method (ISketchBlockInstance)

Gets the leader style of this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderStyle() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Integer

value = instance.GetLeaderStyle()
```

### C#

```csharp
System.int GetLeaderStyle()
```

### C++/CLI

```cpp
System.int GetLeaderStyle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Leader style as defined in [swLeaderStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html)

## VBA Syntax

See [SketchBlockInstance::GetLeaderStyle](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~GetLeaderStyle.html).

## Remarks

Use [ISketchBlockInstance::SetLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~SetLeader.html) to set the leader style.

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::GetLeaderPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderPoints.html)
[ISketchBlockInstance::IGetLeaderPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetLeaderPoints.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
