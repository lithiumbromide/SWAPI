---
title: "AutoSolveToggle Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AutoSolveToggle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AutoSolveToggle.html"
---

# AutoSolveToggle Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::AutoSolve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AutoSolve.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub AutoSolveToggle()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.AutoSolveToggle()
```

### C#

```csharp
void AutoSolveToggle()
```

### C++/CLI

```cpp
void AutoSolveToggle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::AutoSolveToggle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AutoSolveToggle.html).

## Remarks

If this method is set on, then computations are solved automatically. When you are in the process of changing many dimensions in an active sketch, you may want to temporarily turn off automatic solving.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
