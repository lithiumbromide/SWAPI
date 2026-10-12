---
title: "GetEndConditionReference Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetEndConditionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndConditionReference.html"
---

# GetEndConditionReference Method (IExtrudeFeatureData2)

Gets the reference entity defining the end condition in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndConditionReference( _
   ByVal Forward As System.Boolean, _
   ByRef ReferenceType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim ReferenceType As System.Integer
Dim value As System.Object

value = instance.GetEndConditionReference(Forward, ReferenceType)
```

### C#

```csharp
System.object GetEndConditionReference(
   System.bool Forward,
   out System.int ReferenceType
)
```

### C++/CLI

```cpp
System.Object^ GetEndConditionReference(
   System.bool Forward,
   [Out] System.int ReferenceType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward direction, false for reverse
- `ReferenceType`: Reference type as defined by [swSelectionReferenceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectionReferenceTypes_e.html)

### Return Value

Pointer to the reference entity

## VBA Syntax

See [ExtrudeFeatureData2::GetEndConditionReference](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetEndConditionReference.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::SetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.html)
[IExtrudeFeatureData2::SetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetEndCondition.html)
[IExtrudeFeatureData2::GetEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetEndCondition.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
