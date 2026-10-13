---
title: "GetDepth Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetDepth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDepth.html"
---

# GetDepth Method (IExtrudeFeatureData2)

Gets the depth of the extrusion feature in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDepth( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim value As System.Double

value = instance.GetDepth(Forward)
```

### C#

```csharp
System.double GetDepth(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.double GetDepth(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward feature direction, false for reverse

### Return Value

Depth of the extrusion

## VBA Syntax

See [ExtrudeFeatureData2::GetDepth](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetDepth.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::SetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDepth.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
