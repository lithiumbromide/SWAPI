---
title: "SetAutomaticSolve Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "SetAutomaticSolve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~SetAutomaticSolve.html"
---

# SetAutomaticSolve Method (ISketch)

Controls whether the computation to solve the sketch geometry of the part as modifications are automatically performed.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAutomaticSolve( _
   ByVal SolveFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim SolveFlag As System.Boolean
Dim value As System.Boolean

value = instance.SetAutomaticSolve(SolveFlag)
```

### C#

```csharp
System.bool SetAutomaticSolve(
   System.bool SolveFlag
)
```

### C++/CLI

```cpp
System.bool SetAutomaticSolve(
   System.bool SolveFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SolveFlag`: True if solving is on, false if it is off

### Return Value

True if set, false if not

## VBA Syntax

See [Sketch::SetAutomaticSolve](ms-its:sldworksapivb6.chm::/sldworks~Sketch~SetAutomaticSolve.html).

## Remarks

If an application is making many changes in a sketch, then the Automatic Solve option may be turned off temporarily. After changes are completed, this option should be restored to its previous value, which can be obtained by calling [ISketch::GetAutomaticSolve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetAutomaticSolve.html) before calling this method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[IModelDoc2::AutoSolveToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AutoSolveToggle.html)
