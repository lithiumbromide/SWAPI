---
title: "IncompatibleObject Property (IVersionCompatibilityItem)"
project: "SOLIDWORKS API Help"
interface: "IVersionCompatibilityItem"
member: "IncompatibleObject"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem~IncompatibleObject.html"
---

# IncompatibleObject Property (IVersionCompatibilityItem)

Get the object incompatible with the specified file format version.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IncompatibleObject As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IVersionCompatibilityItem
Dim value As System.Object

value = instance.IncompatibleObject
```

### C#

```csharp
System.object IncompatibleObject {get;}
```

### C++/CLI

```cpp
property System.Object^ IncompatibleObject {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [VersionCompatibilityItem::IncompatibleObject](ms-its:sldworksapivb6.chm::/sldworks~VersionCompatibilityItem~IncompatibleObject.html).

## Remarks

The incompatible object is typically a [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html).

## See Also

[IVersionCompatibilityItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem.html)
[IVersionCompatibilityItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVersionCompatibilityItem_members.html)

## Availability

SOLIDWORKS 2026 SP03, Revision Number 34.3
