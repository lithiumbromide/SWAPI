---
title: "NSamples Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "NSamples"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~NSamples.html"
---

# NSamples Property (IRenderMaterial)

Gets or sets the number of samples used to calculate the contribution of the glossy component for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property NSamples As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.NSamples = value

value = instance.NSamples
```

### C#

```csharp
System.double NSamples {get; set;}
```

### C++/CLI

```cpp
property System.double NSamples {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of samples used to calculate the contribution of the glossy component

## VBA Syntax

See [RenderMaterial::NSamples](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~NSamples.html).

## Remarks

Increasing the sampling rate reduces artifacts but reduces performance. This property is available when the type of material is Satin Finish, Accurate reflections is selected, and Glossy is non-zero.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
