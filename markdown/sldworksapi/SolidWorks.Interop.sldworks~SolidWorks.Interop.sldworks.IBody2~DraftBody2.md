---
title: "DraftBody2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DraftBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DraftBody2.html"
---

# DraftBody2 Method (IBody2)

Adds drafts to the specified faces on a temporary body. This method modifies the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function DraftBody2( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object, _
   ByVal EdgeList As System.Object, _
   ByVal BasePoint As System.Object, _
   ByVal DraftAngle As System.Double, _
   ByVal Dir As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim EdgeList As System.Object
Dim BasePoint As System.Object
Dim DraftAngle As System.Double
Dim Dir As System.Object
Dim value As System.Boolean

value = instance.DraftBody2(NumOfFaces, FaceList, EdgeList, BasePoint, DraftAngle, Dir)
```

### C#

```csharp
System.bool DraftBody2(
   System.int NumOfFaces,
   System.object FaceList,
   System.object EdgeList,
   System.object BasePoint,
   System.double DraftAngle,
   System.object Dir
)
```

### C++/CLI

```cpp
System.bool DraftBody2(
   System.int NumOfFaces,
   System.Object^ FaceList,
   System.Object^ EdgeList,
   System.Object^ BasePoint,
   System.double DraftAngle,
   System.Object^ Dir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces to draft
- `FaceList`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to draft
- `EdgeList`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), one for each face, along which to apply the drafts
- `BasePoint`: Pointer to a [MathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object (x,y,z values of the base point)
- `DraftAngle`: Draft angle
- `Dir`: Array of 3 doubles (x, y, z), a vector which specifies the direction of the draft

### Return Value

True if drafts are applied, false if not

## VBA Syntax

See [Body2::DraftBody2](ms-its:sldworksapivb6.chm::/sldworks~Body2~DraftBody2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IDraftBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDraftBody2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
