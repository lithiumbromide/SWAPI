---
title: "CollectIdenticalBodies Property (ICutListSortOptions)"
project: "SOLIDWORKS API Help"
interface: "ICutListSortOptions"
member: "CollectIdenticalBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~CollectIdenticalBodies.html"
---

# CollectIdenticalBodies Property (ICutListSortOptions)

Gets or sets whether to collect identical bodies into a cut list sub-folder.

## Syntax

### Visual Basic (Declaration)

```vb
Property CollectIdenticalBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICutListSortOptions
Dim value As System.Boolean

instance.CollectIdenticalBodies = value

value = instance.CollectIdenticalBodies
```

### C#

```csharp
System.bool CollectIdenticalBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool CollectIdenticalBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to collect identical bodies, false to not

## VBA Syntax

See [CutListSortOptions::CollectIdenticalBodies](ms-its:sldworksapivb6.chm::/sldworks~CutListSortOptions~CollectIdenticalBodies.html).

## Examples

See the [ICutListSortOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.html) examples.

## Remarks

If set to true, this property puts all bodies that are geometrically identical, but generated in different features, into a cut list item sub-folder in the FeatureManager design tree.

If this is a weldment, identical bodies do not move between weldment sub-folders during the sort.

## See Also

[ICutListSortOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.html)
[ICutListSortOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
