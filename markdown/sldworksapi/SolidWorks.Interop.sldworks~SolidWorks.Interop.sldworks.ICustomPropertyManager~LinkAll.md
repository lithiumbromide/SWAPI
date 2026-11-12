---
title: "LinkAll Property (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "LinkAll"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkAll.html"
---

# LinkAll Property (ICustomPropertyManager)

Gets or sets whether to link or unlink all custom properties to or from their parent parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkAll As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim value As System.Boolean

instance.LinkAll = value

value = instance.LinkAll
```

### C#

```csharp
System.bool LinkAll {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkAll {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to link all custom properties, false to unlink all

## VBA Syntax

See [CustomPropertyManager::LinkAll](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~LinkAll.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::LinkProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkProperty.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
