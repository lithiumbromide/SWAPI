---
title: "IGetParents Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetParents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.html"
---

# IGetParents Method (IFeature)

Gets the parent features for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetParents() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As Feature

value = instance.IGetParents()
```

### C#

```csharp
Feature IGetParents()
```

### C++/CLI

```cpp
Feature^ IGetParents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

[Get Parent Features (C++)](Get_Parent_Features_Example_CPlusPlus_COM.htm)

## Remarks

To determine the size of the array, call [IFeature::IGetParentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetParentCount.html) before calling this method.

This method gets only the direct parents of this feature. It does not get parents of parents.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html)
[IFeature::GetOwnerFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetOwnerFeature.html)
[IFeature::GetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.html)
[IFeature::IGetChildCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildCount.html)
[IFeature::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildren.html)

## Availability

SOLIDWORKS 99, datecode 1999207
