---
title: "SetEndCondition Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetEndCondition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition.html"
---

# SetEndCondition Method (IExtrudeFeatureData2)

Sets the end condition type of the extrusion feature for the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEndCondition( _
   ByVal Forward As System.Boolean, _
   ByVal EndCondition As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim EndCondition As System.Integer

instance.SetEndCondition(Forward, EndCondition)
```

### C#

```csharp
void SetEndCondition(
   System.bool Forward,
   System.int EndCondition
)
```

### C++/CLI

```cpp
void SetEndCondition(
   System.bool Forward,
   System.int EndCondition
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward direction, false for reverse
- `EndCondition`: End condition type as defined in [swEndConditions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

## VBA Syntax

See [ExtrudeFeatureData2::SetEndCondition](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetEndCondition.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::SetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.html)
[IExtrudeFeatureData2::GetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.html)
[IExtrudeFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.html)
[IExtrudeFeatureData2::SetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDepth.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
