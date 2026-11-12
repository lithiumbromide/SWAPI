---
title: "GetManifoldBodiesCount Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "GetManifoldBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetManifoldBodiesCount.html"
---

# GetManifoldBodiesCount Method (IModeler)

Gets the number of manifold bodies created from the specified non-manifold body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetManifoldBodiesCount( _
   ByVal NonManifoldIn As Body2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NonManifoldIn As Body2
Dim value As System.Integer

value = instance.GetManifoldBodiesCount(NonManifoldIn)
```

### C#

```csharp
System.int GetManifoldBodiesCount(
   Body2 NonManifoldIn
)
```

### C++/CLI

```cpp
System.int GetManifoldBodiesCount(
   Body2^ NonManifoldIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NonManifoldIn`: Non-manifold [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

### Return Value

Number of manifold bodies

## VBA Syntax

See [Modeler::GetManifoldBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~Modeler~GetManifoldBodiesCount.html).

## Remarks

Call this method before calling [IModeler::IMakeManifoldBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~IMakeManifoldBodies.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::GeneralTopology Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GeneralTopology.html)
[IModeler::MakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MakeManifoldBodies.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
