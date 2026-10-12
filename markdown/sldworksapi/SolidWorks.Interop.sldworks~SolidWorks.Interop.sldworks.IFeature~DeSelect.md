---
title: "DeSelect Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DeSelect.html"
---

# DeSelect Method (IFeature)

Deselects this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.DeSelect()
```

### C#

```csharp
System.bool DeSelect()
```

### C++/CLI

```cpp
System.bool DeSelect();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the feature is deselected successfully, false if not

## VBA Syntax

See [Feature::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~Feature~DeSelect.html).

## Examples

[Get Section Properties for Faces from Section Planes (VBA)](Get_Section_Properties_Example_VB.htm)

## Remarks

Use [IModelDoc2::DeSelectByID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeSelectByID.html) instead of this method. This method does not work well when a PropertyManager page is open or a command is running. IModelDoc2::DeSelectByID handles selection correctly whether or not a command is running.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::Select2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.html)
[IFeature::GetSpecificFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
