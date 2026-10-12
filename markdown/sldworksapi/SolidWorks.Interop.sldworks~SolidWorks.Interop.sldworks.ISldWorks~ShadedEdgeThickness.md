---
title: "ShadedEdgeThickness Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ShadedEdgeThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShadedEdgeThickness.html"
---

# ShadedEdgeThickness Property (ISldWorks)

Gets or sets the edge thickness when the display style is "Shaded with Edges".

## Syntax

### Visual Basic (Declaration)

```vb
Property ShadedEdgeThickness As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

instance.ShadedEdgeThickness = value

value = instance.ShadedEdgeThickness
```

### C#

```csharp
System.int ShadedEdgeThickness {get; set;}
```

### C++/CLI

```cpp
property System.int ShadedEdgeThickness {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Edge thickness

## VBA Syntax

See [SldWorks::ShadedEdgeThickness](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ShadedEdgeThickness.html).

## Remarks

This property is valid only when the Render system is turned on. To turn on the Render system, select **Tools > Options > System Options > Performance > Enhanced graphics performance (requires SOLIDWORKS restart)**.

The set value of this property cannot exceed 6.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
