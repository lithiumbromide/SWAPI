---
title: "MakeManifoldBodies Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "MakeManifoldBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MakeManifoldBodies.html"
---

# MakeManifoldBodies Method (IModeler)

Creates manifold bodies from the specified non-manifold body.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeManifoldBodies( _
   ByVal NonManifoldIn As Body2 _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NonManifoldIn As Body2
Dim value As System.Object

value = instance.MakeManifoldBodies(NonManifoldIn)
```

### C#

```csharp
System.object MakeManifoldBodies(
   Body2 NonManifoldIn
)
```

### C++/CLI

```cpp
System.Object^ MakeManifoldBodies(
   Body2^ NonManifoldIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NonManifoldIn`: Non-manifold [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

### Return Value

[Manifold bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::MakeManifoldBodies](ms-its:sldworksapivb6.chm::/sldworks~Modeler~MakeManifoldBodies.html).

## Examples

[Create and Convert Non-manifold Bodies (C#)](Create_and_Convert_Non-manifold_Bodies_Example_CSharp.htm)
[Create and Convert Non-manifold Bodies (VB.NET)](Create_and_Convert_Non-manifold_Bodies_Example_VBNET.htm)
[Create and Convert Non-manifold Bodies (VBA)](Create_and_Convert_Non-manifold_Bodies_Example_VB.htm)

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::IMakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMakeManifoldBodies.html)
[IModeler::GeneralTopology Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GeneralTopology.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
