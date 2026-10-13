---
title: "CreateCircularSketchStepAndRepeat Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateCircularSketchStepAndRepeat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCircularSketchStepAndRepeat.html"
---

# CreateCircularSketchStepAndRepeat Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateCircularSketchStepAndRepeat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateCircularSketchStepAndRepeat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCircularSketchStepAndRepeat( _
   ByVal ArcRadius As System.Double, _
   ByVal ArcAngle As System.Double, _
   ByVal PatternNum As System.Integer, _
   ByVal PatternSpacing As System.Double, _
   ByVal PatternRotate As System.Boolean, _
   ByVal DeleteInstances As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ArcRadius As System.Double
Dim ArcAngle As System.Double
Dim PatternNum As System.Integer
Dim PatternSpacing As System.Double
Dim PatternRotate As System.Boolean
Dim DeleteInstances As System.String
Dim value As System.Boolean

value = instance.CreateCircularSketchStepAndRepeat(ArcRadius, ArcAngle, PatternNum, PatternSpacing, PatternRotate, DeleteInstances)
```

### C#

```csharp
System.bool CreateCircularSketchStepAndRepeat(
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.string DeleteInstances
)
```

### C++/CLI

```cpp
System.bool CreateCircularSketchStepAndRepeat(
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.String^ DeleteInstances
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArcRadius`: Radius to be used in the circular sketch pattern
- `ArcAngle`: Angle relative to the sketch entities being patterned
- `PatternNum`: Total number of instances, including the seed geometry
- `PatternSpacing`: Spacing between pattern instances in radians
- `PatternRotate`: True to rotate the pattern, false to not
- `DeleteInstances`: Number of instances to delete passed as a string formatted as: "(a) (b) (c) "

### Return Value

True if the sketch pattern was created successfully, false otherwise

## VBA Syntax

See [ModelDoc2::CreateCircularSketchStepAndRepeat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateCircularSketchStepAndRepeat.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreateLinearSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateLinearSketchStepAndRepeat.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
