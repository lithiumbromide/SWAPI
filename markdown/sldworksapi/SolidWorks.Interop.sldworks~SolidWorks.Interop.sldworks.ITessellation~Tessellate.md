---
title: "Tessellate Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "Tessellate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~Tessellate.html"
---

# Tessellate Method (ITessellation)

Performs the tessellation.

## Syntax

### Visual Basic (Declaration)

```vb
Function Tessellate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim value As System.Boolean

value = instance.Tessellate()
```

### C#

```csharp
System.bool Tessellate()
```

### C++/CLI

```cpp
System.bool Tessellate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if successful, false if not

## VBA Syntax

See [Tessellation::Tessellate](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~Tessellate.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
