---
title: "IDraftBody2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDraftBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDraftBody2.html"
---

# IDraftBody2 Method (IBody2)

Adds drafts to the specified faces on a temporary body. This method modifies the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IDraftBody2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face2, _
   ByRef EdgeList As Edge, _
   ByVal BasePoint As MathPoint, _
   ByVal DraftAngle As System.Double, _
   ByRef Dir As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As Face2
Dim EdgeList As Edge
Dim BasePoint As MathPoint
Dim DraftAngle As System.Double
Dim Dir As System.Double
Dim value As System.Boolean

value = instance.IDraftBody2(NumOfFaces, FaceList, EdgeList, BasePoint, DraftAngle, Dir)
```

### C#

```csharp
System.bool IDraftBody2(
   System.int NumOfFaces,
   ref Face2 FaceList,
   ref Edge EdgeList,
   MathPoint BasePoint,
   System.double DraftAngle,
   ref System.double Dir
)
```

### C++/CLI

```cpp
System.bool IDraftBody2(
   System.int NumOfFaces,
   Face2^% FaceList,
   Edge^% EdgeList,
   MathPoint^ BasePoint,
   System.double DraftAngle,
   System.double% Dir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces to draft
- `FaceList`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to draft
- `EdgeList`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), one for each face, along which to apply the drafts
- `BasePoint`: Pointer to a [MathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object (x,y,z values of the base point)
- `DraftAngle`: Draft angle
- `Dir`: Array of 3 doubles (x, y, z), a vector which specifies the direction
  of the draft

### Return Value

True if drafts are applied, false if not

## VBA Syntax

See [Body2::IDraftBody2](ms-its:sldworksapivb6.chm::/sldworks~Body2~IDraftBody2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::DraftBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DraftBody2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
