---
title: "DisplaySurfaceBodies Property (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "DisplaySurfaceBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~DisplaySurfaceBodies.html"
---

# DisplaySurfaceBodies Property (IDrSection)

Gets or sets whether to display surface bodies in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplaySurfaceBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

instance.DisplaySurfaceBodies = value

value = instance.DisplaySurfaceBodies
```

### C#

```csharp
System.bool DisplaySurfaceBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool DisplaySurfaceBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display surface bodies, false to not

## VBA Syntax

See [DrSection::DisplaySurfaceBodies](ms-its:sldworksapivb6.chm::/sldworks~DrSection~DisplaySurfaceBodies.html).

## Examples

See the [IDrSection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) examples.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
