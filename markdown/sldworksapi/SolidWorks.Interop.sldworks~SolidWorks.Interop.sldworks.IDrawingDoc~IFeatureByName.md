---
title: "IFeatureByName Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IFeatureByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IFeatureByName.html"
---

# IFeatureByName Method (IDrawingDoc)

Gets the specified feature in the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureByName( _
   ByVal Name As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Name As System.String
Dim value As Feature

value = instance.IFeatureByName(Name)
```

### C#

```csharp
Feature IFeatureByName(
   System.string Name
)
```

### C++/CLI

```cpp
Feature^ IFeatureByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the feature

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [DrawingDoc::IFeatureByName](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IFeatureByName.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~FeatureByName.html)
