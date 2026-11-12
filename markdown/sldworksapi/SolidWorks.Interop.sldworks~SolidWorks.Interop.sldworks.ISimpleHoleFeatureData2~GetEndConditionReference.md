---
title: "GetEndConditionReference Method (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "GetEndConditionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetEndConditionReference.html"
---

# GetEndConditionReference Method (ISimpleHoleFeatureData2)

Gets the reference entity that defines the end condition for this simple hole feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndConditionReference( _
   ByRef ReferenceType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim ReferenceType As System.Integer
Dim value As System.Object

value = instance.GetEndConditionReference(ReferenceType)
```

### C#

```csharp
System.object GetEndConditionReference(
   out System.int ReferenceType
)
```

### C++/CLI

```cpp
System.Object^ GetEndConditionReference(
   [Out] System.int ReferenceType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ReferenceType`: Reference type as defined in [swSelectionReferenceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectionReferenceTypes_e.html)

### Return Value

Reference entity

## VBA Syntax

See [SimpleHoleFeatureData2::GetEndConditionReference](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~GetEndConditionReference.html).

## Examples

See [ISimpleHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::SetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SetEndConditionReference.html)
[ISimpleHoleFeatureData2::Face Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Face.html)
[ISimpleHoleFeatureData2::IFace Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IFace.html)
[ISimpleHoleFeatureData2::IVertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IVertex.html)
[ISimpleHoleFeatureData2::Vertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Vertex.html)
[ISimpleHoleFeatureData2::Type Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Type.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
