---
title: "GetUserPointsCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetUserPointsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetUserPointsCount.html"
---

# GetUserPointsCount Method (ISketchBlockDefinition)

Gets the number of user points in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPointsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Integer

value = instance.GetUserPointsCount()
```

### C#

```csharp
System.int GetUserPointsCount()
```

### C++/CLI

```cpp
System.int GetUserPointsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of user points

## VBA Syntax

See [SketchBlockDefinition::GetUserPointsCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetUserPointsCount.html).

## Remarks

Call this method before calling [ISketchBlockDefinition::IGetUserPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetUserPoints.html) to get the size of the array for that method.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetUserPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetUserPoints.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
