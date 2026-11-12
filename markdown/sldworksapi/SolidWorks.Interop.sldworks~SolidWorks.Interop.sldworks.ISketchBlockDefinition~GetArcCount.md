---
title: "GetArcCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetArcCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetArcCount.html"
---

# GetArcCount Method (ISketchBlockDefinition)

Gets the number of arcs in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Integer

value = instance.GetArcCount()
```

### C#

```csharp
System.int GetArcCount()
```

### C++/CLI

```cpp
System.int GetArcCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of arcs

## VBA Syntax

See [SketchBlockDefinition::GetArcCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetArcCount.html).

## Examples

[Get Block Instance in Part or Assembly (VBA)](Get_Block_Instance_in_Part_or_Assembly_Example_VB.htm)

## Remarks

Call this method before calling [ISketchBlockDefinition::IGetArcs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetArcs.html) to get the size of the array for that method.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefintion::GetArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetArcs.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
