---
title: "IVertex Property (ISimpleHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData"
member: "IVertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData~IVertex.html"
---

# IVertex Property (ISimpleHoleFeatureData)

Obsolete. Superseded by [ISimpleHoleFeatureData2::IVertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~IVertex.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IVertex As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData
Dim value As Vertex

instance.IVertex = value

value = instance.IVertex
```

### C#

```csharp
Vertex IVertex {get; set;}
```

### C++/CLI

```cpp
property Vertex^ IVertex {
   Vertex^ get();
   void set (    Vertex^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SimpleHoleFeatureData::IVertex](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData~IVertex.html).

## See Also

[ISimpleHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData.html)
[ISimpleHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData_members.html)
