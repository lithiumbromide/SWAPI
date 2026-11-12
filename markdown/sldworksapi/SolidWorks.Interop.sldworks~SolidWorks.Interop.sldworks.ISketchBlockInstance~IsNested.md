---
title: "IsNested Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "IsNested"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IsNested.html"
---

# IsNested Method (ISketchBlockInstance)

Gets whether this sketch block instance is nested within another block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsNested() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Boolean

value = instance.IsNested()
```

### C#

```csharp
System.bool IsNested()
```

### C++/CLI

```cpp
System.bool IsNested();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if nested within another block definition, false if not

## VBA Syntax

See [SketchBlockInstance::IsNested](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~IsNested.html).

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
