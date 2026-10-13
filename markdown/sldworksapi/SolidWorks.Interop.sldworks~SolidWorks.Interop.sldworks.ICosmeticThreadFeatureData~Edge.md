---
title: "Edge Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "Edge"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~Edge.html"
---

# Edge Property (ICosmeticThreadFeatureData)

Gets or sets the circular edge to which this cosmetic thread is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Property Edge As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As Edge

instance.Edge = value

value = instance.Edge
```

### C#

```csharp
Edge Edge {get; set;}
```

### C++/CLI

```cpp
property Edge^ Edge {
   Edge^ get();
   void set (    Edge^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Circular [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) to which this cosmetic thread is attached

## VBA Syntax

See [CosmeticThreadFeatureData::Edge](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~Edge.html).

## Examples

[Get Cosmetic Threads Features in a Part (VBA)](Get_Cosmetic_Threads_in_a_Part_Document_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2003 SP5, Revision Number 11.5
