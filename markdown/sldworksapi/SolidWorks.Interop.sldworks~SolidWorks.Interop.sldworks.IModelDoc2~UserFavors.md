---
title: "UserFavors Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "UserFavors"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UserFavors.html"
---

# UserFavors Method (IModelDoc2)

Specifies whether geometric relations are automatically created as you add sketch entities.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UserFavors()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.UserFavors()
```

### C#

```csharp
void UserFavors()
```

### C++/CLI

```cpp
void UserFavors();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::UserFavors](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~UserFavors.html).

## Remarks

If this option is on, then the cursor changes shape as you sketch to show you which relations can be created: horizontal, vertical, parallel, perpendicular, tangent, midpoint, or coincident.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, RevisionNumber 10.0
