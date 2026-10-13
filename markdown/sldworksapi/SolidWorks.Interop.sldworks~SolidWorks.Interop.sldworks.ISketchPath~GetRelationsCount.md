---
title: "GetRelationsCount Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "GetRelationsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetRelationsCount.html"
---

# GetRelationsCount Method (ISketchPath)

Gets the number of sketch relations in this sketch path.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelationsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
Dim value As System.Integer

value = instance.GetRelationsCount()
```

### C#

```csharp
System.int GetRelationsCount()
```

### C++/CLI

```cpp
System.int GetRelationsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch relations

## VBA Syntax

See [SketchPath::GetRelationsCount](ms-its:sldworksapivb6.chm::/Sldworks~SketchPath~GetRelationsCount.html).

## Examples

See the [ISketchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html) examples.

## Remarks

Call this method before calling [ISketchPath::IGetRelations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath~IGetRelations.html) to get the size of the array for that method.

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)
[ISketchPath::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetRelations.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
