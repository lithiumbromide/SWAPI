---
title: "BendDirection Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "BendDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendDirection.html"
---

# BendDirection Property (IOneBendFeatureData)

Gets the direction of this bend.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BendDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Integer

value = instance.BendDirection
```

### C#

```csharp
System.int BendDirection {get;}
```

### C++/CLI

```cpp
property System.int BendDirection {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend direction as defined in [swBendDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendDirection_e.html)

## VBA Syntax

See [OneBendFeatureData::BendDirection](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~BendDirection.html).

## Examples

[Get Direction of a Bend (VBA)](Get_Direction_of_a_Bend_Example_VB.htm)
[Get Direction of a Bend (VB.NET)](Get_Direction_of_a_Bend_Example_VBNET.htm)
[Get Direction of a Bend (C#)](Get_Direction_of_a_Bend_Example_CSharp.htm)

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::BendDown Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendDown.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
