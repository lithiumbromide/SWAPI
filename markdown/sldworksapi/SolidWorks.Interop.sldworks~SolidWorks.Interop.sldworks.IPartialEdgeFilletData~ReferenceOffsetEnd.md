---
title: "ReferenceOffsetEnd Property (IPartialEdgeFilletData)"
project: "SOLIDWORKS API Help"
interface: "IPartialEdgeFilletData"
member: "ReferenceOffsetEnd"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetEnd.html"
---

# ReferenceOffsetEnd Property (IPartialEdgeFilletData)

Gets the offset reference for the end condition for this partial edge fillet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceOffsetEnd As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartialEdgeFilletData
Dim value As System.Object

value = instance.ReferenceOffsetEnd
```

### C#

```csharp
System.object ReferenceOffsetEnd {get;}
```

### C++/CLI

```cpp
property System.Object^ ReferenceOffsetEnd {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset reference (2D/3D sketch [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html), reference [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html))

## VBA Syntax

See [PartialEdgeFilletData::ReferenceOffsetEnd](ms-its:sldworksapivb6.chm::/sldworks~PartialEdgeFilletData~ReferenceOffsetEnd.html).

## Remarks

This property is valid only if [IPartialEdgeFilletData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~EndCondition.html) is swSimpleFilletPartialEdgeCondition_e.PartialEdgeReferenceOffset.

Use [IPartialEdgeFilletData::ReferenceOffsetEndType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetEndType.html) to get the type of object returned by this property.

To modify the reference offset for the end condition of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.html).

## See Also

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
