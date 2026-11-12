---
title: "GetConstrainedStatus Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetConstrainedStatus"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetConstrainedStatus.html"
---

# GetConstrainedStatus Method (ISketch)

Gets the current constrained status of the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConstrainedStatus() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetConstrainedStatus()
```

### C#

```csharp
System.int GetConstrainedStatus()
```

### C++/CLI

```cpp
System.int GetConstrainedStatus();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Constrained status as defined in [swConstrainedStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstrainedStatus_e.html)

## VBA Syntax

See [Sketch::GetConstrainedStatus](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetConstrainedStatus.html).

## Examples

[Get Sketch Constraints (VBA)](Get_Sketch_Constraints_Example_VB.htm)
[Autodimension All Sketches (C#)](Autodimension_All_Sketches_Example_CSharp.htm)
[Autodimension All Sketches (VB.NET)](Autodimension_All_Sketches_Example_VBNET.htm)
[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::ConstrainAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ConstrainAll.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
