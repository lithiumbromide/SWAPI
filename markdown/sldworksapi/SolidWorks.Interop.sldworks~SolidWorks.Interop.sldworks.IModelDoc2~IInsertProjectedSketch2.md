---
title: "IInsertProjectedSketch2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IInsertProjectedSketch2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertProjectedSketch2.html"
---

# IInsertProjectedSketch2 Method (IModelDoc2)

Projects the selected sketch items from the current sketch onto a selected surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertProjectedSketch2( _
   ByVal Reverse As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Reverse As System.Integer
Dim value As Feature

value = instance.IInsertProjectedSketch2(Reverse)
```

### C#

```csharp
Feature IInsertProjectedSketch2(
   System.int Reverse
)
```

### C++/CLI

```cpp
Feature^ IInsertProjectedSketch2(
   System.int Reverse
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Reverse`: 1 to reverse the projected direction

### Return Value

Newly created [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) or NULL if the operation fails

## VBA Syntax

See [ModelDoc2::IInsertProjectedSketch2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IInsertProjectedSketch2.html).

## Remarks

You can reverse the direction in which the curve is projected. This is necessary only when the selected face wraps around the plane of the curve. For example, if the sketch being projected is surrounded by a cylindrical face, then two possible projections exist. The Reverse argument switches the direction based on the normal vector of the sketch. The default direction is along the sketch normal.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertProjectedSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertProjectedSketch.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
