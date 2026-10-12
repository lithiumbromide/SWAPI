---
title: "RepresentationShared Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "RepresentationShared"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RepresentationShared.html"
---

# RepresentationShared Property (IConfiguration)

Gets or sets whether this [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) Representation configuration is shared.

## Syntax

### Visual Basic (Declaration)

```vb
Property RepresentationShared As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.RepresentationShared = value

value = instance.RepresentationShared
```

### C#

```csharp
System.bool RepresentationShared {get; set;}
```

### C++/CLI

```cpp
property System.bool RepresentationShared {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this Representation configuration is shared, false if not

## VBA Syntax

See [Configuration::RepresentationShared](ms-its:sldworksapivb6.chm::/sldworks~Configuration~RepresentationShared.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
