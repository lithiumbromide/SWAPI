---
title: "CreateLinearSketchStepAndRepeat Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateLinearSketchStepAndRepeat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateLinearSketchStepAndRepeat.html"
---

# CreateLinearSketchStepAndRepeat Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateLinearSketchStepAndRepeat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateLinearSketchStepAndRepeat.html).

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
Dim instance As IModelDoc2
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

- `NumX`: Total number of instances along direction 1, including the seed
- `NumY`: Total number of instances along direction 2, including the seed
- `SpacingX`: Spacing between instances along direction 1
- `SpacingY`: Spacing between instances along direction 2
- `AngleX`: Relative to the X axis, the angle for direction 1
- `AngleY`: Relative to the X axis, the angle for direction 2
- `DeleteInstances`: Number of instances to delete passed as a string in the format: "(a) (b) (c) "

### Return Value

True if the sketch pattern was created successfully, false otherwise

## VBA Syntax

See [ModelDoc2::CreateLinearSketchStepAndRepeat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateLinearSketchStepAndRepeat.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreateCircularSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCircularSketchStepAndRepeat.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
