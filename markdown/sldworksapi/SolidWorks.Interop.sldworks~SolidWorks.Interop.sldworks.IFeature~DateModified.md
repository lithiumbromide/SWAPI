---
title: "DateModified Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "DateModified"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateModified.html"
---

# DateModified Property (IFeature)

Gets the date on which the feature was last modified.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DateModified As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.String

value = instance.DateModified
```

### C#

```csharp
System.string DateModified {get;}
```

### C++/CLI

```cpp
property System.String^ DateModified {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Date on which the feature was last modified

## VBA Syntax

See [Feature::DateModified](ms-its:sldworksapivb6.chm::/sldworks~Feature~DateModified.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::CreatedBy Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CreatedBy.html)
[IFeature::DateCreated Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DateCreated.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
