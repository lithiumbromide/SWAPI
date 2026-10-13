---
title: "GetParabolaCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetParabolaCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetParabolaCount.html"
---

# GetParabolaCount Method (ISketchBlockDefinition)

Gets the number of parabolas in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParabolaCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Integer

value = instance.GetParabolaCount()
```

### C#

```csharp
System.int GetParabolaCount()
```

### C++/CLI

```cpp
System.int GetParabolaCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of parabolas

## VBA Syntax

See [SketchBlockDefinition::GetParabolaCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetParabolaCount.html).

## Remarks

Call this method before calling [ISketchBlockDefinition::IGetParabolas](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetParabolas.html) to get the size of the array for that method.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetParabolas Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetParabolas.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
