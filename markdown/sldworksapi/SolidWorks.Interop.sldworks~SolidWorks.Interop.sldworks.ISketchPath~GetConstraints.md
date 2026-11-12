---
title: "GetConstraints Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "GetConstraints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetConstraints.html"
---

# GetConstraints Method (ISketchPath)

Gets the names of the constraints in this sketch path.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConstraints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
Dim value As System.Object

value = instance.GetConstraints()
```

### C#

```csharp
System.object GetConstraints()
```

### C++/CLI

```cpp
System.Object^ GetConstraints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the names of the sketch constraints

## VBA Syntax

See [SketchPath::GetConstraints](ms-its:sldworksapivb6.chm::/Sldworks~SketchPath~GetConstraints.html).

## Examples

See the [ISketchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html) examples.

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)
[ISketchPath::GetConstraintsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetConstraintsCount.html)
[ISketchPath::IGetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~IGetConstraints.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
