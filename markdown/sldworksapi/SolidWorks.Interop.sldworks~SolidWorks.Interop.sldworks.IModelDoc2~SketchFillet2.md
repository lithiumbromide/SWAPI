---
title: "SketchFillet2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchFillet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchFillet2.html"
---

# SketchFillet2 Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateFillet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateFillet.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchFillet2( _
   ByVal Rad As System.Double, _
   ByVal ConstrainedCorners As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Rad As System.Double
Dim ConstrainedCorners As System.Short
Dim value As System.Boolean

value = instance.SketchFillet2(Rad, ConstrainedCorners)
```

### C#

```csharp
System.bool SketchFillet2(
   System.double Rad,
   System.short ConstrainedCorners
)
```

### C++/CLI

```cpp
System.bool SketchFillet2(
   System.double Rad,
   System.short ConstrainedCorners
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Rad`: Radius of the fillet in meters
- `ConstrainedCorners`: Action to take if the corner to be filleted is constrained or has a dimension (see **Remarks**)

### Return Value

True if the fillet is created, false if not

## VBA Syntax

See [ModelDoc2::SketchFillet2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchFillet2.html).

## Remarks

The ConstrainedCorners argument:

- Indicates what action to take if the corner to be filleted is constrained in some manner or has a dimension related to it. In this case, adding a fillet to the corner cannot be done without certain consequences. If the corner is not involved with any constraints, this argument is ignored.
- Can take one of the values found in [swConstrainedCornerAction_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstrainedCornerAction_e.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
