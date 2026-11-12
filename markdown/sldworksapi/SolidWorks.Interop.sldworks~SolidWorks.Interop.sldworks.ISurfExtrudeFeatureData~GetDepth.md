---
title: "GetDepth Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "GetDepth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetDepth.html"
---

# GetDepth Method (ISurfExtrudeFeatureData)

Gets the depth of the feature in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDepth( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
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

- `Forward`: True gets the depth in the forward direction, false gets it in the reverse direction

### Return Value

Extrusion depth

## VBA Syntax

See [SurfExtrudeFeatureData::GetDepth](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~GetDepth.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::SetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetDepth.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
