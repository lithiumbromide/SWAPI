---
title: "CreateArcByCenter Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateArcByCenter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArcByCenter.html"
---

# CreateArcByCenter Method (IModelDoc2)

Creates an arc by center in this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateArcByCenter( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double, _
   ByVal P3x As System.Double, _
   ByVal P3y As System.Double, _
   ByVal P3z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1x As System.Double
Dim P1y As System.Double
Dim P1z As System.Double
Dim P2x As System.Double
Dim P2y As System.Double
Dim P2z As System.Double
Dim P3x As System.Double
Dim P3y As System.Double
Dim P3z As System.Double
Dim value As System.Boolean

value = instance.CreateArcByCenter(P1x, P1y, P1z, P2x, P2y, P2z, P3x, P3y, P3z)
```

### C#

```csharp
System.bool CreateArcByCenter(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.double P3x,
   System.double P3y,
   System.double P3z
)
```

### C++/CLI

```cpp
System.bool CreateArcByCenter(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.double P3x,
   System.double P3y,
   System.double P3z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1x`: X coordinate for first point
- `P1y`: Y coordinate for first point
- `P1z`: Z coordinate for first point
- `P2x`: X coordinate for second point
- `P2y`: Y coordinate for second point
- `P2z`: Z coordinate for second point
- `P3x`: X coordinate for third point
- `P3y`: Y coordinate for third point
- `P3z`: Z coordinate for third point

### Return Value

True if successful, false otherwise

## VBA Syntax

See [ModelDoc2::CreateArcByCenter](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateArcByCenter.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::Create3PointArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Create3PointArc.html)
[IModelDoc2::CreateArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArc2.html)
[IModelDoc2::ICreateArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateArc2.html)
[IModelDoc2::CreateTangentArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateTangentArc2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
