---
title: "GetFace Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "GetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetFace.html"
---

# GetFace Method (ISurfExtrudeFeatureData)

Gets the end condition face for this extruded surface in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFace( _
   ByVal Forward As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As System.Object

value = instance.GetFace(Forward)
```

### C#

```csharp
System.object GetFace(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.Object^ GetFace(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True gets the end condition face in the forward direction, false gets it in the reverse direction

### Return Value

End condition [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [SurfExtrudeFeatureData::GetFace](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~GetFace.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::SetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetFace.html)
[ISurfExtrudeFeatureData::IGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetFace.html)
[ISurfExtrudeFeatureData::ISetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetFace.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
