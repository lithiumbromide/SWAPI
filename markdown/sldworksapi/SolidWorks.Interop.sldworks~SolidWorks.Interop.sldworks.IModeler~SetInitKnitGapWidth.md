---
title: "SetInitKnitGapWidth Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "SetInitKnitGapWidth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetInitKnitGapWidth.html"
---

# SetInitKnitGapWidth Method (IModeler)

Sets the initial gap bound width for sewing a body. Call this method before calling any calls that attempt to knit a body; for example, [IBody2::CreateBodyFromSurfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBodyFromSurfaces.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetInitKnitGapWidth( _
   ByVal InitGapWidth As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim InitGapWidth As System.Double
Dim value As System.Boolean

value = instance.SetInitKnitGapWidth(InitGapWidth)
```

### C#

```csharp
System.bool SetInitKnitGapWidth(
   System.double InitGapWidth
)
```

### C++/CLI

```cpp
System.bool SetInitKnitGapWidth(
   System.double InitGapWidth
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InitGapWidth`: Desired knitting gap width for body knitting; valid range is from 1e-8 to 0.1 meters

### Return Value

True if successfully set, false if not

## VBA Syntax

See [Modeler::SetInitKnitGapWidth](ms-its:sldworksapivb6.chm::/sldworks~Modeler~SetInitKnitGapWidth.html).

## Remarks

This initial gap width bound is adjusted during the knitting operation in an attempt to successfully knit a body. Upon completion of the knitting operation, the value is reset to the default value.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::GetInitKnitGapWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetInitKnitGapWidth.html)
