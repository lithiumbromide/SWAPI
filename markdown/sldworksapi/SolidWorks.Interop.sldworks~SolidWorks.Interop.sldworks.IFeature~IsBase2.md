---
title: "IsBase2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IsBase2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsBase2.html"
---

# IsBase2 Method (IFeature)

Gets whether this feature is a base feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBase2() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.IsBase2()
```

### C#

```csharp
System.bool IsBase2()
```

### C++/CLI

```cpp
System.bool IsBase2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this is a base feature, false if not

## VBA Syntax

See [Feature::IsBase2](ms-its:sldworksapivb6.chm::/sldworks~Feature~IsBase2.html).

## Remarks

Any feature that creates a solid body is a base feature. For example:

- An extrude operation creates a solid body; therefore, that feature is a base feature.
- A body imported via an IGES file is a base feature.

However, a fillet operation does not create a solid body; therefore, that feature is not a base feature.

In a multibody environment, more than one feature can return true. Thus, a lot of features can be base features in a multibody environment.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::ISetBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody3.html)
[IFeature::SetBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBody2.html)

## Availability

SOLIDWORKS 2003 SP3, Revision Number 11.3
