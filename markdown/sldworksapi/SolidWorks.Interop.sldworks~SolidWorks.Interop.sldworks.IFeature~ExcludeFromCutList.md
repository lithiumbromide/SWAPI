---
title: "ExcludeFromCutList Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "ExcludeFromCutList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ExcludeFromCutList.html"
---

# ExcludeFromCutList Property (IFeature)

Gets or sets whether to exclude this feature from the cut list.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExcludeFromCutList As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

instance.ExcludeFromCutList = value

value = instance.ExcludeFromCutList
```

### C#

```csharp
System.bool ExcludeFromCutList {get; set;}
```

### C++/CLI

```cpp
property System.bool ExcludeFromCutList {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to exclude, false to not

## VBA Syntax

See [Feature::ExcludeFromCutList](ms-its:sldworksapivb6.chm::/sldworks~Feature~ExcludeFromCutList.html).

## Remarks

This method only works for cut list items.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
