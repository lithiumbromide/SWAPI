---
title: "GetUserPointsCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetUserPointsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPointsCount.html"
---

# GetUserPointsCount Method (ISketch)

Gets the number of user points in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserPointsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
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

Number of user points in the sketch

## VBA Syntax

See [Sketch::GetUserPointsCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetUserPointsCount.html).

## Examples

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

## Remarks

Call this method before calling [ISketch::IGetUserPoints2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetUserPoints2.html) to get the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IGetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.html)
[ISketch::GetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPoints2.html)
[ISketch::GetUserPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPointsCount.html)
[ISketch::IGetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.html)
