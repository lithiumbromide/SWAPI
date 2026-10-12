---
title: "DateCreated Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "DateCreated"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateCreated.html"
---

# DateCreated Property (IFeature)

Gets the date on which the feature was created.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DateCreated As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.String

value = instance.DateCreated
```

### C#

```csharp
System.string DateCreated {get;}
```

### C++/CLI

```cpp
property System.String^ DateCreated {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Date on which the feature was created

## VBA Syntax

See [Feature::DateCreated](ms-its:sldworksapivb6.chm::/sldworks~Feature~DateCreated.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature:CreatedBy Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CreatedBy.html)
[IFeature::DateModified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateModified.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
