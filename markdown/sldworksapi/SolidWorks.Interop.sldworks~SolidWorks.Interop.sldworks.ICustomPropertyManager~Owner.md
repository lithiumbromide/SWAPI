---
title: "Owner Property (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Owner"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Owner.html"
---

# Owner Property (ICustomPropertyManager)

Gets the owner of this custom property.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Owner As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim value As System.Object

value = instance.Owner
```

### C#

```csharp
System.object Owner {get;}
```

### C++/CLI

```cpp
property System.Object^ Owner {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to owner of the custom property; currently either a [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) or a [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [CustomPropertyManager::Owner](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Owner.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
