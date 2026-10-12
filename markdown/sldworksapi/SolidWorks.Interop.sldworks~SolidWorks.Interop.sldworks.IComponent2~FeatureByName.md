---
title: "FeatureByName Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "FeatureByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FeatureByName.html"
---

# FeatureByName Method (IComponent2)

Gets the specified feature for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureByName( _
   ByVal Name As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Name As System.String
Dim value As Feature

value = instance.FeatureByName(Name)
```

### C#

```csharp
Feature FeatureByName(
   System.string Name
)
```

### C++/CLI

```cpp
Feature^ FeatureByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the feature to retrieve

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [Component2::FeatureByName](ms-its:sldworksapivb6.chm::/sldworks~Component2~FeatureByName.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
