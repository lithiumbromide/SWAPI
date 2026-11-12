---
title: "IGetVertex Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "IGetVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetVertex.html"
---

# IGetVertex Method (ISurfExtrudeFeatureData)

Gets the end condition vertex in the forward or reverse direction for this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVertex( _
   ByVal Forward As System.Boolean _
) As Vertex
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As Vertex

value = instance.IGetVertex(Forward)
```

### C#

```csharp
Vertex IGetVertex(
   System.bool Forward
)
```

### C++/CLI

```cpp
Vertex^ IGetVertex(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True gets the vertex in the forward direction, false gets it in the reverse direction

### Return Value

End condition [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [SurfExtrudeFeatureData::IGetVertex](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~IGetVertex.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::GetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetVertex.html)
[ISurfExtrudeFeatureData::ISetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetVertex.html)
[ISurfExtrudeFeatureData::SetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetVertex.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
