---
title: "DraftBody Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "DraftBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~DraftBody.html"
---

# DraftBody Method (IBody)

Obsolete. Superseded by [IBody2::DraftBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~DraftBody2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DraftBody( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object, _
   ByVal EdgeList As System.Object, _
   ByVal DraftAngle As System.Double, _
   ByVal Dir As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim EdgeList As System.Object
Dim DraftAngle As System.Double
Dim Dir As System.Object
Dim value As System.Boolean

value = instance.DraftBody(NumOfFaces, FaceList, EdgeList, DraftAngle, Dir)
```

### C#

```csharp
System.bool DraftBody(
   System.int NumOfFaces,
   System.object FaceList,
   System.object EdgeList,
   System.double DraftAngle,
   System.object Dir
)
```

### C++/CLI

```cpp
System.bool DraftBody(
   System.int NumOfFaces,
   System.Object^ FaceList,
   System.Object^ EdgeList,
   System.double DraftAngle,
   System.Object^ Dir
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

See [Body::DraftBody](ms-its:sldworksapivb6.chm::/sldworks~Body~DraftBody.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
