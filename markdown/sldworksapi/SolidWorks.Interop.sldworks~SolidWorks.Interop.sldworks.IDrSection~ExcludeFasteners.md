---
title: "ExcludeFasteners Property (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "ExcludeFasteners"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ExcludeFasteners.html"
---

# ExcludeFasteners Property (IDrSection)

Gets or sets whether to exclude fasteners in the section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExcludeFasteners As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

instance.ExcludeFasteners = value

value = instance.ExcludeFasteners
```

### C#

```csharp
System.bool ExcludeFasteners {get; set;}
```

### C++/CLI

```cpp
property System.bool ExcludeFasteners {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to exclude fasteners, false to include them

## VBA Syntax

See [DrSection::ExcludeFasteners](ms-its:sldworksapivb6.chm::/sldworks~DrSection~ExcludeFasteners.html).

## Remarks

Call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) after calling this property.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
