---
title: "SetEndConditionReference Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetEndConditionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.html"
---

# SetEndConditionReference Method (IExtrudeFeatureData2)

Sets the reference entity that defines the end condition in a forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEndConditionReference( _
   ByVal Forward As System.Boolean, _
   ByVal PDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim PDisp As System.Object

instance.SetEndConditionReference(Forward, PDisp)
```

### C#

```csharp
void SetEndConditionReference(
   System.bool Forward,
   System.object PDisp
)
```

### C++/CLI

```cpp
void SetEndConditionReference(
   System.bool Forward,
   System.Object^ PDisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward direction, false for reverse
- `PDisp`: Pointer to the reference entity

## VBA Syntax

See [ExtrudeFeatureData2::SetEndConditionReference](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetEndConditionReference.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.html)
[IExtrudeFeatureData2::GetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.html)
[IExtrudeFeatureData2::SetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
