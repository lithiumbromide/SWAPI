---
title: "IsDimXpertAnnotation Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IsDimXpertAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsDimXpertAnnotation.html"
---

# IsDimXpertAnnotation Method (IFeature)

Gets whether this feature is a DimXpert annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDimXpertAnnotation() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.IsDimXpertAnnotation()
```

### C#

```csharp
System.bool IsDimXpertAnnotation()
```

### C++/CLI

```cpp
System.bool IsDimXpertAnnotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a DimXpert annotation; false otherwise

## VBA Syntax

See [Feature::IsDimXpertAnnotation](ms-its:sldworksapivb6.chm::/sldworks~Feature~IsDimXpertAnnotation.html).

## Examples

[Get DimXpertManager Info (VBA)](Get_DimXpertManager_Info_Example_VB.htm)
[Get DimXpertManager Info (VB.NET)](Get_DimXpertManager_Info_Example_VBNET.htm)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
