---
title: "ITessellation Interface"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html"
---

# ITessellation Interface

Used to gather tessellation information from a SOLIDWORKS body.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ITessellation
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
```

### C#

```csharp
public interface ITessellation
```

### C++/CLI

```cpp
public interface class ITessellation
```

## VBA Syntax

See [Tessellation](ms-its:sldworksapivb6.chm::/sldworks~Tessellation.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## Remarks

Allows you to specify certain tolerances to adjust the information that is returned that describes the tessellation of this body.

## Accessors

[IBody2::GetTessellation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetTessellation.html) and [IBody2::IGetTessellation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetTessellation.html)

## Access Diagram

[Tessellation](SWObjectModel.pdf#Tessellation)

## See Also

[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
