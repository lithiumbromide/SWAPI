---
title: "IMakeManifoldBodies Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IMakeManifoldBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMakeManifoldBodies.html"
---

# IMakeManifoldBodies Method (IModeler)

Creates manifold bodies from the specified non-manifold body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IMakeManifoldBodies( _
   ByVal NonManifoldIn As Body2, _
   ByVal Count As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NonManifoldIn As Body2
Dim Count As System.Integer
Dim value As Body2

value = instance.IMakeManifoldBodies(NonManifoldIn, Count)
```

### C#

```csharp
Body2 IMakeManifoldBodies(
   Body2 NonManifoldIn,
   System.int Count
)
```

### C++/CLI

```cpp
Body2^ IMakeManifoldBodies(
   Body2^ NonManifoldIn,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NonManifoldIn`: Non-manifold [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `Count`: Number of manifold bodies

### Return Value

[Manifold bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::IMakeManifoldBodies](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IMakeManifoldBodies.html).

## Remarks

Call [IModeler::GetManifoldBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~GetManifoldBodiesCount.html) before calling this method to determine the size of the array for that method.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::MakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MakeManifoldBodies.html)
[IModeler::GeneralTopology Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GeneralTopology.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
