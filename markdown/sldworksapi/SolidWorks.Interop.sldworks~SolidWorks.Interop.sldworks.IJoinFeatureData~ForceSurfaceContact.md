---
title: "ForceSurfaceContact Property (IJoinFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJoinFeatureData"
member: "ForceSurfaceContact"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ForceSurfaceContact.html"
---

# ForceSurfaceContact Property (IJoinFeatureData)

Gets or sets whether to join any coincident faces and any intruding volumes.

## Syntax

### Visual Basic (Declaration)

```vb
Property ForceSurfaceContact As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IJoinFeatureData
Dim value As System.Boolean

instance.ForceSurfaceContact = value

value = instance.ForceSurfaceContact
```

### C#

```csharp
System.bool ForceSurfaceContact {get; set;}
```

### C++/CLI

```cpp
property System.bool ForceSurfaceContact {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to join any coincident faces and any intruding volumes, false to not

## VBA Syntax

See [JoinFeatureData::ForceSurfaceContact](ms-its:sldworksapivb6.chm::/sldworks~JoinFeatureData~ForceSurfaceContact.html).

## See Also

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.html)
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
