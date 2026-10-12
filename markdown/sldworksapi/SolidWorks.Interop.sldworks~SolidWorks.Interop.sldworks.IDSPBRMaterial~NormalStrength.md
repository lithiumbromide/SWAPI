---
title: "NormalStrength Property (IDSPBRMaterial)"
project: "SOLIDWORKS API Help"
interface: "IDSPBRMaterial"
member: "NormalStrength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial~NormalStrength.html"
---

# NormalStrength Property (IDSPBRMaterial)

Gets or sets the normal strength for this material.

## Syntax

### Visual Basic (Declaration)

```vb
Property NormalStrength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDSPBRMaterial
Dim value As System.Double

instance.NormalStrength = value

value = instance.NormalStrength
```

### C#

```csharp
System.double NormalStrength {get; set;}
```

### C++/CLI

```cpp
property System.double NormalStrength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Normal strength

## VBA Syntax

See [DSPBRMaterial::NormalStrength](ms-its:sldworksapivb6.chm::/sldworks~DSPBRMaterial~NormalStrength.html).

## See Also

[IDSPBRMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial.html)
[IDSPBRMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDSPBRMaterial_members.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
