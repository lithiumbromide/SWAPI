---
title: "CreateCircularSketchStepAndRepeat Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateCircularSketchStepAndRepeat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCircularSketchStepAndRepeat.html"
---

# CreateCircularSketchStepAndRepeat Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateCircularSketchStepAndRepeat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCircularSketchStepAndRepeat.html).

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
Dim instance As IModelDoc
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

- `ArcRadius`:
- `ArcAngle`:
- `PatternNum`:
- `PatternSpacing`:
- `PatternRotate`:
- `DeleteInstances`:

## VBA Syntax

See [ModelDoc::CreateCircularSketchStepAndRepeat](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateCircularSketchStepAndRepeat.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
