---
title: "RoundSharpEdges Property (IAppearanceSetting)"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: "RoundSharpEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting~RoundSharpEdges.html"
---

# RoundSharpEdges Property (IAppearanceSetting)

Gets or sets the value by which to round sharp edges when rendering a model using a ray-trace rendering engine.

## Syntax

### Visual Basic (Declaration)

```vb
Property RoundSharpEdges As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
Dim value As System.Double

instance.RoundSharpEdges = value

value = instance.RoundSharpEdges
```

### C#

```csharp
System.double RoundSharpEdges {get; set;}
```

### C++/CLI

```cpp
property System.double RoundSharpEdges {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value by which to round sharp edges

## VBA Syntax

See [AppearanceSetting::RoundSharpEdges](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting~RoundSharpEdges.html).

## Remarks

This method:

- is only available when a ray-trace rendering engine is loaded.
- does not change model geometry.

## See Also

[IAppearanceSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)
[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
