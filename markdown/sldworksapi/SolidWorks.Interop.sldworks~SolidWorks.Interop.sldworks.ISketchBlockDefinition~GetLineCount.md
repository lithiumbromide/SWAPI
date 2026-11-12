---
title: "GetLineCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetLineCount.html"
---

# GetLineCount Method (ISketchBlockDefinition)

Gets the number of lines in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Integer

value = instance.GetLineCount()
```

### C#

```csharp
System.int GetLineCount()
```

### C++/CLI

```cpp
System.int GetLineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of lines

## VBA Syntax

See [SketchBlockDefinition::GetLineCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetLineCount.html).

## Examples

[Get Block Instance in Part or Assembly (VBA)](Get_Block_Instance_in_Part_or_Assembly_Example_VB.htm)

## Remarks

Call this method before calling [ISketchBlockDefinition::IGetLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetLines.html) to get the size of the array for that method.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetLines.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
