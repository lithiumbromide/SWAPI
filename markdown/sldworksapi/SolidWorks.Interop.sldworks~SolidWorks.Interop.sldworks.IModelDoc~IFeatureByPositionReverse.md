---
title: "IFeatureByPositionReverse Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IFeatureByPositionReverse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IFeatureByPositionReverse.html"
---

# IFeatureByPositionReverse Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IFeatureByPositionReverse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IFeatureByPositionReverse.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureByPositionReverse( _
   ByVal Num As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Num As System.Integer
Dim value As Feature

value = instance.IFeatureByPositionReverse(Num)
```

### C#

```csharp
Feature IFeatureByPositionReverse(
   System.int Num
)
```

### C++/CLI

```cpp
Feature^ IFeatureByPositionReverse(
   System.int Num
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Num`:

## VBA Syntax

See [ModelDoc::IFeatureByPositionReverse](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IFeatureByPositionReverse.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
