---
title: "GetEndCondition Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "GetEndCondition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetEndCondition.html"
---

# GetEndCondition Method (ISurfExtrudeFeatureData)

Gets the end condition of this extruded surface for the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndCondition( _
   ByVal Forward As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As System.Integer

value = instance.GetEndCondition(Forward)
```

### C#

```csharp
System.int GetEndCondition(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.int GetEndCondition(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True gets the end condition in the forward direction, false gets it in the reverse direction

### Return Value

End condition as defined in [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html)

## VBA Syntax

See [SurfExtrudeFeatureData::GetEndCondition](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~GetEndCondition.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::SetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetEndCondition.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
