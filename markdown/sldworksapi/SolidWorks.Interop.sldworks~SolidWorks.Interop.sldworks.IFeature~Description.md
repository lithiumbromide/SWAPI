---
title: "Description Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "Description"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Description.html"
---

# Description Property (IFeature)

Gets or sets the description for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Description As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.String

instance.Description = value

value = instance.Description
```

### C#

```csharp
System.string Description {get; set;}
```

### C++/CLI

```cpp
property System.String^ Description {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Feature description

## VBA Syntax

See [Feature::Description](ms-its:sldworksapivb6.chm::/sldworks~Feature~Description.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
