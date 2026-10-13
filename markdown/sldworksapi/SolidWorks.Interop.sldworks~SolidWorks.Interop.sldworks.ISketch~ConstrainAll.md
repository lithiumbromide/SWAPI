---
title: "ConstrainAll Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "ConstrainAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ConstrainAll.html"
---

# ConstrainAll Method (ISketch)

Attempts to solve all of the apparent relations in the sketch and returns the number
of constraints that were added to the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConstrainAll() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.ConstrainAll()
```

### C#

```csharp
System.int ConstrainAll()
```

### C++/CLI

```cpp
System.int ConstrainAll();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of constraints added

## VBA Syntax

See [Sketch::ConstrainAll](ms-its:sldworksapivb6.chm::/sldworks~Sketch~ConstrainAll.html).

## Remarks

f the sketch already has constraints, then no constraints are added (in the same
way that the user-interface button **Constrain All** can only be pressed once for a sketch.)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetConstrainedStatus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetConstrainedStatus.html)
