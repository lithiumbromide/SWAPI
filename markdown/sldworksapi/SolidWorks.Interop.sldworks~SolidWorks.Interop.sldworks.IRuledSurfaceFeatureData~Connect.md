---
title: "Connect Property (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "Connect"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~Connect.html"
---

# Connect Property (IRuledSurfaceFeatureData)

Gets or sets whether or not to connect the surfaces of this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Connect As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim value As System.Boolean

instance.Connect = value

value = instance.Connect
```

### C#

```csharp
System.bool Connect {get; set;}
```

### C++/CLI

```cpp
property System.bool Connect {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to connect surfaces, false to remove connecting surfaces

## VBA Syntax

See [RuledSurfaceFeatureData::Connect](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~Connect.html).

## Remarks

Connecting surfaces are usually created between sharp corners.

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
