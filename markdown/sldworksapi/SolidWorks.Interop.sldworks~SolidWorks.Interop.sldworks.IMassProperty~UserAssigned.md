---
title: "UserAssigned Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "UserAssigned"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~UserAssigned.html"
---

# UserAssigned Property (IMassProperty)

Gets whether the mass property values are user-defined or calculated for this document, regardless of which model is being edited.

## Syntax

### Visual Basic (Declaration)

```vb
Property UserAssigned As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Boolean

instance.UserAssigned = value

value = instance.UserAssigned
```

### C#

```csharp
System.bool UserAssigned {get; set;}
```

### C++/CLI

```cpp
property System.bool UserAssigned {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if mass property values are user-defined, false if calculated

## VBA Syntax

See [MassProperty::UserAssigned](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~UserAssigned.html).

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::ISetAssignedMassProp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetAssignedMassProp.html)
[IMassProperty::SetAssignedMassProp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetAssignedMassProp.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
