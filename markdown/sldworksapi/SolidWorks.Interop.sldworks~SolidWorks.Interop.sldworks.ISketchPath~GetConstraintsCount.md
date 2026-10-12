---
title: "GetConstraintsCount Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "GetConstraintsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetConstraintsCount.html"
---

# GetConstraintsCount Method (ISketchPath)

Gets the number of constraints in this sketch path.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConstraintsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
Dim value As System.Integer

value = instance.GetConstraintsCount()
```

### C#

```csharp
System.int GetConstraintsCount()
```

### C++/CLI

```cpp
System.int GetConstraintsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of constraints

## VBA Syntax

See [SketchPath::GetConstraintsCount](ms-its:sldworksapivb6.chm::/Sldworks~SketchPath~GetConstraintsCount.html).

## Examples

See the [ISketchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html) examples.

## Remarks

Call this method before calling [ISketchPath::IGetConstraints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath~IGetConstraints.html) to get the size of the array for that method.

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)
[ISketchPath::GetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetConstraints.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
