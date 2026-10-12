---
title: "GetEllipseCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetEllipseCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetEllipseCount.html"
---

# GetEllipseCount Method (ISketchBlockDefinition)

Gets the number of ellipses in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEllipseCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Integer

value = instance.GetEllipseCount()
```

### C#

```csharp
System.int GetEllipseCount()
```

### C++/CLI

```cpp
System.int GetEllipseCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of ellipses

## VBA Syntax

See [SketchBlockDefinition::GetEllipseCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetEllipseCount.html).

## Remarks

Call this method before calling [ISketchBlockDefinition::IGetEllipses](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetEllipses.html) to get the size of the array for that method.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetEllipses Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetEllipses.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
