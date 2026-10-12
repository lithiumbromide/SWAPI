---
title: "GetFeatureOwner Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetFeatureOwner"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetFeatureOwner.html"
---

# GetFeatureOwner Method (IDimension)

Gets the feature for this dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureOwner() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As Feature

value = instance.GetFeatureOwner()
```

### C#

```csharp
Feature GetFeatureOwner()
```

### C++/CLI

```cpp
Feature^ GetFeatureOwner();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object for this dimension

## VBA Syntax

See [Dimension::GetFeatureOwner](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetFeatureOwner.html).

## Examples

[Get Component Via Display Dimension (VBA)](Get_Component_Via_Display_Dimension_Example_VB.htm)

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
