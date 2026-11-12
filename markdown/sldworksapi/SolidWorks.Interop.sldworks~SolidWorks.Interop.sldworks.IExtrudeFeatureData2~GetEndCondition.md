---
title: "GetEndCondition Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetEndCondition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.html"
---

# GetEndCondition Method (IExtrudeFeatureData2)

Gets the type of end condition of this extrusion feature for forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndCondition( _
   ByVal Forward As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
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

- `Forward`: True for forward direction, false for reverse

### Return Value

End condition type as defined in [swEndConditions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

## VBA Syntax

See [ExtrudeFeatureData2::GetEndCondition](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetEndCondition.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.html)
[IExtrudeFeatureData2::SetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition.html)
[IExtrudeFeatureData2::SetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
