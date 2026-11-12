---
title: "SketchRectangleAtAnyAngle Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchRectangleAtAnyAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchRectangleAtAnyAngle.html"
---

# SketchRectangleAtAnyAngle Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchRectangleAtAnyAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchRectangleAtAnyAngle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchRectangleAtAnyAngle( _
   ByVal Val1 As System.Double, _
   ByVal Val2 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal Val3 As System.Double, _
   ByVal Val4 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal Val3x As System.Double, _
   ByVal Val3y As System.Double, _
   ByVal Z3 As System.Double, _
   ByVal Val5 As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Val1 As System.Double
Dim Val2 As System.Double
Dim Z1 As System.Double
Dim Val3 As System.Double
Dim Val4 As System.Double
Dim Z2 As System.Double
Dim Val3x As System.Double
Dim Val3y As System.Double
Dim Z3 As System.Double
Dim Val5 As System.Boolean

instance.SketchRectangleAtAnyAngle(Val1, Val2, Z1, Val3, Val4, Z2, Val3x, Val3y, Z3, Val5)
```

### C#

```csharp
void SketchRectangleAtAnyAngle(
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.double Val3x,
   System.double Val3y,
   System.double Z3,
   System.bool Val5
)
```

### C++/CLI

```cpp
void SketchRectangleAtAnyAngle(
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.double Val3x,
   System.double Val3y,
   System.double Z3,
   System.bool Val5
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val1`:
- `Val2`:
- `Z1`:
- `Val3`:
- `Val4`:
- `Z2`:
- `Val3x`:
- `Val3y`:
- `Z3`:
- `Val5`:

## VBA Syntax

See [ModelDoc::SketchRectangleAtAnyAngle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchRectangleAtAnyAngle.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
