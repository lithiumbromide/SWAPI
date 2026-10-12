---
title: "IsDimXpertFeature Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IsDimXpertFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsDimXpertFeature.html"
---

# IsDimXpertFeature Method (IFeature)

Gets whether this feature is a DimXpert feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDimXpertFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.IsDimXpertFeature()
```

### C#

```csharp
System.bool IsDimXpertFeature()
```

### C++/CLI

```cpp
System.bool IsDimXpertFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a DimXpert feature; false otherwise

## VBA Syntax

See [Feature::IsDimXpertFeature](ms-its:sldworksapivb6.chm::/sldworks~Feature~IsDimXpertFeature.html).

## Examples

[Get DimXpertManager Info (VBA)](Get_DimXpertManager_Info_Example_VB.htm)
[Get DimXpertManager Info (VB.NET)](Get_DimXpertManager_Info_Example_VBNET.htm)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
