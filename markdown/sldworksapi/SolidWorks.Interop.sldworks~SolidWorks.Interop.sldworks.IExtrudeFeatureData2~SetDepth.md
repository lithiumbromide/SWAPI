---
title: "SetDepth Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetDepth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDepth.html"
---

# SetDepth Method (IExtrudeFeatureData2)

Sets the depth of the feature in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDepth( _
   ByVal Forward As System.Boolean, _
   ByVal Depth As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim Depth As System.Double

instance.SetDepth(Forward, Depth)
```

### C#

```csharp
void SetDepth(
   System.bool Forward,
   System.double Depth
)
```

### C++/CLI

```cpp
void SetDepth(
   System.bool Forward,
   System.double Depth
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward direction, false for reverse
- `Depth`: Depth of the extrusion

## VBA Syntax

See [ExtrudeFeatureData2::SetDepth](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetDepth.html).

## Examples

[Access Selections (VBA)](Access_Selections_Example_VB.htm)

## Remarks

Use this method to specify the surface offset distance when [end condition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.html) is swEndCondOffsetFromSurface.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDepth.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
