---
title: "InsertHelix Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertHelix"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertHelix.html"
---

# InsertHelix Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertHelix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertHelix.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertHelix( _
   ByVal Reversed As System.Boolean, _
   ByVal Clockwised As System.Boolean, _
   ByVal Tapered As System.Boolean, _
   ByVal Outward As System.Boolean, _
   ByVal Helixdef As System.Integer, _
   ByVal Height As System.Double, _
   ByVal Pitch As System.Double, _
   ByVal Revolution As System.Double, _
   ByVal TaperAngle As System.Double, _
   ByVal Startangle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Reversed As System.Boolean
Dim Clockwised As System.Boolean
Dim Tapered As System.Boolean
Dim Outward As System.Boolean
Dim Helixdef As System.Integer
Dim Height As System.Double
Dim Pitch As System.Double
Dim Revolution As System.Double
Dim TaperAngle As System.Double
Dim Startangle As System.Double

instance.InsertHelix(Reversed, Clockwised, Tapered, Outward, Helixdef, Height, Pitch, Revolution, TaperAngle, Startangle)
```

### C#

```csharp
void InsertHelix(
   System.bool Reversed,
   System.bool Clockwised,
   System.bool Tapered,
   System.bool Outward,
   System.int Helixdef,
   System.double Height,
   System.double Pitch,
   System.double Revolution,
   System.double TaperAngle,
   System.double Startangle
)
```

### C++/CLI

```cpp
void InsertHelix(
   System.bool Reversed,
   System.bool Clockwised,
   System.bool Tapered,
   System.bool Outward,
   System.int Helixdef,
   System.double Height,
   System.double Pitch,
   System.double Revolution,
   System.double TaperAngle,
   System.double Startangle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Reversed`:
- `Clockwised`:
- `Tapered`:
- `Outward`:
- `Helixdef`:
- `Height`:
- `Pitch`:
- `Revolution`:
- `TaperAngle`:
- `Startangle`:

## VBA Syntax

See [ModelDoc::InsertHelix](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertHelix.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
