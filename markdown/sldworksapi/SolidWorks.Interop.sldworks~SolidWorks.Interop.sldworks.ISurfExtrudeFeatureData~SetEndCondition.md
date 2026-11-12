---
title: "SetEndCondition Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "SetEndCondition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetEndCondition.html"
---

# SetEndCondition Method (ISurfExtrudeFeatureData)

Sets the end condition of this extruded surface in the forward or reverse direction.

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
Dim instance As ISurfExtrudeFeatureData
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

- `Forward`: True sets the end condition in the forward direction, false sets it in the reverse direction
- `EndCondition`: End condition as defined in [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html)

## VBA Syntax

See [SurfExtrudeFeatureData::SetEndCondition](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~SetEndCondition.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::GetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetEndCondition.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
