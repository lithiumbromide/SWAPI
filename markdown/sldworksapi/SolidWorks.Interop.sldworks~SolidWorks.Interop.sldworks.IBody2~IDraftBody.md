---
title: "IDraftBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDraftBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDraftBody.html"
---

# IDraftBody Method (IBody2)

Obsolete. Superseded by [IBody2::IDraftBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDraftBody2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IDraftBody( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face2, _
   ByRef EdgeList As Edge, _
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
Dim DraftAngle As System.Double
Dim Dir As System.Double
Dim value As System.Boolean

value = instance.IDraftBody(NumOfFaces, FaceList, EdgeList, DraftAngle, Dir)
```

### C#

```csharp
System.bool IDraftBody(
   System.int NumOfFaces,
   ref Face2 FaceList,
   ref Edge EdgeList,
   System.double DraftAngle,
   ref System.double Dir
)
```

### C++/CLI

```cpp
System.bool IDraftBody(
   System.int NumOfFaces,
   Face2^% FaceList,
   Edge^% EdgeList,
   System.double DraftAngle,
   System.double% Dir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:
- `EdgeList`:
- `DraftAngle`:
- `Dir`:

## VBA Syntax

See [Body2::IDraftBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~IDraftBody.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
