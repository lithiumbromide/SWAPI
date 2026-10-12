---
title: "GeneralTopology Property (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "GeneralTopology"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GeneralTopology.html"
---

# GeneralTopology Property (IModeler)

Gets or sets the Parasolid option to create general (non-manifold) bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property GeneralTopology As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim value As System.Boolean

instance.GeneralTopology = value

value = instance.GeneralTopology
```

### C#

```csharp
System.bool GeneralTopology {get; set;}
```

### C++/CLI

```cpp
property System.bool GeneralTopology {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to create general bodies, false to not

## VBA Syntax

See [Modeler::GeneralTopology](ms-its:sldworksapivb6.chm::/sldworks~Modeler~GeneralTopology.html).

## Examples

[Create and Convert Non-manifold Bodies (C#)](Create_and_Convert_Non-manifold_Bodies_Example_CSharp.htm)
[Create and Convert Non-manifold Bodies (VB.NET)](Create_and_Convert_Non-manifold_Bodies_Example_VBNET.htm)
[Create and Convert Non-manifold Bodies (VBA)](Create_and_Convert_Non-manifold_Bodies_Example_VB.htm)

## Remarks

SOLIDWORKS expects this property be false because SOLIDWORKS does not support the creation of general bodies. If you set this property to True, then set it back to false as soon as your intended operations complete.

To tessellate a general body, set [ITesssellation::MatchType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~MatchType.html) to swTesselationMatchFacetGeometry, which sets the Parasolid facet match to clipping facet boundaries to a common edge

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::GetManifoldBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetManifoldBodiesCount.html)
[IModeler::IMakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMakeManifoldBodies.html)
[IModeler::MakeManifoldBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MakeManifoldBodies.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
