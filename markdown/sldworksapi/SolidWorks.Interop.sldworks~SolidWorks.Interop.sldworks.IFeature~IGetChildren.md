---
title: "IGetChildren Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetChildren"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildren.html"
---

# IGetChildren Method (IFeature)

Gets the child features belonging to this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetChildren() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As Feature

value = instance.IGetChildren()
```

### C#

```csharp
Feature IGetChildren()
```

### C++/CLI

```cpp
Feature^ IGetChildren();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method gets the direct children of this feature. It does not get children of children.

To determine the size of the array, call [IFeature::IGetChildCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetChildCount.html) before calling this method.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html)
[IFeature::GetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.html)
[IFeature::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.html)
[IFeature::IGetParentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParentCount.html)

## Availability

SOLIDWORKS 99, datecode 1999207
