---
title: "GetVertex Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "GetVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetVertex.html"
---

# GetVertex Method (ISurfExtrudeFeatureData)

Gets the end condition vertex in the forward or reverse direction for this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertex( _
   ByVal Forward As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As System.Object

value = instance.GetVertex(Forward)
```

### C#

```csharp
System.object GetVertex(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.Object^ GetVertex(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True gets the vertex in the forward direction, false gets it in the reverse direction

### Return Value

End condition [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [SurfExtrudeFeatureData::GetVertex](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~GetVertex.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::SetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetVertex.html)
[ISurfExtrudeFeatureData::IGetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetVertex.html)
[ISurfExtrudeFeatureData::ISetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetVertex.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
