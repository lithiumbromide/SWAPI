---
title: "GetReverseOffset Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "GetReverseOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetReverseOffset.html"
---

# GetReverseOffset Method (ISurfExtrudeFeatureData)

Gets the reverse offset direction setting for the end condition of this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReverseOffset( _
   ByVal Fwd As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Fwd As System.Boolean
Dim value As System.Boolean

value = instance.GetReverseOffset(Fwd)
```

### C#

```csharp
System.bool GetReverseOffset(
   System.bool Fwd
)
```

### C++/CLI

```cpp
System.bool GetReverseOffset(
   System.bool Fwd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Fwd`: True gets the reverse offset setting in the forward direction, false gets it in the reverse direction

### Return Value

True if the reverse offset setting is enabled, false if it is disabled

## VBA Syntax

See [SurfExtrudeFeatureData::GetReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~GetReverseOffset.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::SetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetReverseOffset.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
