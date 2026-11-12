---
title: "Clockwise Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "Clockwise"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~Clockwise.html"
---

# Clockwise Property (IHelixFeatureData)

Gets or sets the direction of the turns of this helix feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Clockwise As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim value As System.Boolean

instance.Clockwise = value

value = instance.Clockwise
```

### C#

```csharp
System.bool Clockwise {get; set;}
```

### C++/CLI

```cpp
property System.bool Clockwise {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if direction of turns is clockwise, false if counterclockwise

## VBA Syntax

See [HelixFeatureData::Clockwise](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~Clockwise.html).

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
