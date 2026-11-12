---
title: "CreateLinearSketchStepAndRepeat Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateLinearSketchStepAndRepeat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateLinearSketchStepAndRepeat.html"
---

# CreateLinearSketchStepAndRepeat Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateLinearSketchStepAndRepeat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateLinearSketchStepAndRepeat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateLinearSketchStepAndRepeat( _
   ByVal NumX As System.Integer, _
   ByVal NumY As System.Integer, _
   ByVal SpacingX As System.Double, _
   ByVal SpacingY As System.Double, _
   ByVal AngleX As System.Double, _
   ByVal AngleY As System.Double, _
   ByVal DeleteInstances As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim NumX As System.Integer
Dim NumY As System.Integer
Dim SpacingX As System.Double
Dim SpacingY As System.Double
Dim AngleX As System.Double
Dim AngleY As System.Double
Dim DeleteInstances As System.String
Dim value As System.Boolean

value = instance.CreateLinearSketchStepAndRepeat(NumX, NumY, SpacingX, SpacingY, AngleX, AngleY, DeleteInstances)
```

### C#

```csharp
System.bool CreateLinearSketchStepAndRepeat(
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.string DeleteInstances
)
```

### C++/CLI

```cpp
System.bool CreateLinearSketchStepAndRepeat(
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.String^ DeleteInstances
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumX`:
- `NumY`:
- `SpacingX`:
- `SpacingY`:
- `AngleX`:
- `AngleY`:
- `DeleteInstances`:

## VBA Syntax

See [ModelDoc::CreateLinearSketchStepAndRepeat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateLinearSketchStepAndRepeat.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
