---
title: "GetRelations Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "GetRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetRelations.html"
---

# GetRelations Method (ISketchPath)

Gets the sketch relations for this sketch path.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
Dim value As System.Object

value = instance.GetRelations()
```

### C#

```csharp
System.object GetRelations()
```

### C++/CLI

```cpp
System.Object^ GetRelations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch relations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html)

## VBA Syntax

See [SketchPath::GetRelations](ms-its:sldworksapivb6.chm::/Sldworks~SketchPath~GetRelations.html).

## Examples

See the [ISketchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html) examples.

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)
[ISketchPath::GetRelationsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetRelationsCount.html)
[ISketchPath::IGetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~IGetRelations.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
